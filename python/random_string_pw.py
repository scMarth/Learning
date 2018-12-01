import string
import random


letters = [random.choice(string.ascii_letters) for _ in range(5)]
digits = [random.choice(string.digits) for _ in range(2)]
special = [random.choice("!@#$%&?") for _ in range(1)]
password = letters+digits+special
random.shuffle(password)
password = "".join(password)

print(password)