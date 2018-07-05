import pandas as pd
import numpy as np


dataframe = pd.read_excel("Data.xlsx")
df = dataframe.copy()

names = df['Prenom']
names = names.fillna('?')
# DOB = df['DOB']
# DOB = DOB.fillna('0000-00-00')
# DOB = DOB.astype(str).str.extract('(....-..-..)', expand=True)
# DOB = DOB.fillna('0000-00-00')
# DOB = DOB.values.reshape(DOB.shape[0],)
# DOB = pd.DataFrame(DOB)


# comb = pd.concat([df['Nom'], names, DOB],axis=1)
# comb.columns = ['Nom', 'Prenom', 'Dates']

# comb = comb['Nom'] + comb['Prenom'] + comb['Dates']
comb = df['Nom'] + names


# drop out parenthesis content
comb = comb.str.replace(r"\(.*\)","")
comb = comb.str.replace(' ',"")
comb = comb.str.replace('/',"")
comb = comb.str.replace('-',"")

df['Anonymization'] = (comb).astype('category').cat.codes

# encode to 00001 format
for idx, row in df.iterrows():
	df['Anonymization'].loc[idx] = '{:04n}'.format(df['Anonymization'].loc[idx] + 1)


from difflib import SequenceMatcher
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


for idx, row in df.iterrows():
	if idx < 785:
		sim = similar(comb[idx], comb[idx + 1])
		if sim >= 0.8:
			df['Anonymization'].loc[idx+1] = df['Anonymization'].loc[idx]



# Save the new database in xlsx format
# df.to_excel("Data2.xlsx", index=False)


for idx, row in df.iterrows():
	print df['Anonymization'].loc[idx], comb.loc[idx]

