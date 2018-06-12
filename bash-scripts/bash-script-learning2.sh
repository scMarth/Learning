#!/bin/bash

read -p "Enter a number : " num

# can also use: eq ne le lt ge gt
if ((num == 10)); then
   echo "Your number equals 10"
fi

if ((num > 10)); then
   echo "It is greater than 10"
else
   echo "It is less than ten"
fi

if (( ((num%2)) == 0)); then
   echo "It is even"
fi

if (( ((num>0)) && ((num<11)) )); then
   echo "$num is between 1 and 10"
fi


# if you create a file and it works, then open it in vim
touch sample_file && vim sample_file

# if sample directory doesn't exist, then we want to make it
[ -d sample_dir ] || mkdir sample_dir

# -d check if it exists or not