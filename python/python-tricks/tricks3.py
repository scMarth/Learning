# https://www.youtube.com/watch?v=_c6Mxvmav9M

# Adding 2 lists

a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=a+b
print(c)
print("")

# ----------------------------------------------------------------------

# Calendar

import calendar
print(calendar.month(2017,1))
print("")

# ----------------------------------------------------------------------

# Swap

a=123
b=456
a,b=b,a
print(a)
print(b)
print("")

# ----------------------------------------------------------------------

# List

a="Hello World"
a=list(a)
print(a)
print("")

# ----------------------------------------------------------------------

# Join

msg=['well ','done']
msg=''.join(msg)
print(msg)
print("")

# ----------------------------------------------------------------------

# Date Time

import datetime
date=datetime.datetime.now()
date=date.strftime("%d-%m-%y %I:%M:%S %p")
print(date)
print("")

# ----------------------------------------------------------------------

# Random

import random
a='abcdefghijklmnopqrstuvwxyz'
print(random.choice(a))
print("")

# ----------------------------------------------------------------------

# Color

# import os
# os.system('color A')
# input('Hello World')
# print("")

# ----------------------------------------------------------------------

# Compress

import zlib
a='hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohello'
b=zlib.compress(a)
print(b)
print("")

a=zlib.decompress(b)
print(a)
print("")

# ----------------------------------------------------------------------

# Message Box

import ctypes
ctypes.windll.user32.MessageBoxA(0,'This is great','message',0)

# ----------------------------------------------------------------------
