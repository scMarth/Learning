mylist = [x*x for x in range(3)]
for i in mylist:
   print(i)

# can call again
for i in mylist:
   print(i)

print("")
print("Using Generators:")
print("")

mygenerator = (x*x for x in range(3))
print(mygenerator)
for i in mygenerator:
   print(i)


# these don't work
for i in mygenerator:
   print(i)

print(mygenerator)

# using yield
print("Using yield")

def createGenerator():
   mylist = range(3)
   for i in mylist:
      yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
for i in mygenerator:
   print(i)


'''

https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.

The generator is considered empty once the function runs, but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy an "if/else" anymore.

'''

