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

    def printReal(self):
        print(self.r)

    def printRealAndImag(self):
        self.printReal()
        self.printImag()

    def setRealAndImag(self, realPart, imagPart):
        self.r = realPart
        self.i = imagPart

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return