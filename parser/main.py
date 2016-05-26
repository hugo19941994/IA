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
# TODO: Improve chunker results (train with another dataset?)
# TODO: Remove blank results
# TODO: Check argv for chunker activation

import os
import errno
import sys
import glob
import requests
import json
import pickle
import nltk
from download_tika import comprobar_apache_tika
from regex_rules import *
from nltk import *


def main():
    '''Main routine - Checks dependencies, parses CV,
    extracts information and dumps it into a JSON file'''
    print("Iniciando el segmentador de curriculums...\n")

    # Descargar Tika
    print("Comprobando TIKA...")
    comprobar_apache_tika('http://ftp.cixug.es/apache/tika/tika-app-1.13.jar')
    # Descargar tokenizador de NLTK
    print("Comprobando el tokenizador de NLTK...")
    nltk.download("punkt")
    # Cargar tokenizador de español
    print("Cargando el tokenizador...")
    tokenizer = pickle.load(open("nltk/spanish.pickle", 'rb'))
    # Stemmer para español que viene con NLTK
    stemmer = nltk.SnowballStemmer("spanish")

    # Determinar si se lee desde el directorio de curriculums
    # o si se pasa el curriculum por parámetros
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print("Se procesara el siguiente curriculum: " + path + "\n")
    else:
        path = 'cv/*.*'
        print("Se procesaran los curriculums de la carpeta " + path + "\n")

    print("Procesando...")

    # Lectura de de los curriculums en formato pdf, html, Word y OpenOfice
    files = [f for f in glob.glob(path)
             if f.lower().endswith((".pdf", ".html", ".doc", ".docx", ".odt"))]

    for count, name in enumerate(files):
        try:
            # Usar tika para pasar archivo a texto plano
            raw = subprocess.check_output(["java", "-jar",
                                           "tika-app-1.13.jar",
                                           "-t", name],
                                          universal_newlines=False).decode('utf-8')

            # Eliminate lines that cointain only whitespace
            raw = "".join([s for s in raw.strip().splitlines(True) if s.strip()])

            print("Procesando " + name + "\n")

            # Crear e inicializar listas
            par, emails, datos, educacion, laboral, idiomas, libros, extras = ([] for i in range(8))
            listas = [datos, educacion, laboral, idiomas, libros, extras, emails]

            # User stemmer de español
            raw2 = stemmer.stem(raw)

            print("Tokenizando el contenido...")
            # Cortar texto en párrafos
            paragraphs = [p for p in raw2.split('\n') if p]
            for paragraph in paragraphs:
                # Tokenizar cada parrafo
                tokens = tokenizer.tokenize(paragraph)
                for token in tokens:
                    par.append(token)  # Poner cada token en el mismo array

            # 0 = Datos Personales, 1 = Formación,
            # 2 = Exp Laboral, 3 = Idiomas, 4 = Emails
            last = 0
            for token in par:  # Buscar cabeceras
                # Recorre todas las regex
                for num, reg in enumerate(REGEX_RULES):
                    if reg.match(token):  # Si coincide
                        last = num
                        break
                # Poner contenido de un segmento en su propio array
                listas[last].append(token)

            for token in datos:  # Buscar e-mails dentro de Datos personales
                match = REGEX_EMAIL.findall(token)
                for email in match:
                    emails.append(email)

            # Escritura a JSON
            section_json = {'Datos Personales': listas[0],
                            'Formacion': listas[1],
                            'Experiencia Laboral': listas[2],
                            'Idiomas': listas[3],
                            'Libros': listas[4],
                            'Extras': listas[5],
                            'Emails': listas[6]}

            os.makedirs("./out/section", exist_ok=True)
            os.makedirs("./out/chunker", exist_ok=True)

            print("Escribiendo salida de fichero de ./out/section/" + str(count) + ".json\n")
            json.dump(section_json, open("./out/section/" + str(count) + ".json", 'w'),
                      sort_keys=True, indent=4, separators=(',', ': '))

            # Name Entity Recognition with raw text
            # Text must be divided into smaller pieces becuase Alchemy doesn't
            # accept very long text
            final_json = []
            with open('./apikey.txt', 'r') as f:
                apikey = f.readline()
            raw_parts = textwrap.wrap(raw, 1000)  # 1000 letter max parts
            for part in raw_parts:
                print(count)
                payload = {'apikey': apikey[:-1], 'text': part, 'outputMode': 'json'}
                r = requests.get('http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities', params=payload)
                for entity in r.json()['entities']:
                    final_json.append(entity)

            # Escritura a JSON
            print("\nEscribiendo salida de fichero de ./out/chunker/" + str(count) + ".json\n")
            json.dump(final_json, open("./out/chunker/" + str(count) + ".json", 'w'),
                      sort_keys=True, indent=4, separators=(',', ': '))

        except IOError as exc:
            # No fallar si otro directorio es encontrado, simplemente ignorarlo
            if exc.errno != errno.EISDIR:
                raise  # Propagacion de errores

            print(raw.split('\n', 1)[1])
main()
