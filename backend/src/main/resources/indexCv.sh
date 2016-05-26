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
if [ ! -e ./counter.txt ]
then
    touch counter.txt
fi
if [ ! -d ./cv ]
then
    mkdir cv
fi
if [ ! -d ./cvReal ]
then
    mkdir cvReal
fi
if [ ! -d ./upload ]
then
    mkdir upload
fi

# Get current index
COUNTER=$(cat counter.txt)

if [ -z "$COUNTER" ]
then
    COUNTER=1
fi

for file in ./upload/*  # Check uploaded files
do
    if [ -e $file ]  # Check if file exists
    then
        # Get filename and extension
        filename=$(basename "$file")
        extension="${filename##*.}"

        # Parse file
        (cd ../../../../parser; python main.py ../backend/src/main/resources/upload/$filename) & wait

        # Move parsed JSON
        mv /home/hfs/CV-Parser/parser/out/section/0.json "./cv/$COUNTER.json"

        # Get content of JSON
        DATA=$(less ./cv/$COUNTER.json)

        # JSON to elastic
        curl -XPUT 'http://hugofs.com:9200/concurrente/cv/'$COUNTER -d "$DATA" -vn

        # Change filename to index
        mv $file ./cvReal/$COUNTER.$extension

        # Increment counter
        COUNTER=$((++COUNTER))
        echo $((COUNTER)) > counter.txt
    fi
done

echo "finished"
