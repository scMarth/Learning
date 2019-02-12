result1 = [x*2 if x%2 == 0 else x*0 for x in range(0, 10)]
print result1

result2 = []
for x in range(0, 10):
    if x%2 == 0:
        result2.append(x*2)
    else:
        result2.append(x*0)
print result2
