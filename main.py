import nltk, sys
from nltk import *
#nltk.download()

name = sys.argv[1]

raw = subprocess.getoutput(["java", "-jar",  "tika-app-1.11.jar",  "-t", name])
#f = open("D:\\Users\\Hugo\\Desktop\\t\\t.txt")

tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
#tokens = tokenizer.tokenize(raw)

paragraphs = [p for p in raw.split('\n') if p]
par, emails, datos, educacion, laboral = [], [], [], [], []
for paragraph in paragraphs:
    tokens = tokenizer.tokenize(paragraph)
    for p in tokens:
        par.append(p)

# for t in par:
    # print(t)
#print("\n")

last = "datos"
for t in par:
    if re.search("[\w.]@[\w.]", t) != None:
        print("ENCONTRADO EMAIL")
        print(t)
        emails.append(re.search("[\w.]@[\w.]", t))
    if ("DATOS PERSONALES" or "Datos Personales" or "Nombre" or "Apellido") in t:
        print("ENCONTRADO SEGMENTO DATOS PERSONALES")
        last = "datos"
    if("PREPARACION ACADEMICA" or "Formacion" or "Certificaciones" or "Estudios" or "Cursos" or "Titulos" or "Titulo" or "Academica" or "Academico" or "Seminarios" or "Extraacademica") in t:
        print("ENCONTRADO SEGMENTO FORMACION")
        last = "educacion"
    if("Experiencia" or "Profesional" or "Laboral" or "Cargos" or "Empresa") in t:
        print("ENCONTRADO SEGMENTO EXPERIENCIA LABORAL")
        last = "laboral"

    if last == "datos":
        datos.append(t)
    elif last == "educacion":
        educacion.append(t)
    elif last == "laboral":
        laboral.append(t)

print("\nDatos Personales:")
print(datos)
print("\nEducacion:")
print(educacion)
print("\nExperiencia Laboral:")
print(laboral)
print(emails)