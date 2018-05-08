def ls(inputStr, directory=b"/", columns=None, size=False):
    print(inputStr)
    print(directory)
    print(columns)
    print(size)

    if directory[-1] != b"/":
        directory += b"/"

        # List indexes of -x mean the xth item from the end of the list, so n[-1] means the last item in the list  n
    
    print(directory) 

ls("string", "path/morePath")