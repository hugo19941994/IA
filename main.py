# UEM/Everis - Proyecto Integrador 2015-2016
# Inteligencia Artificial
# * Jorge De Castro Cabello
# * Hugo Ferrando Seage
# * Santiago Gualda Torrijos
# * Cristian López-Ramos Rivera
# TODO: Name Entity Recognition, Web service?, improve segmentation, HMM?, JSON or YAML export?, choose mirror dynamically?, poner porcentaje descargar en vez de puntos

import nltk
import glob
import errno
from downloadTika import *
from regexRules import *
from nltk import *


def creartxt(name):
    archi = open(name + '.txt', 'w')
    archi.close()


def escribirtxt(lists):
    archi = open(name + '.txt', 'w')
    for i, lista in enumerate(lists):
        if i == 0:
            archi.write("Datos Personales:\n")
        elif i == 1:
            archi.write("\nEducacion:\n")
        elif i == 2:
            archi.write("\nExperiencia Laboral:\n")
        elif i == 3:
            archi.write("\nIdiomas:\n")
        elif i == 4:
            archi.write("\nLibros:\n")
        elif i == 5:
            archi.write("\nExtras:\n")
        elif i == 6:
            archi.write("\nEmails Encontrados:\n")
        for palabra in lista:
            archi.write(palabra + "\n")

print("Iniciando el segmentador de curriculums...\n")

# Descargar Tika
print("Comprobando TIKA...")
descargaTika()
# Descargar tokenizador de NLTK
print("Comprobando el tokenizador de NLTK...")
nltk.download("punkt")
# Cargar tokenizador de español
print("Cargando el tokenizador...")
tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")

# Determinar si se lee desde el directorio de curriculums o si se pasa el curriculum por parámetros
if len(sys.argv) > 1:
    path = sys.argv[1]
    print("Se procesara el siguiente curriculum: " + path + "\n")
else:
    path = 'cv/*.*'
    print("Se procesaran los curriculums de la carpeta " + path + "\n")

print("Procesando...")

# Lectura de de los curriculums en formato pdf, html, Word y OpenOfice
files = [f for f in glob.glob(path) if f.lower().endswith((".pdf", ".html", ".doc", ".docx", ".odt"))]

for name in files:
    try:
        with open(name) as f:
            # Usar tika para pasar archivo a texto plano
            raw = subprocess.check_output(["java", "-jar",  "tika-app-1.11.jar",  "-t", name], universal_newlines=True)

            # Crear fichero a escribir
            creartxt(name)
            print("Procesando " + name + "\n")

            # Crear e inicializar listas
            par, emails, datos, educacion, laboral, idiomas, libros, extras = ([] for i in range(8))
            listas = [datos, educacion, laboral, idiomas, libros, extras, emails]

            # Cortar texto en párrafos
            paragraphs = [p for p in raw.split('\n') if p]
            print("Tokenizando el contenido...")
            for paragraph in paragraphs:
                tokens = tokenizer.tokenize(paragraph)  # Tokenizar cada parrafo
                for p in tokens:
                    par.append(p)  # Poner cada token en el mismo array

            last = 0  # 0 = Datos Personales, 1 = Formación, 2 = Exp Laboral, 3 = Idiomas, 4 = Emails
            for t in par:  # Buscar cabeceras
                for i,r in enumerate(regxRules):  # Recorre todas las regex
                    if r.match(t):  # Si coincide
                        last = i
                        #print("Cabecera encontrada:\n" + t)
                        break
                # Poner contenido de un segmento en su propio array
                listas[last].append(t)

            for t in datos:  # Buscar e-mails dentro de Datos personales
                match = regexEmail.findall(t)
                for email in match:
                    #print("Email encontrado!")
                    emails.append(email)

            # Escritura a fichero txt
            print("\nEscribiendo salida de fichero de " + name + ".txt\n")
            escribirtxt(listas)

    except IOError as exc:
        if exc.errno != errno.EISDIR:  # No fallar si otro directorio es encontrado, simplemente ignorarlo
            raise  # Propagacion de errores
