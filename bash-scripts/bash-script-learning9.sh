#!/bin/bash

# parameter expansions and strings

rand_str="A random string"

echo "String Length : ${#rand_str}"
echo "${rand_str:2}"
echo "${rand_str:2:7}"
echo "${rand_str#*A }" #everything after "A "

