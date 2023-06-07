import os, sys, json

workspace = os.path.dirname(os.path.abspath(__file__))

# Path to the Chrome Bookmarks.bak file
chrome_bookmarks_path = workspace + r'\Bookmarks.bak'

# Path to the output HTML file
firefox_bookmarks_path = workspace + r'\bookmarks.html'

# Change the following line to the path of your Bookmarks.bak file
with open(chrome_bookmarks_path, 'r', encoding='utf-8') as f:
    chrome_bookmarks_data = json.load(f)

def convert_bookmarks(node):
    if 'children' in node:
        output = '<DT><H3>' + node['name'] + '</H3>\n<DL>\n'
        for child in node['children']:
            output += convert_bookmarks(child)
        output += '</DL>\n'
    else:
        output = '<DT><A HREF="' + node['url'] + '">' + node['name'] + '</A>\n'
    return output

# Change the following line to the desired output file path and name
output_file = open(firefox_bookmarks_path, 'w', encoding='utf-8')
output_file.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<HTML>\n<HEAD>\n<TITLE>Bookmarks</TITLE>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n<DT><H1>Bookmarks</H1>\n<DL><p>\n')
for child in chrome_bookmarks_data['roots']['bookmark_bar']['children']:
    output_file.write(convert_bookmarks(child))
output_file.write('</DL><p>\n</HTML>')
output_file.close()
