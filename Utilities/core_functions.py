import pandas as pd
import numpy as np
import os
from difflib import SequenceMatcher


def load_database(filename):
	if type(filename) == str:
		dataframe = pd.read_excel(filename)
		df = dataframe.copy()
	else:
		raise ValueError('The filename must be a string e.g. filename = "name"')
	return df


def anonymize(df, column1, column2):
	if type(column1) and type(column2) == str:

		df[column2] = df[column2].fillna('?')
		comb = df[column1] + df[column2]
		comb = comb.str.replace(r"\(.*\)","")
		comb = comb.str.replace(' ',"")
		comb = comb.str.replace('/',"")
		comb = comb.str.replace('-',"")
		df['Anonymization'] = (comb).astype('category').cat.codes

		# encode to 00001 format
		for idx, row in df.iterrows():
			df['Anonymization'].loc[idx] = '{:04n}'.format(df['Anonymization'].loc[idx] + 1)
		for idx, row in df.iterrows():
			if idx <  df.shape[0]-1:
				sim = similar(comb[idx], comb[idx + 1])
				if sim > 0.87:
					df['Anonymization'].loc[idx+1] = df['Anonymization'].loc[idx]
	else:
		raise ValueError('The column_names must be a string e.g. last_name_column_header =  "Nom")')
	return df, comb


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


