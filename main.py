# UEM/Everis - Proyecto Integrador 2015-2016
# Inteligencia Artificial
# * Jorge De Castro Cabello
# * Hugo Ferrando Seage
# * Santiago Gualda Torrijos
# * Cristian López-Ramos Rivera
# TODO: Name Entity Recognition, Web service?, improve segmentation, HMM?, JSON or YAML export?

import nltk
import sys
import glob
import errno

from nltk import *
#nltk.download("punkt") #Activar para descargar paquetes de NLTK

def creartxt(name):
    archi=open(name + '.txt','w')
    archi.close()

def escribirtxt(datos, educacion, laboral, emails):
    
    archi=open(name + '.txt','w')
    
    archi.write("Datos Personales:\n")
    for palabra in datos:
        archi.write(palabra + "\n")
        
    archi.write("\nEducacion:\n")
    for palabra in educacion:
        archi.write(palabra + "\n")

    archi.write("\nExperiencia Laboral:\n")
    for palabra in laboral:
        archi.write(palabra + "\n")
   
    archi.write("\nEmails Encontrados:\n")
    for palabra in emails:
        archi.write(palabra + "\n")

#Directorio de los curriculums
path = 'cv/*.pdf'   

#Lectura de de los curriculums
files = glob.glob(path)

for name in files: # name = curriculum name
    try:
        with open(name) as f: # No need to specify 'r': this is the default.
            # Usar tika para pasar archivo a texto plano
            raw = subprocess.getoutput(["java", "-jar",  "tika-app-1.11.jar",  "-t", name])
            # Cargar tokenizador español
            tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")

            #Crear fichero a escribir
            creartxt(name)

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

            #Escritura a fichero txt
            escribirtxt(datos, educacion, laboral, emails)
  
    except IOError as exc:
        if exc.errno != errno.EISDIR: # No fallar si otro directorio es encontrado, simplemente ignorarlo
            raise # Propagacion de errores
