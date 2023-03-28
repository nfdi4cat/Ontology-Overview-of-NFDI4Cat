import pandas as pd
import json

onto_list = ['AFO','BFO','EMMO']
for onto_name in onto_list:
    table = pd.read_excel('./Master_Table/Possible_Template_TF_OntoWorldMap_2023-03-28_10-52.xlsx',sheet_name = onto_name)
    
    with open("./GeneralStructure.json") as f: 
        trans_dict = json.load(f)
    
    #a = table.Ontology.dropna(how='all')
    
    #for i in range(len(table.Ontology.dropna(how='all'))):
    #    print(table.Ontology[i])
    
    data_table = ["Ontology"]
    data_table.extend(list(table.Ontology.dropna(how='all')))
    
    for superkey in trans_dict:
        if superkey == "Comments":
            list_index = data_table.index(superkey)
            trans_dict[superkey]= data_table[list_index+1]
        else:
            for key in trans_dict[superkey]:        
                list_index = data_table.index(key)
                trans_dict[superkey][key] = data_table[list_index+1]
    
    with open("./json/"+onto_name+".json", "w") as f:
        json.dump(trans_dict,f)