class Real:
    def __init__(self, realpart):
        self.r = realpart

    def printReal(self):
        print(self.r)

class Complex(Real): # real is the base class
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def printImag(self):
        print(self.i)

    def printRealAndImag(self):
        self.printReal()
        self.printImag()

    def setRealAndImag(self, realPart, imagPart):
        self.r = realPart
        self.i = imagPart


a = Real(3.0)
a.printReal() # because this is a class, () is actually passing 1 variable, namely the 'self'

print("")

x = Complex(3.0, -4.5)
x.printReal()
x.printImag()

print("")
x.printRealAndImag()

x.setRealAndImag(6, 9)
print("")
x.printRealAndImag()

x.__init__("hello", "world")
print("")
x.printRealAndImag()
