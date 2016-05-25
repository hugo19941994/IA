#!/bin/bash
# Este script permite indexar una carpeta entera que contenga 
# ficheros json en un index de elasticSearch especificado
#
# Author: Jorge de Castro
# Version: 07/03/2016/A
# See <a href = "https://bitbucket.org/jdecastroc/restcvparser" /> Bitbucket
#     repository </a>
#


COUNTER=1

for file in cv/*.json; do
DATA=$(less $file)
curl -XPUT 'http://hugofs.com:9200/concurrente/cv/'$COUNTER -d "$DATA" -vn
sleep 4
COUNTER=$(($COUNTER+1))
done
echo "finished"
