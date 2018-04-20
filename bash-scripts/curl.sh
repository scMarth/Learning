#!/bin/bash

LINECOUNT=0
FIRSTLINE=1
LASTLINE=10

# listOfQueries.txt is simply a list of queries (urls), one per line, without quotes
cat listOfQueries.txt | while read line ; do
   LINECOUNT=$(($LINECOUNT + 1))

   # Only process lines that are between FIRSTLINE and LASTLINE (inclusive)
   if [ $FIRSTLINE -gt $LINECOUNT ] || [ $LINECOUNT -gt $LASTLINE ]
   then
      continue
   fi

   VARI=0
   for i in $line; do
      VARI=$(($VARI + 1))

      # The first token in the line will be the URL
      if [ $VARI -eq 1 ]
      then
         VARURL=$i
      fi
   done

   echo "LINECOUNT: $LINECOUNT"
   echo "VARURL: $VARURL"

   # Remove newline character at end, otherwise the call to curl will fail
   VARURL=${VARURL%$'\r'}

   CURL='curl'
   CURLARGS="-f -s -S -k"

   echo "Curling..."
   $CURL $CURLARGS $VARURL > $LINECOUNT.json
   echo "Exit Status: $?"

   # If a json directory doesn't exist, create it
   if [ ! -d "json" ]; then
      mkdir "json"
   fi

   mv $LINECOUNT.json json
   echo ""

done