#!/bin/bash

# define separators

OIFS="$IFS"
IFS=","

read -p "Enter 2 numbers to add separated by a comma" num1 num2

num1=${num1//[[:blank:]]/}
num2=${num2//[[:blank:]]/}

sum=$((num1+num2))

echo "$num1 + $num2 = $sum"

IFS="$OIFS"

# parameter expansion
name="Derezzk"
echo "${name}'s toy"

samp_string="The dog climbed the tree"
echo "${samp_string//dog/cat}"

# You can assign a default value if it doesn't exist with :-

# This uses the default if it doesn't exist and assigns the value
# to the variable
echo "I am ${name:=Derek}"