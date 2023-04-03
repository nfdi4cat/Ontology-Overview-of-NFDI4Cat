import pandas as pd
import json
import os

def ConvertExcelToMD(PathToExcel):
    
    onto_list = pd.ExcelFile(PathToExcel).sheet_names
    
    # remove Sheet names with non-ontology names:
    ignore_sheets = ['Template mit Beispiel', 'List_zu_betrachtende_Ontologien']
    remove_NonOntologies = lambda x: [x.remove(i) for i in ignore_sheets]
    remove_NonOntologies(onto_list)
    
    for onto_name in onto_list:
        table = pd.read_excel(PathToExcel,sheet_name = onto_name)
        
        with open("./json/GeneralStructure.json") as f: 
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
            
        
        with open("./json/md-translator.json") as f:     
            translator_dict = json.load(f)
            
            
        outstring = "## " + onto_name + " - " + ontodata_dict["Ontology"]["Ontology Name"] + "\n\n\n"   
        
        table_string = "|Aspect |Description| \n |:---|:---|\n"
        
        for key in translator_dict:
            if key == "Comments":
                outstring += "## Comments\n"
                for i in ontodata_dict[key]:
                    outstring += str(i) + "\n"
            else:
                outstring += "## "+ key + "\n"
                outstring += table_string
                for dict_list in translator_dict[key]:
                    outstring += "| " + str(list(dict_list.values())[0]) + " | "+ str(ontodata_dict[key][list(dict_list.keys())[0]]) + " |\n"
                outstring += "\n"
                
        with open('./ontology_metadata/'+ onto_name +'.md', 'w') as f:
            f.write(outstring)
            
def UpdateMainReadme(): 
    path = './ontology_metadata/'
    markdown_list = [s for s in os.listdir(path) if s.endswith('.md')]
    print_list = "| Link to Markdown | Ontology Name |\n |:---:|:---|\n"
    
    for i in markdown_list:
        ontology_name = i.replace('.md','')
        with open('./json/' + ontology_name + '.json') as dictFile:
            onto_dict = json.load(dictFile)
        
        print_list += '| [' + ontology_name + '] |' + onto_dict["Ontology"]["Ontology Name"] +' |\n'
    
    ###
    print_list += '\n'
    for i in markdown_list:
        print_list += '[' + i.replace('.md','') + ']: ./ontology_metadata/' + i + '\n' 
    
    with open('./Main_Readme_Update.txt', 'w') as f:
        f.write(print_list)

Master_Table = './master_table/Possible_Template_TF_OntoWorldMap_2023-03-28_10-52.xlsx'

ConvertExcelToMD(Master_Table)

UpdateMainReadme()
