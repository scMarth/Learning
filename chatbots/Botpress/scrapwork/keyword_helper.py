import json, sys

# each element in this list is a list, which contain keywords that have equivalent links
equiv_keywords = []
data = None

with open('keywordData.json') as json_file:
    data = json.load(json_file)
    for key in data:
        if 'links' in data[key]:
            if len(equiv_keywords) == 0:
                equiv_keywords.append([key])
            else:
                match_index = None
                match_found = False

                # check for a match
                for i in range(len(equiv_keywords)):
                    match = True
                    key_list = equiv_keywords[i]

                    test_key = key_list[0]
                    test_key_links = data[test_key]['links']
                
                    for url_type in data[key]['links']:
                        if url_type not in test_key_links:
                            match = False
                        else:
                            for url in data[key]['links'][url_type]:
                                if url not in test_key_links[url_type]:
                                    match = False
                    
                    if match:
                        equiv_keywords[i].append(key)
                        match_found = True
                        break
                    
                if not match_found:
                    equiv_keywords.append([key])

with open('out.txt', 'w') as file:
    for key_list in equiv_keywords:
        for i in range(0, len(key_list) - 1):
            file.write(key_list[i] + ', ')
        file.write(key_list[-1] + '\n')

        urls = data[key_list[0]]['links']
        for url_type in urls:
            file.write('\t' + url_type + '\n')
            for url in urls[url_type]:
                file.write('\t\t' + url + '\n')
        file.write('\n')