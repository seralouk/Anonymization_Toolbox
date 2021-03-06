import os
import pandas as pd
import numpy as np
import sys
# Define the paths
data_path = '/Users/miplab/Desktop/Anonymization_toolbox/Data/'
functions_path = '/Users/miplab/Desktop/Anonymization_toolbox/Utilities/'
results_path = '/Users/miplab/Desktop/Anonymization_toolbox/Results/'
sys.path.append(functions_path)
sys.path.append(data_path)
from core_functions import load_database, anonymize, similar


# Define the names of the file and its columns
database_filename = "Data2.xlsx"
list_of_column_names = ["Prenom","Nom"]
# first_name_column_header = "Prenom"
# last_name_column_header =  "Nom"


# Define a thershold for the similarity between subjects. E.g If similarity is > threshold for subject A and B then the algorithm will assign the same ID for these 2. Perfect example is the twin case !
threshold = 0.87

if not os.path.exists(results_path):
    os.makedirs(results_path)
os.chdir(data_path)

# Load the dataset
df = load_database(database_filename)

# Anonymize the dataset based on similarity between subject's attributes
data_final, comb = anonymize(df, list_of_column_names, threshold)

# Save 
data_final[['Anonymization','Nom','Prenom']].to_excel(results_path + "Data_July.xlsx", index=False)

# Visualize and check the anonymization
for idx, row in data_final.iterrows():
	print data_final['Anonymization'].loc[idx], comb.loc[idx]