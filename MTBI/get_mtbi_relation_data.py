import requests, sys, re, time
"""Print unique unordered MBTI combinations numbered."""

MBTI_TYPES = [
    'ISTJ','ISFJ','INFJ','INTJ',
    'ISTP','ISFP','INFP','INTP',
    'ESTP','ESFP','ENFP','ENTP',
    'ESTJ','ESFJ','ENFJ','ENTJ',
]

relation_data = []

def main():
    count = 1
    n = len(MBTI_TYPES)
    for i in range(n):
        for j in range(i, n):
            p1 = MBTI_TYPES[i]
            p2 = MBTI_TYPES[j]
            print(f"{count}: {p1}/{p2}")
            count += 1

            url = f"https://256personalities.com/chemistry-guide/{p1}/{p2}"
            response = requests.get(url)
            raw_html = response.text

            article_match = re.search(r'<article\b[^>]*>(.*?)</article>', raw_html, re.DOTALL)

            if article_match:
                article_html = article_match.group(1)

                # Find the first <p>...</p> inside it
                p_match = re.search(r'<p\b[^>]*>(.*?)</p>', article_html, re.DOTALL)

                if p_match:
                    p_text = re.sub(r'<[^>]+>', '', p_match.group(1))  # strip inner tags
                    p_text = p_text.strip()
                    print(p_text)
                    relation_data.append((p1, p2, p_text))
            # be polite to the server and avoid overwhelming it with requests
            time.sleep(1)

    # dump all the data to a csv file
    with open('mtbi_relation_data.csv', 'w', encoding='utf-8') as f:
        f.write("Personality1,Personality2,Relation\n")
        for p1, p2, relation in relation_data:
            f.write(f"{p1},{p2},{relation}\n")



if __name__ == '__main__':
    main()

