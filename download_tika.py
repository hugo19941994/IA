'''Downloads Apache Tika for file conversion'''
import urllib.request as urllib2
import hashlib
import os.path


def get_file(url):
    '''Obtencion del nombre del archivo (Ultima parte de la url)'''
    filename = url.split('/')[-1]
    if not filename:
        filename = ''
    return filename


def chunk_report(bytes_so_far, total_size):
    '''Informs user about the percentage of the download'''
    percent = float(bytes_so_far) / total_size
    percent = round(percent*100, 2)
    if percent % 5 == 0:
        print("Descargados %d de %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))

    if bytes_so_far >= total_size:
        print('\nDescarga Completa\n')


def download(url, chunk_size=8192, report_hook=None):
    '''Downloads the actual file'''
    urlresponse = urllib2.urlopen(url)
    filename = getFile(url)

    # Obtencion de la longitud de archivo
    meta = urlresponse.info()
    meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
    meta_length = meta_func("Content-Length")
    total_size = None
    if meta_length:
        total_size = int(meta_length[0])

    bytes_so_far = 0

    with open(filename, 'wb') as file:
        while True:
            chunk = urlresponse.read(chunk_size)
            bytes_so_far += len(chunk)
            file.write(chunk)
            if not chunk:
                break

            if report_hook:
                report_hook(bytes_so_far, chunk_size, total_size)

    return bytes_so_far


def comprobarApacheTika(url):
    filename = get_file(url)
    if filename == '':
        print("Nombre de archivo de ApacheTika no obtenido")
        exit()

    if not os.path.exists(filename):
        print("Apache Tika no encontrado, procediendo a su descarga: \n")
        download(url, report_hook=chunk_report)

    if not os.path.exists(filename):
        print("Apache Tika no encontrado en el directorio")
        exit()

    if os.path.exists(filename):
        # Comprobar Tika con su SHA1
        with open(filename, 'rb') as file:
            if hashlib.sha1(file.read()).hexdigest() == "59cc7c4c48a6a41899ca282d925b2738d05a45a8":
                print("SHA1 correcto")
            else:
                print("SHA1 incorrecto\nBorra el archivo y prueba otra vez")
                exit()
