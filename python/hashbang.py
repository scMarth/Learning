#!/usr/bin/env python

import sys, socket

print("Hello {0}, you are using Python version {1}".format(socket.gethostname, sys.version))

'''

In Linux, you can do:

    $ chmod +x hashbang.py
    $ ./hashbang.py
    Hello

    $

use:
    #!/usr/bin/env python3

for Python 3

otherweise, you can call it like:

    $ python hashbang.py
    $ python3 hashbang.py

'''