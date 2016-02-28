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

import glob
import errno
import sys
import pickle
import json
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
    comprobar_apache_tika('http://ftp.cixug.es/apache/tika/tika-app-1.12.jar')
    # Descargar tokenizador de NLTK
    print("Comprobando el tokenizador de NLTK...")
    # nltk.download()
    nltk.download("punkt")
    # Cargar tokenizador de español
    print("Cargando el tokenizador...")
    #tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
    tokenizer = pickle.load(open("nltk/spanish.pickle", 'rb'))
    # Spanish conll2002 POS tagger
    tagger = pickle.load(open("nltk/conll2002_aubt.pickle", 'rb'))
    # Chunker para español entrenado con corpus Conll2002 usando Naive Bayes
    #chunker = nltk.data.load("chunkers/conll2002_NaiveBayes.pickle")
    chunker = pickle.load(open("nltk/conll2002_NaiveBayes.pickle", 'rb'))
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

    activate_chunker = input("Do you want the chunker results? (y/n) ")

    # Lectura de de los curriculums en formato pdf, html, Word y OpenOfice
    files = [f for f in glob.glob(path)
             if f.lower().endswith((".pdf", ".html", ".doc", ".docx", ".odt"))]

    for name in files:
        try:
            # Usar tika para pasar archivo a texto plano
            raw = subprocess.check_output(["java", "-jar",
                                           "tika-app-1.12.jar",
                                           "-t", name],
                                          universal_newlines=True)

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

            os.makedirs("./out/" + name, exist_ok=True)
            print("Escribiendo salida de fichero de " + name +
                  "section.json\n")
            json.dump(section_json, open("./out/" + name + "/section.json", 'w'),
                      sort_keys=True, indent=4, separators=(',', ': '))

            if activate_chunker == 'y':
                # Separa la linea por palabras (whitespace)
                # y agrega tag (tipo de palabra)
                # Recorre todas las listas
                cdp, cf, cel, ci, cl, ce, cem = ({} for i in range(7))
                lista_chunker = [cdp, cf, cel, ci, cl, ce, cem]

                for lista, lchunk in zip(listas, lista_chunker):
                    if not len(lista) == 0:  # Excepto si estan vacias
                        # Separa cada palabra
                        word = [words for segments in lista for words in segments.split()]

                        # POS Tagging y Chunker entrenados con Conll2002 español y Naive Bayes
                        chk_tree = chunker.parse(tagger.tag(word))
                        personas, lugares, organizaciones = ([] for i in range(3))
                        for subtree in chk_tree.subtrees(filter=lambda t: t.label() == 'PER'):
                            personas.append(" ".join([a for (a, b) in subtree.leaves()]))
                        for subtree in chk_tree.subtrees(filter=lambda t: t.label() == 'ORG'):
                            organizaciones.append(" ".join([a for (a, b) in subtree.leaves()]))
                        for subtree in chk_tree.subtrees(filter=lambda t: t.label() == 'LOC'):
                            lugares.append(" ".join([a for (a, b) in subtree.leaves()]))
                        lchunk['S'] = {"Personas": personas, "Organizaciones": organizaciones,
                                       "Lugares": lugares}
                chunker_json = {'Chunker - Datos Personales': cdp,
                                'Chunker - Formacion': cf, 'Chunker - Experiencia Laboral': cel,
                                'Chunker - Idiomas': ci, 'Chunker - Libros': cl,
                                'Chunker - Extras': ce, 'Chunker - Emails': cem}

                # Escritura a JSON
                print("\nEscribiendo salida de fichero de " + name + "chunker.json\n")
                json.dump(chunker_json, open("./out/" + name + "/chunker.json", 'w'),
                          sort_keys=True, indent=4, separators=(',', ': '))

        except IOError as exc:
            # No fallar si otro directorio es encontrado, simplemente ignorarlo
            if exc.errno != errno.EISDIR:
                raise  # Propagacion de errores

main()
