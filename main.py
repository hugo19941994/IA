# UEM/Everis - Proyecto Integrador 2015-2016
# Inteligencia Artificial
# * Jorge De Castro Cabello
# * Hugo Ferrando Seage
# * Santiago Gualda Torrijos
# * Cristian López-Ramos Rivera
# TODO: Name Entity Recognition, Web service?, improve segmentation, HMM?, JSON or YAML export?

import nltk
import sys
from nltk import *
# nltk.download() Activar para descargar paquetes de NLTK

# Nombre de archivo es primer argumento
name = sys.argv[1]
# Usar tika para pasar archivo a texto plano
raw = subprocess.getoutput(["java", "-jar",  "tika-app-1.11.jar",  "-t", name])
# Cargar tokenizador español
tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")

par, emails, datos, educacion, laboral = [], [], [], [], []

# Cortar texto en parrafos
paragraphs = [p for p in raw.split('\n') if p]
for paragraph in paragraphs:
    tokens = tokenizer.tokenize(paragraph)  # Tokenizar cada parrafo
    for p in tokens:
        par.append(p)  # Poner tokens en el mismo array

# Posibles cabeceras e emails
regexEmail = re.compile(r'[\w.-]+@[\w.-]+')
regexDatos = re.compile("Datos personales|Nombre[s]|Apellido[s]", re.IGNORECASE)
regexFormacion = re.compile("Preparaci[o|ó]n|Acad[e|é]mic[a|o]|Formaci[o|ó]n|Titulo[s]|Certificaci[ó|o]n[es]|"
                            "Estudios|Cursos|Seminario[s]|Extra[-]academic[a|o]", re.IGNORECASE)
regexExperiencia = re.compile("Experiencia|Profesional|Laboral|Cargos|Empresa", re.IGNORECASE)

last = 0  # 0 = Datos Personales, 1 = Formación, 2 = Exp Laboral
for t in par:
    # Buscar e-mails
    match = regexEmail.findall(t)
    for email in match:
        emails.append(email)
    # Buscar cabeceras
    if regexDatos.match(t):
        print("Datos personales encontrados!")
        last = 0
    if regexFormacion.match(t):
        print("Formación encontrada!")
        last = 1
    if regexExperiencia.match(t):
        print("Experiencia laboral encontrada!")
        last = 2
    # Poner contenido de un segmento en su propio array
    if last == 0:
        datos.append(t)
    elif last == 1:
        educacion.append(t)
    elif last == 2:
        laboral.append(t)

print("\nDatos Personales:")
print(datos)
print("\nEducacion:")
print(educacion)
print("\nExperiencia Laboral:")
print(laboral)
print("\nEmails Encontrados:")
print(emails)
