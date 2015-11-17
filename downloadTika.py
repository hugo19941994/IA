import urllib.request
import shutil
import os.path
import hashlib
import time
import threading


def mientrasDescarga():
    spaces = 0
    while run:
        sys.stdout.write(" " * spaces + ".\r")
        if spaces >= 10:
            sys.stdout.write(" " * 11 + "\r")
            spaces = 0
        else:
            spaces += 1
        time.sleep(1)
    return


def descargaTika():
    # Comprobar si Tika 1.11 existe en la carpeta
    if (not os.path.isfile("tika-app-1.11.jar")):
        # Se descarga si no está
        print("Descargando Tika 1.11")

        # Imprimimos mensaje por consola para que no parezca que el programa esta parado
        run = True
        t = threading.Thread(target=mientrasDescarga, daemon=True)
        t.start()

        with urllib.request.urlopen("http://ftp.cixug.es/apache/tika/tika-app-1.11.jar") as response, open("tika-app-1.11.jar", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        run = False

    # Comprobar Tika con su SHA1
    with open("tika-app-1.11.jar", 'rb') as f:
        if hashlib.sha1(f.read()).hexdigest() == "59cc7c4c48a6a41899ca282d925b2738d05a45a8":
            print("Tika tiene SHA1 correcto")
        else:
            print("Tika no tiene SHA1 correcto\nBorra el archivo de Tika y prueba otra vez")
            exit()
