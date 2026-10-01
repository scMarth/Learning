import csv, os, sys

csv_path = os.path.join(os.path.dirname(__file__), 'mtbi_relation_data.csv')

if not os.path.exists(csv_path):
    print(f"CSV not found: {csv_path}")
    sys.exit()

MBTI_TYPES = [
    'ISTJ','ISFJ','INFJ','INTJ',
    'ISTP','ISFP','INFP','INTP',
    'ESTP','ESFP','ENFP','ENTP',
    'ESTJ','ESFJ','ENFJ','ENTJ',
]


# read the us distribution of MBTI types from a CSV file
# source: https://www.16personalities.com/country-profiles/united-states
MTBI_PREVALENCE = {}
with open(os.path.join(os.path.dirname(__file__), 'united_states_personality_distributions.csv'), newline='', encoding='utf-8') as fh:
    reader = csv.reader(fh)
    next(reader, None)  # Skip header
    for row in reader:
        MTBI_PREVALENCE[row[0]] = float(row[2].rstrip('%'))  # Store combined percentage

print("MBTI Prevalence in the US:")
for mtbi, prevalence in MTBI_PREVALENCE.items():
    print(f"  {mtbi}: {prevalence:.2f}%")

ratings = {}

with open(csv_path, newline='', encoding='utf-8') as fh:
    reader = csv.reader(fh)
    headers = next(reader, None)
    # if headers:
    #     # print('Headers:', headers)
    for i, row in enumerate(reader, start=1):
        # print(f"{i}: {row}")

        # print(row[0], row[1], row[2])

        if row[0] not in ratings:
            ratings[row[0]] = {}
        if row[1] not in ratings:
            ratings[row[1]] = {}


        if row[0] != row[1]:
            ratings[row[0]][row[1]] = row[2]
            ratings[row[1]][row[0]] = row[2]
        else:
            ratings[row[0]][row[1]] = row[2]



mtbi_data = {}


RATING_WEIGHTS = {
    'Perfect': 5,
    'Good': 4,
    'OK': 3,
    'Not Bad': 2,
    'Disaster': 1,
}

for mtbi in MBTI_TYPES:
    rating_counts = {}
    ranking = 0
    weighted_ranking = 0.0

    for mtbi2 in MBTI_TYPES:
        connection_rating = ratings[mtbi][mtbi2]
        rating_counts[connection_rating] = rating_counts.get(connection_rating, 0) + 1

        w = RATING_WEIGHTS[connection_rating]
        ranking += w
        weighted_ranking += w * MTBI_PREVALENCE[mtbi2]

    sanity_check_sum = sum(rating_counts.values())

    mtbi_data[mtbi] = {
        'rating_counts': rating_counts,
        'sanity_check_sum': sanity_check_sum,
        'ranking': ranking,
        'weighted_ranking': weighted_ranking/100.0,
    }

print('')

for mtbi in sorted(mtbi_data, key=lambda k: mtbi_data[k]['weighted_ranking'], reverse=True):
     print(f"{mtbi}: ranking: {mtbi_data[mtbi]['ranking']}, rating_counts: {mtbi_data[mtbi]['rating_counts']}, sanity_check_sum: {mtbi_data[mtbi]['sanity_check_sum']}, weighted_ranking: {mtbi_data[mtbi]['weighted_ranking']}")