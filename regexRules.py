import re
# Posibles cabeceras y e-mails
regexEmail = re.compile(r'[\w.-]+@[\w.-]+')
regexDatos = re.compile("Datos personales|Nombre[s]|Apellido[s]", re.IGNORECASE)
regexFormacion = re.compile("Preparaci[o|ó]n|Acad[e|é]mic[a|o]|Formaci[o|ó]n|Titulo[s]|"
                        "Certificaci[ó|o]n[es]|Estudios|Seminario[s]|Extra[-]academic[a|o]",
                        re.IGNORECASE)
regexExperiencia = re.compile("Experiencia|Profesional|Laboral|Cargos|Empresa", re.IGNORECASE)
regexIdiomas = re.compile("Idioma[s]|Ingl[e|é]s|Franc[e|é]s|Italiano|Alem[a|á]n|Chino|Ruso|Japon[e|é]s|Le[i|í]do|Escrito|Oral|Niv[e|é]l", re.IGNORECASE)
regexLibros = re.compile("[Co][-]Autor[a]|Publicaci[o|ó]n[es]", re.IGNORECASE)
regexExtra = re.compile("Deporte[s]|Hobby|Hobbies|Extra[-]academic[o|a]|Extra[-]curricular", re.IGNORECASE)

regxRules = [regexDatos, regexFormacion, regexExperiencia, regexIdiomas, regexLibros, regexExtra]
