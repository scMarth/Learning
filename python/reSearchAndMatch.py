import re

def matchResult(expr, inputStr):
    if (re.match(expr, inputStr)):
        return True
    return False
    
def searchResult(expr, inputStr):
    if (re.search(expr, inputStr)):
        return True
    return False

print("'hello' contains 'ello' using re.match: " + str(matchResult("ello", "hello")))
print("'hello' contains 'ello' using re.search: " + str(searchResult("ello", "hello")))


print("'hello' contains 'ello' using re.match: " + str(matchResult("ello", "world the fox hello")))
print("'hello' contains 'ello' using re.search: " + str(searchResult("ello", "world the fox hello")))

print("'hello' contains 'ello' using re.match: " + str(matchResult("\\bworld", "world the fox hello")))
print("'hello' contains 'ello' using re.search: " + str(searchResult("\\bworld", "world the fox hello")))

print("'hello' contains 'ello' using re.match: " + str(matchResult("\\bhello", "world the fox hello")))
print("'hello' contains 'ello' using re.search: " + str(searchResult("\\bhello", "world the fox hello")))

print("'hello' contains 'ello' using re.match: " + str(matchResult("\s", "world the fox hello")))
print("'hello' contains 'ello' using re.search: " + str(searchResult("\s", "world the fox hello")))

print(searchResult("\s", "the quick brown fox")) # True
print(searchResult("\bfox", "the quick brown fox")) # False
print(searchResult("\\bfo\\b", "the quick brown fox")) # False
print(searchResult("\\bfox\\b", "the quick brown fox")) # True

testString = "\\b" + "fox" + "\\b"
print(searchResult(testString, "the quick brown fox"))
