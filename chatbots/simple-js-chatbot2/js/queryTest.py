"""
Try to see if a ODP link can be verified programmatically. So far no success.
"""

import requests, re, codecs

urls = [
    r'https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=zip+code',
    r'https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=zip',
    r'https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=zoning',
    r'https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=hello'
]

with codecs.open('DEBUG.txt', 'w', 'utf-8') as file:
    for url in urls:
        file.write(url + '\n')
        p = requests.get(url)

        no_success_expr = "Your search didn't match any dataset."

        if re.search(no_success_expr, p.text):
            file.write('No results found.\n')
            file.write(p.text)
            file.write('\n')
            print('No results found.')
            # print(p.text)
        else:
            file.write('Results were found.\n')
            print('Results were found.')


