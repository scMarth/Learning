import json, sys

# each element in this list is a list, which contain keywords that have equivalent links
equiv_keywords = []

with open('keywordData.json') as json_file:
    data = json.load(json_file)
    for key in data:
        print('KEY = {}'.format(key))
        if 'links' in data[key]:
            if len(equiv_keywords) == 0:
                equiv_keywords.append([key])
                print(equiv_keywords)
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

print('\n\n')
for key_list in equiv_keywords:
    print(key_list)


                    
                    