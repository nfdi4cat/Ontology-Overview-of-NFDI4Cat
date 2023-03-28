import pandas as pd
import json

table = pd.read_excel('./Master_Table/Possible_Template_TF_OntoWorldMap_2023-03-28_10-52.xlsx',sheet_name ='AFO')

with open("./GeneralStructure.json") as f: 
    trans_dict = json.load(f)

#a = table.Ontology.dropna(how='all')

#for i in range(len(table.Ontology.dropna(how='all'))):
#    print(table.Ontology[i])

data_table = ["Ontology"]
data_table.extend(list(table.Ontology.dropna(how='all')))

for superkey in trans_dict:
    for key in trans_dict[superkey]:
        print(key)
