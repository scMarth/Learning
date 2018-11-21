def method1():
    return "some string"

def method2(method_to_run):
    result = method_to_run()
    print(result)

def method3():
    return "something else"

method2(method1)
method2(method3)