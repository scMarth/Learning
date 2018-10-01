def function(string="Initial Value"):
    print(string)

function("override")


def manyArgs(arg1, arg2, arg3, arg4):
    print("arg1:")
    print(arg1)
    print("")

    print("arg2:")
    print(arg2)
    print("")

    print("arg3:")
    print(arg3)
    print("")

    print("arg4:")
    print(arg4)
    print("")

manyArgs("foo", 1, 2, range(1,3))
