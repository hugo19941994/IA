import urllib.request as urllib2
import hashlib


def chunk_report(bytes_so_far, chunk_size, total_size):
    percent = float(bytes_so_far) / total_size
    percent = round(percent*100, 2)
    if percent % 5 == 0:
        print("Descargados %d de %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))

    if bytes_so_far >= total_size:
        print('\nDescarga Completa\n')


def chunk_read(url, chunk_size=8192, report_hook=None):
    urlresponse = urllib2.urlopen(url)
    meta = urlresponse.info()
    meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
    meta_length = meta_func("Content-Length")
    total_size = None
    if meta_length:
        total_size = int(meta_length[0])
    bytes_so_far = 0

    while True:
        chunk = urlresponse.read(chunk_size)
        bytes_so_far += len(chunk)

        if not chunk:
            break

        if report_hook:
            report_hook(bytes_so_far, chunk_size, total_size)

    return bytes_so_far


chunk_read('http://ftp.cixug.es/apache/tika/tika-app-1.11.jar', report_hook=chunk_report)

# Comprobar Tika con su SHA1
with open("tika-app-1.11.jar", 'rb') as f:
    if hashlib.sha1(f.read()).hexdigest() == "59cc7c4c48a6a41899ca282d925b2738d05a45a8":
        print("SHA1 correcto")
    else:
        print("SHA1 incorrecto\nBorra el archivo y prueba otra vez")
