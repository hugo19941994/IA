import urllib.request as urllib2
import hashlib
import time
import threading

run = True
status = ""


def mientrasDescarga():
    while run:
        print(status, end="")
        time.sleep(2)
    return


def download(url):
    urlresponse = urllib2.urlopen(url)

    # Obtención del nombre del archivo (última parte de la url)
    filename = url.split('/')[-1]
    if not filename:
        filename = 'downloaded file'

    # Escritura de archivo en modo wb (write binary mode)
    with open(filename, 'wb') as f:
        # Obtención de la longitud de archivo
        meta = urlresponse.info()
        meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
        meta_length = meta_func("Content-Length")
        file_size = None
        if meta_length:
            file_size = int(meta_length[0])

        print("Descargando: {0} Bytes: {1}".format(url, file_size))

        file_size_dl = 0
        block_sz = 8192
        statusthread = threading.Thread(target=mientrasDescarga, daemon=True)
        statusthread.start()
        while True:
            buffer = urlresponse.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)

            status = "{0:16}".format(file_size_dl)
            if file_size:
                status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
            status += chr(13)
        run = False
        print()

    # Comprobar Tika con su SHA1
    with open("tika-app-1.11.jar", 'rb') as f:
        if hashlib.sha1(f.read()).hexdigest() == "59cc7c4c48a6a41899ca282d925b2738d05a45a8":
            print("Tika tiene SHA1 correcto")
        else:
            print("Tika no tiene SHA1 correcto\nBorra el archivo de Tika y prueba otra vez")

    return filename


url = "http://ftp.cixug.es/apache/tika/tika-app-1.11.jar"
name = download(url)
print(name)
