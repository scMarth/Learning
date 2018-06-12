#!/bin/bash

# regular expressions

read -p "Enter 2 numbers to sum : " num1 num2

sum=$((num1 + num2))

echo "$num1 + $num2 = $sum"

read -sp "Enter the secret code" secret

if [ "$secret" == "password" ]; then
   echo "Enter"
else
   echo "Wrong Password"
fi


