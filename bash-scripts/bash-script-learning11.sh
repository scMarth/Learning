#!/bin/bash

# this doesn't work in git bash for some reason

while read avg rbis hrs; do
   printf "Avg: ${avg}\nRBIs: ${rbis}\nHRs: ${hrs}\n"
done < barry.txt

