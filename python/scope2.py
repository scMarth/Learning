def helloFunction():
    def amIPrivate():
        print("Hello")
    amIPrivate()

helloFunction()
# amIPrivate() # would throw an error because of scope