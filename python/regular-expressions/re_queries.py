import requests, re, codecs

url = 'https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices'
base_url = 'https://giswebservices.ci.salinas.ca.us'

p = requests.get(url)

# print(p.text)

hrefs = re.findall(r'<li><a\s+href=\"[^\"]+\">.*</a>.*</li>', p.text)

count = 0
for href in hrefs:
    count += 1
    match_obj = re.search(r'href=\"([^\"]+)\">PublishedServices\/(.*)</a>', href)
    # print(match_obj.group(0)) # whole string
    # print(match_obj.group(1)) # parenthesized group 1
    # print(match_obj.group(2)) # parenthesized group 2

    full_url = base_url + match_obj.group(1)

    print("%-3d %-122s %-51s"%(count, full_url, match_obj.group(2)))