# https://stackoverflow.com/questions/54713650/create-dictionary-from-a-groupby-o

# ??? what is he asking?

import pandas as pd

data = {'Type' : ['Dog', 'Cat', 'Mouse', 'Dog', 'Cat', 'Cat', 'Mouse', 'Dog'],'Attributes' : ['ID', 'ID', 'ID', 'height','height', 'Weight', 'height', 'Weight'],'Amount':['1','1','3','40','5','6','10','9']}

new_df = pd.DataFrame(data)

#      Type    Attributes Amount
# 0  Animal      ID      1
# 1  Animal     Joe      2
# 2    Bird      ID      3
# 3  Animal     kip     40
# 4    Bird  Pigeon      5
# 5  Animal    Alex      6
# 6  Animal    Jane     10
# 7    Bird     Pie      9

print(new_df)
print("")

grouped = {'Type':{}}

for i in range(0, len(data['Type'])):
    print data['Type'][i]
    animal_type = data['Type'][i]
    animal_Attributes = data['Attributes'][i]
    animal_amount = data['Amount'][i]
    if animal_type not in grouped['Type']:
        grouped['Type'][animal_type] = []
    grouped['Type'][animal_type].append({"Attributes":animal_Attributes, "Amount":animal_amount})

print(grouped)

'''

grouped = {
    'Type': {
        'Animal' : [
            {
                Attributes: ID
                Amount: 1
            }
        ]
    }
}

'''