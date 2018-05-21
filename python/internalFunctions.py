def function():
    #variable = 0
    def partA():
        # this doesn't work
        # variable += 1
        print("Hello")
    def partB():
        print("Hello 2")

    partA()
    partB()
    print(variable)


function()

# doesn't exist in this scope
partA()
