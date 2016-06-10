#!/bin/bash
# Este script permite indexar una carpeta entera que contenga
# ficheros json en un index de elasticSearch especificado
#
# Author: Jorge de Castro
# Auther: Hugo Ferrando Seage
# Version: 25/05/2016/A
# See <a href = "https://github.com/hugo19941994/CV-Parser" /> Github
#     repository </a>
#

# Check if files and folders exist
if [ -z "$1" ]
then
    exit
else
    curl -XDELETE "http://localhost:9200/concurrente/cv/$1"
    rm ./cv/$1*
    rm ./cvReal/$1*
fi

echo "Deleted $1 CV"
