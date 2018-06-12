#!/bin/bash

# comment

echo "Hello World"

# don't put a space before/after '='' for declarations and variable definitions
myName="Derek"

# the shell treats all variables as if they are strings

# declare a constant
declare -r NUM1=5

num2=4

num3=$((NUM1+num2))
num4=$((NUM1-num2))
num5=$((NUM1*num2))
num6=$((NUM1/num2))

echo "5 + 4 = $num3"
echo "5 - 4 = $num4"
echo "5 * 4 = $num5"
echo "5 / 4 = $num6"

echo $((5**2))
echo $(( 5%4 ))

rand=5

let rand+=4

echo "$rand"

echo "rand++ = $(( rand++ ))"
echo "++rand = $(( ++rand ))"
echo "rand-- = $(( rand-- ))"
echo "--rand = $(( --rand ))"


num7=1.2
num8=3.4

# can call python commands, but requires python to be installed.
num9=$(python -c "print $num7+$num8")
echo $num9

echo "Hello again"

cat<< END
This text
prints on
many lines
END


getDate(){
   date
   return
}

getDate

# global variable available to everything else in your script
name="Derek"

demLocal(){
   local name="Paul"
   return
}

demLocal
echo "$name"

getSum(){
   local num3=$1
   local num4=$2

   local sum=$((num3 + num4))
   echo $sum
}

num1=5
num2=6

sum=$(getSum num1 num2)
echo "The sum is $sum"

read -p "What is your name? " name
echo "Hello $name"

read -p "How old are you? " age
if [ $age -eq 16 ]
then
   echo "You can drive"
elif [ $age -eq 15 ]
then
   echo "You can drive next year"
else
   echo "You can't drive"
fi

