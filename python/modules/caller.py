'''

from module import * # this imports everything, EXCEPT private variables

echoString("The quick brown fox")

'''

###############################################################################


import module # this imports everything, including private variables


module.echoString("The quick brown fox")
module.__privatelyEchoString("This shouldn't work")
