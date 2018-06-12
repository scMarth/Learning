#!/bin/bash

# regular expressions

read -p "Validate Date : " date

pat="^[0-9]{8}$"

if [[ $date =~ $pat ]]; then
   echo "$date is valid"
else
   echo "$date not valid"
fi

