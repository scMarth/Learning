import re

'''
In Python 3, this will give the error for bad escape \p at position 2.
'''
# if re.search(".*\\polygon$", "hello\polygon"):
#     print('Detected')

"""
This still gives the same error as in above:
"""
# if re.search(".*\polygon$", "hello\polygon"):
#     print('Detected')

"""
This still gives the same error
"""
# if re.search(r".*\polygon$", "hello\polygon"):
#     print('Detected')

"""
This works
"""
if re.search(r".*\\polygon$", "hello\polygon"):
    print('Detected')

