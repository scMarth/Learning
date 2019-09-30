"""
Try to see if a ODP link can be verified programmatically. So far no success.
"""

import requests, re, codecs

urls = [
    'https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=zip+code',
    'https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=zip',
    'https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=zoning',
    'https://cityofsalinas.opendatasoft.com/explore/?refine.language=en&sort=modified&q=hello'
]

count = 0
for url in urls:
    count += 1

    with codecs.open(str(count) + '.txt', 'w', 'utf-8') as html_file:

    # file.write(url + '\n')
        p = requests.get(url)

        no_success_expr = "Your search didn't match any dataset."

        if re.search(no_success_expr, p.text):
            html_file.write(p.text)
            print('No results found.')
            # print(p.text)
        else:
            # html_file.write('Results were found.\n')
            print('Results were found.')


