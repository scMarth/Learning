from operator import itemgetter 
from itertools import groupby
import fitz
doc = fitz.open("../pdfs/RoadClosureInfo.pdf")     # any supported document type
page = doc[0]

"""
Get all words on page in a list of lists. Each word is represented by:
[x0, y0, x1, y1, word, bno, lno, wno]
The first 4 entries are the word's rectangle coordinates, the last 3 are just
technical info (block number, line number, word number).
"""
words = page.getTextWords()
# print(words)

with open("./extracted.txt", "w") as file:
    for i in range(0, len(doc)):
        page = doc[i]

        for word in words:
            try:
                file.write(str(word[4]) + " ")
            except:
                continue
        file.write("\n\n")