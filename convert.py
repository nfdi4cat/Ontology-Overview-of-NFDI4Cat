import pandas as pd
import json
import os
from tabulate import tabulate

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

####

def load_ontologies_metadata():
    ## Reads in the metadata-json files of each ontology, omitting the 
    #  GeneralStructure and md-translator files as they do not contain metadata.
    #  output: metadata_dict that contains the acronyms of the ontologies as keys
    #          and the respective json-file as dictionary are the values
    json_list = [f for f in os.listdir('./json/') if (f.endswith('.json') and f != "GeneralStructure.json" and f!= "md-translator.json" and f!= "ontology_domains.json")]
    metadata_dict = {}
    for json_name in json_list:
        with open('./json/' + json_name) as file:
            onto_metadata = json.load(file)
            metadata_dict[onto_metadata["Ontology"]["Ontology Acronym"]] = onto_metadata
  
    return metadata_dict        

####
            
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
   
    
    ####
    # List the most appropiate ontologies for each domain of interest by filtering
    # out only the entries without missing.
    md_dict = load_ontologies_metadata()
    key_dom_interest = "Domain of Interest Represented (contained, related: broader/narrower, missing)"

    #list the domains of interest used in the first key of md_dict, assuming 
    #every sheet in the template requests the same domains of interest
    domains_of_interest = list(md_dict[list(md_dict.keys())[0]][key_dom_interest].keys())
    domain_dict = {}

    for domain in domains_of_interest:
        onto_list = []
        for onto_abbrev in md_dict:
            dict_entry = md_dict[onto_abbrev][key_dom_interest][domain]
            if ("contained" in dict_entry) or ("related: narrower" in dict_entry):
                onto_list.append(onto_abbrev) 
        domain_dict[domain] = onto_list
    # domain_dict now contains all domains of interest and the respective ontologies
    # that contain this domain or are at least narrow related to the domain.
    ##

    df = pd.DataFrame.from_dict(domain_dict, orient='index').transpose()    

    with open("./json/ontology_domains.json", "w") as f:
         json.dump(domain_dict,f)

    # add [ and ] to ontology name to get link to md file automatically in md
    df = df.applymap(lambda onto: '[' + onto + ']' if type(onto)==str else None)
    # Format df to markdown
    markdown_table = tabulate(df, headers='keys', tablefmt='pipe')
    # Append markdown to Main_Readme_Update
    with open('./Main_Readme_Update.txt', 'a') as f:
        f.write("\n## The ontologies in this table contain the respective domain of knowledge or are narrower related to them.\n")
        f.write(markdown_table)

   
    
    print('================================================================')
    print('Parts of Updated README.md written in "./Main_Readme_Update.txt"')
    print('Please copy and paste the content into the respective parts of  ')
    print('./README.md to update the linking to the ontology markdown files.')
    print('================================================================')
    
Master_Table = './master_table/MT_OntoWorldMap_2023-06-13.xlsx'

ConvertExcelToMD(Master_Table)

UpdateMainReadme()
