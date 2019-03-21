import numpy as np

# create numpy array by passing a list
a = np.array([2,3,4])
print(a)
print("")

# create numpy array by range
a = np.arange(1,12,2)
print(a)
print("")

# linear spacing from 1 to 12 and specify a number of 6 elements
# creates a floating point array
a = np.linspace(1,12,6)
print(a)
print("")

# reshape to 2 dimentional array
# 3 rows of 2 elements each
a = a.reshape(3,2)
print(a)
print("")

# prints number of elements of array, regardless of shape
print(a.size)
print("")

# prints shape of array
print(a.shape)
print("")

# print datatype
print(a.dtype) # float64, default for floating point values in numpy
print("")

# print how many bytes each elements takes up
print(a.itemsize)
print("")

b = np.array([(1.5, 2, 3), (4,5,6)])
print(b)
print("")

# applies comparison to each element in array
print(a < 4)
print("")

# empty array full of zeros
a = np.zeros((3,4))
print(a)
print("")

a = np.ones((3,4))
print(a)
print("")

a = np.array([2,3,4], dtype=np.int16)
print(a)
print("")

# random number from 0 to 1
a = np.random.random((2,3))
print(a)
print("")

# sometimes, numpy will default using scientific notation, so suppress will stop scientific notation
# precision = 2 is two decimal places
np.set_printoptions(precision=2, suppress=True)
print(a)
print("")

# random int from 0 to 10, 5 elements
a = np.random.randint(0,10,5)
print(a)
print("")

# sum
print(a.sum())

# min
print(a.min())

# max
print(a.max())

# mean (average)
print(a.mean())

# variance
print(a.var())

# standard deviation
print(a.std())

a = np.random.randint(0,10,6)
a = a.reshape(3,2)
print(a)
print("")

# sum of only 1 axis
print(a.sum(axis=1))

# sum of only 1 axis
print(a.sum(axis=0))
print("")

# import csv
data = np.loadtxt(r".\data.csv", dtype=np.uint8, delimiter=",", skiprows=1)
print(data)
print("")

a = np.arange(10)
print(a)
print("")

# shuffle (in-place shuffle, no need for a = ... just like sort function)
np.random.shuffle(a)
print(a)
print("")

# gives random choice from a
print(np.random.choice(a))
print(np.random.choice(a))
print(np.random.choice(a))
print(np.random.choice(a))
print(np.random.choice(a))
print(np.random.choice(a))
print("")

# 5 to 10 range, 2 items
print(np.random.random_integers(5,10,2))