import re

s='@VirginAmerica it was amazing, and arrived an hour early.'
t='heyyyyy@VirginAmerica , am I dreaming?'
m='heyyyyy @VirginAmerica , am I dreaming?'
u=''
f='@United...'
h='@United@VirginAmerica'

for text in [s, t, m, u, f, h]:
    print(re.findall(r'@(\w+)', text))