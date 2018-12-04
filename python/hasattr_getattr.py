class Reactangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


rect = Reactangle(4,6)

print(str(rect.area()))
print("")

print(hasattr(rect, 'height'))
print(hasattr(rect, 'width'))
print(hasattr(rect, 'area'))
print("")

print(str(getattr(rect, 'height')))
print(str(getattr(rect, 'width')))
print(str(getattr(rect, 'area')))
