'''Regex rules used by the main program to find sections of a CV'''
import re

# Posibles cabeceras y e-mails
REGEX_EMAIL = re.compile(r'[\w.-]+@[\w.-]+')

REGEX_DATOS = re.compile("Datos personales|Nombre[s]|Apellido[s]", re.IGNORECASE)

REGEX_FORMACION = re.compile("Preparaci[o|ó]n|Acad[e|é]mic[a|o]|Formaci[o|ó]n|Titulo[s]|"
                             "Certificaci[ó|o]n[es]|Estudios|Seminario[s]|Extra[-]academic[a|o]",
                             re.IGNORECASE)

REGEX_EXPERIENCIA = re.compile("Experiencia|Profesional|Laboral|Cargos|Empresa", re.IGNORECASE)

REGEX_IDIOMAS = re.compile("Idioma[s]|Ingl[e|é]s|Franc[e|é]s|Italiano|Alem[a|á]n|Chino|Ruso|"
                           "Japon[e|é]s|Le[i|í]do|Escrito|Oral|Niv[e|é]l", re.IGNORECASE)

REGEX_LIBROS = re.compile("[Co][-]Autor[a]|Publicaci[o|ó]n[es]", re.IGNORECASE)

REGEX_EXTRA = re.compile("Deporte[s]|Hobby|Hobbies|"
                         "Extra[-]academic[o|a]|Extra[-]curricular", re.IGNORECASE)

REGEX_RULES = [REGEX_DATOS, REGEX_FORMACION, REGEX_EXPERIENCIA,
               REGEX_IDIOMAS, REGEX_LIBROS, REGEX_EXTRA]
