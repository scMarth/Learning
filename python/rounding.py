import decimal

# python by default will round down on a half decimal:
print(0.5555)
print(round(0.5555, 3))

# https://stackoverflow.com/questions/33019698/how-to-properly-round-up-half-float-numbers-in-python

num = 0.5555
dec = decimal.Decimal(num)

# rounded = dec.quantize(decimal.Decimal(0.001), rounding=decimal.ROUND_HALF_UP) # error
# rounded = dec.quantize(decimal.Decimal('0.001'), rounding=decimal.ROUND_HALF_UP) # no error 0.555
# rounded = dec.quantize(decimal.Decimal('0.001'), rounding=decimal.ROUND_UP) # no error 0.556
rounded = dec.quantize(decimal.Decimal('1.111'), rounding=decimal.ROUND_UP) # no error 0.556
print(rounded)

# NOTE: to see why there are errors, see the comment block below

test = decimal.Decimal('1.111')
test2 = decimal.Decimal(1.111)
test3 = decimal.Decimal(str(1.111))

print(test)
print(test2)
print(test3)

print(test == test3) # True

'''
https://stackoverflow.com/questions/588004/is-floating-point-math-broken

This is the case because of how floating point is stored with finite precision, and there are cases
where the a number cannot be exactly represented.
'''

print(0.1 + 0.2 == 0.3) # False
print(0.1 + 0.2) # prints 0.30000000000000004