#!/bin/bash
#----------------HY-------------
OLDIFS=$IFS

IFS=","

while read product price quantity  #Mis variables o campos a parsear, es el indicador de columna
do
        echo -e "\e[1;33m$product \"
        ========================\e[0m\n\
        Price : \t $price \n\
        Quantity : \t $quantity \n"
done < $1
IFS=$OLDIFS
