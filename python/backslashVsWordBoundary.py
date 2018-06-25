import re

def searchResult(expr, inputStr):
    if (re.search(expr, inputStr)):
        return True
    return False

print(searchResult("\s", "the quick brown fox")) # True
print(searchResult("\bfox", "the quick brown fox")) # False
print(searchResult("\\bfox", "the quick brown fox")) # True


print("")
print("The quick brown\b")
