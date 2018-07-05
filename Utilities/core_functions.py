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


def anonymize(df, column_names, threshold):

	if all(isinstance(item, str) for item in column_names):
		df[column_names[0]] = df[column_names[0]].fillna('?')
		comb = df[column_names[1]] + df[column_names[0]]
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
				if sim > threshold:
					df['Anonymization'].loc[idx+1] = df['Anonymization'].loc[idx]
	else:
		raise ValueError('The column_names must be a string e.g. last_name_column_header =  "Nom")')
	return df, comb


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


