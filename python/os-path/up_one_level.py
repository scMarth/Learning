import os, pathlib

workspace = os.path.dirname(__file__)
path = pathlib.Path(os.path.dirname(__file__))
print(path.parent)

print(str(path.parent) + r'\otherDir')