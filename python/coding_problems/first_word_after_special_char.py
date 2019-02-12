# https://stackoverflow.com/questions/54525128/getting-first-word-after-a-special-character-in-a-string-in-python#54525258

import re

s='@VirginAmerica it was amazing, and arrived an hour early.'
t='heyyyyy@VirginAmerica , am I dreaming?'
m='heyyyyy @VirginAmerica , am I dreaming?'
u=''
f='@United...'
h='@United@VirginAmerica'

for text in [s, t, m, u, f, h]:
    print(re.findall(r'@(\w+)', text))