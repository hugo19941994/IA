'''
UEM/Everis - Proyecto Integrador 2015-2016
Inteligencia Artificial
* Jorge De Castro Cabello
* Hugo Ferrando Seage
* Santiago Gualda Torrijos
* Cristian López-Ramos Rivera
Description: Parses CV files (in several formats)
             and outputs useful information in JSON
'''

import os
import errno
import sys
import glob
import json
import pickle
import subprocess
import textwrap
import requests
import nltk
from download_tika import comprobar_apache_tika
from regex_rules import REGEX_RULES, REGEX_EMAIL


def check_download():
    '''Cheks if Tika and NLTK are installed.
    Proceeds to download if not present.
    Loads the spanish tokenizer and stemmer for later use'''

    print("Checking Apache Tika")
    comprobar_apache_tika('http://ftp.cixug.es/apache/tika/tika-app-1.13.jar')

    print("Checking NLTK and punkt")
    nltk.download("punkt")

    print("Loading spanish tokenizer and stemmer")
    tokenizer = pickle.load(open("nltk/spanish.pickle", 'rb'))
    stemmer = nltk.SnowballStemmer("spanish")

    return tokenizer, stemmer


def check_path():
    '''If an argument is present it will be used as
    the only folder or file to parse.
    If no argument is present all files inside the cv folder will be parsed'''

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = 'cv/*.*'

    print("Parsing following file/folder: " + path)

    # Accepted file formats: PDF, HTML, Word, OpenOffice
    files = [f for f in glob.glob(path)
             if f.lower().endswith((".pdf", ".html", ".doc", ".docx", ".odt"))]

    return files


def convert_to_plaintext(name):
    '''Use Apache Tike to convert files into plaintext ones
    Finally removes any line that contains no information'''

    # Use Tika to change format to plain text
    raw_text = subprocess.check_output(["java", "-jar",
                                        "tika-app-1.13.jar",
                                        "-t", name],
                                       universal_newlines=False).decode('utf-8')

    # Eliminate lines that cointain only whitespace
    return "".join([s for s in raw_text.strip().splitlines(True) if s.strip()])


def tokenize_plaintext(tokenizer, stemmed_text):
    '''Given a text split it into parragraphs and tokenize each one'''

    token_list = []
    # Divide text into parragraphs
    paragraphs = [p for p in stemmed_text.split('\n') if p]

    for paragraph in paragraphs:
        # Tokenize each parragraph
        tokens = tokenizer.tokenize(paragraph)
        for token in tokens:
            token_list.append(token)  # Each token on the same array
    return token_list


def search_sections(lists, tokens):
    '''Using a series of regex reules (representing a section of a CV)
    search for matches in every token.
    Every time a match occurs the following tokens will
    be placed in that category until a new match occurs'''

    # 0 = Datos Personales, 1 = Formación, 2 = Exp Laboral
    # 3 = Idiomas, 4 = Libros, 5 = Extras, 6 = Emails
    last = 0
    for token in tokens:  # Search for match
        # Using all regex rules
        for num, reg in enumerate(REGEX_RULES):
            if reg.match(token):  # Match
                last = num  # Change section
                break
        # Add token to corresponding list
        lists[last].append(token)

    for token in lists[0]:  # Search for emails inside 'Datos Personales'
        match = REGEX_EMAIL.findall(token)
        for email in match:
            lists[6].append(email)


def ner(stemmed_text):
    '''Perform Name Entity Recognition (NER) using the Aclhemy API
    The apikey must be placed into a plaintext file called apikey.txt
    The text that will be analyzed must be divided into smaller chunks due
    to the restrictions imposed by Alche,my'''

    alchemy_result = []
    with open('./apikey.txt', 'r') as apikey_file:
        apikey = apikey_file.readline()
    raw_parts = textwrap.wrap(stemmed_text, 1000)  # 1000 letter max parts
    for count, part in enumerate(raw_parts):
        print("Sending request " + str(count) + " to Alchemy")
        payload = {'apikey': apikey[:-1], 'text': part, 'outputMode': 'json'}
        req = requests.post('http://access.alchemyapi.com/calls/text/'
                            'TextGetRankedNamedEntities', params=payload)
        if req.json()['status'] == 'ERROR':
            print("Error in Alchemy, aborting Name Entity Recognition")
            break
        else:
            for entity in req.json()['entities']:
                alchemy_result.append(entity)
    return alchemy_result
    # payload = {'apikey': apikey[:-1],
    # 'text': stemmed_text, 'outputMode': 'json'}
    # req = requests.post('http://access.alchemyapi.com/calls/text/'
    # 'TextGetRankedNamedEntities', data=payload)
    # for entity in req.json()['entities']:
    # alchemy_result.append(entity)
    # return alchemy_result


def save_json(lists, alchemy_result, count):
    '''Saves the results of the parsed CV into a JSON file named as the index'''

    out_json = {'Datos Personales': lists[0],
                'Formacion': lists[1],
                'Experiencia Laboral': lists[2],
                'Idiomas': lists[3],
                'Libros': lists[4],
                'Extras': lists[5],
                'Emails': lists[6],
                'NER': alchemy_result}

    os.makedirs("./out", exist_ok=True)  # Folder where results are saved

    print("Writing file ./out/" + str(count) + ".json")

    json.dump(out_json, open("./out/" + str(count) + ".json", 'w'),
              sort_keys=True, indent=4, separators=(',', ': '))


def create_lists():
    '''Creates empty lists to store the different parts of the CVs'''
    par = []  # Stores parragraph tokens
    datos, educacion, laboral, idiomas, libros, extras, emails = ([] for i in range(7))
    return par, [datos, educacion, laboral, idiomas, libros, extras, emails]


def main():
    '''Main routine - Checks dependencies, parses CV,
    extracts information and dumps it into a JSON file'''
    print("Starting CV-Parser")

    tokenizer, stemmer = check_download()
    par, lists = create_lists()
    files = check_path()

    for count, name in enumerate(files):
        try:
            print("\nProcessing " + name)

            print("Converting to plain text")
            print("Stemming")
            # Stem plaintext using Spanish NLTK stemmer
            stemmed_text = stemmer.stem(convert_to_plaintext(name))

            print("Tokenizing")
            par = tokenize_plaintext(tokenizer, stemmed_text)

            print("Regex matching to search CV sections")
            search_sections(lists, par)

            print("Searching for Named Entities using Alchemy")
            alchemy_result = ner(stemmed_text)

            save_json(lists, alchemy_result, count)

        except IOError as exc:
            # No fallar si otro directorio es encontrado, simplemente ignorarlo
            if exc.errno != errno.EISDIR:
                raise  # Propagacion de errores

main()
