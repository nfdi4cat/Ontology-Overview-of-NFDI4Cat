import pandas as pd
import json

onto_list = ['AFO','BFO','EMMO']
for onto_name in onto_list:
    table = pd.read_excel('./Master_Table/Possible_Template_TF_OntoWorldMap_2023-03-28_10-52.xlsx',sheet_name = onto_name)
    
    with open("./GeneralStructure.json") as f: 
        ontodata_dict = json.load(f)
    
    #a = table.Ontology.dropna(how='all')
    
    #for i in range(len(table.Ontology.dropna(how='all'))):
    #    print(table.Ontology[i])
    
    data_table = ["Ontology"]
    data_table.extend(list(table.Ontology.dropna(how='all')))
    
    for superkey in ontodata_dict:
        if superkey == "Comments":
            list_index = data_table.index(superkey)
            ontodata_dict[superkey]= data_table[list_index+1:]
        else:
            for key in ontodata_dict[superkey]:        
                list_index = data_table.index(key)
                ontodata_dict[superkey][key] = data_table[list_index+1]
    
    with open("./json/"+onto_name+".json", "w") as f:
        json.dump(ontodata_dict,f)
        
    
    with open("./md-translator.json") as f:     
        translator_dict = json.load(f)
        
        
    outstring = "## " + onto_name + " - " + ontodata_dict["Ontology"]["Ontology Name"] + "\n\n\n"   
    
    table_string = "|Aspect |Description| \n |:---|:---|\n"
    
    
    for key in translator_dict:
        if key == "Comments":
            outstring = outstring + "## Comments\n"
            outstring = outstring + str(translator_dict[key]) + "\n"
        else:
            outstring = outstring + "## "+ key + "\n"
            outstring = outstring + table_string
            for dict_list in translator_dict[key]:
                outstring = outstring + "| " + str(list(dict_list.values())[0]) + " | "+ str(ontodata_dict[key][list(dict_list.keys())[0]]) + " |\n"
            outstring = outstring + "\n"
            
    with open('./Ontology_Metadata_out/'+ onto_name +'.md', 'w') as f:
        f.write(outstring)