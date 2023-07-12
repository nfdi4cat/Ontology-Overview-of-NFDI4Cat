import pandas as pd
import json
import os
from tabulate import tabulate
import plotly.graph_objects as go


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

    #df = pd.DataFrame.from_dict(domain_dict, orient='index').transpose()    
    
    DomainRadarPlotter_all_ontologies()
    
    #with open("./json/ontology_domains.json", "w") as f:
    #     json.dump(domain_dict,f)

    # add [ and ] to ontology name to get link to md file automatically in md
    #df = df.applymap(lambda onto: '[' + onto + ']' if type(onto)==str else None)
    # Format df to markdown
    #markdown_table = tabulate(df, headers='keys', tablefmt='pipe')
    # Append markdown to Main_Readme_Update
    with open('./Main_Readme_Update.txt', 'a') as f:
        f.write("\n## Map of Ontologies for Catalysis Research Domains .\n")
        f.write("\n The ontologies are classified with regards to their research domain [here](./Radarplots.md).\n")
        f.write("\n [Here](./Radarplots.html) you can find the Radar plot as interactive plot.\n")
        f.write("\n ![Map of Ontologies for Catalysis Research Domains](./Fig2-OntoMap.svg)\n")
                #<img src="./controllers_brief.svg">[Here](./Fig2-OntoMap.svg) you can find the Radar plot as an interactive plot.\n")

        
        #f.write(markdown_table)

   
    
    print('================================================================')
    print('Parts of Updated README.md written in "./Main_Readme_Update.txt"')
    print('Please copy and paste the content into the respective parts of  ')
    print('./README.md to update the linking to the ontology markdown files.')
    print('================================================================')

####


####
def Heatmap_to_Markdown():
    # Read the Excel file
    df = pd.read_excel('MappingHeatmap.xlsx')
    md_dict = load_ontologies_metadata()
    print_list = []
    df = df.fillna('')
    # Iterate through each cell in the DataFrame
    for row in df.index:
        for col in df.columns:
            # Get the current cell value
            cell_value = df.at[row, col]
            if type(cell_value) != str and cell_value != df.at[row,'Unnamed: 0']:
                # Write the column and row names behind the cell value
                new_value = f'[' + str(int(cell_value)) +'](/mapping/'+col+'_'+df.at[row,'Unnamed: 0'] +'.md)'
                df.at[row, col] = new_value
            
            if df.at[row,'Unnamed: 0'] == col:
                df.at[row, col] = md_dict[col]["Ontology Characteristics"]["Class count"]
                
    for col in df.columns:
        df.rename(columns={col: '['+col+']'}, inplace=True)
    
    for row in df.index:
        repl_str = '['+df.at[row,'[Unnamed: 0]']+']'
        df.at[row,'[Unnamed: 0]'] = repl_str
        
    df.rename(columns={'[Unnamed: 0]': ''}, inplace=True)
    
    df.to_markdown('Heatmap_Classes.md', index=False)
    # Save the modified DataFrame to a new Excel file
    #df.to_excel('output_file1.xlsx', index=False)
####

####
def Mappings_to_Markdown():
    file_list = [f for f in os.listdir('./mapping/') if f.endswith('.xlsx')]
    
    for file in file_list:
        df = pd.read_excel('./mapping/'+file)
        del df['Unnamed: 0']
        df.to_markdown('./mapping/' + file.replace('xlsx','md'))
####

####
####
def DomainRadarPlotter_all_ontologies():
    ####
    # List the most appropiate ontologies for each domain of interest by filtering
    # out only the entries without missing.
    md_dict = load_ontologies_metadata()
    key_dom_interest = "Domain of Interest Represented (contained, related: broader/narrower, missing)"

    #list the domains of interest used in the first key of md_dict, assuming 
    #every sheet in the template requests the same domains of interest
    domains_of_interest = list(md_dict[list(md_dict.keys())[0]][key_dom_interest].keys())
    # contained domains
    domain_dict_c = {}
    # contained and narrower related domains
    domain_dict_c_n = {}
    # contained, narrower and broader related domains
    domain_dict_c_n_b = {}

    for domain in domains_of_interest:
        # contained ontologies
        onto_list_c = []
        # contained and narrower related ontologies
        onto_list_c_n = []
        # contained, narrower and broader related ontologies
        onto_list_c_n_b = []
        
        for onto_abbrev in md_dict:
            dict_entry = md_dict[onto_abbrev][key_dom_interest][domain]
            
            if ("contained" in dict_entry):
                onto_list_c.append(onto_abbrev) 
                
            if ("contained" in dict_entry) or ("related: narrower" in dict_entry):
                onto_list_c_n.append(onto_abbrev) 
                
            if ("contained" in dict_entry) or ("related: narrower" in dict_entry) or ("related: broader" in dict_entry):
                onto_list_c_n_b.append(onto_abbrev) 
        
        domain_dict_c[domain] = onto_list_c
        domain_dict_c_n[domain] = onto_list_c_n
        domain_dict_c_n_b[domain] = onto_list_c_n_b
    # domain_dict now contains all domains of interest and the respective ontologies
    # that contain this domain or are at least narrow related to the domain.
    ##
    
    plotlist_c = [len(domain_dict_c[i]) for i in domains_of_interest]
    plotlist_c_n = [len(domain_dict_c_n[i]) for i in domains_of_interest]
    plotlist_c_n_b = [len(domain_dict_c_n_b[i]) for i in domains_of_interest]
    
    
    # Store domain dictionaries
    df_c = pd.DataFrame.from_dict(domain_dict_c, orient='index').transpose()    
    df_c_n = pd.DataFrame.from_dict(domain_dict_c_n, orient='index').transpose()    
    df_c_n_b = pd.DataFrame.from_dict(domain_dict_c_n_b, orient='index').transpose()    

    # add [ and ] to ontology name to get link to md file automatically in md
    df_c = df_c.applymap(lambda onto: '[' + onto + ']' if type(onto)==str else None)
    df_c_n = df_c_n.applymap(lambda onto: '[' + onto + ']' if type(onto)==str else None)
    df_c_n_b = df_c_n_b.applymap(lambda onto: '[' + onto + ']' if type(onto)==str else None)
    
    markdown_table_c = tabulate(df_c, headers='keys', tablefmt='pipe')
    markdown_table_c_n = tabulate(df_c_n, headers='keys', tablefmt='pipe')
    markdown_table_c_n_b = tabulate(df_c_n_b, headers='keys', tablefmt='pipe')
    
    # Append markdown to Main_Readme_Update
    with open('./Radarplots.md', 'w') as f:
        f.write("\n## The ontologies in this table contain the respective domain of knowledge.\n")
        f.write(markdown_table_c)
        f.write("\n## The ontologies in this table contain the respective domain of knowledge or are narrower related to them.\n")
        f.write(markdown_table_c_n)
        f.write("\n## The ontologies in this table contain the respective domain of knowledge or are narrower related or are broader related to them.\n")
        f.write(markdown_table_c_n_b)
    
    ## DELETING TOP-LEVEL-ONTOLOGIES
    del domains_of_interest[-1]
    del plotlist_c_n_b[-1]
    del plotlist_c_n[-1]
    del plotlist_c[-1]
    #
    
    # Extending the list by the first entries to close the radar plots:
    plotlist_c.extend([plotlist_c[0]])
    plotlist_c_n.extend([plotlist_c_n[0]])
    plotlist_c_n_b.extend([plotlist_c_n_b[0]])
    domains_of_interest.extend([domains_of_interest[0]])
    
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
          r= plotlist_c_n_b,
          theta=domains_of_interest,
          fill='toself',
          #line_close=True,
          name='contained, related: narrower, and related: broader'
    ))
      
    fig.add_trace(go.Scatterpolar(
          r=plotlist_c_n,
          theta=domains_of_interest,
          fill='toself',
          name='contained and related: narrower'
    ))

    fig.add_trace(go.Scatterpolar(
          r=plotlist_c,
          theta=domains_of_interest,
          fill='toself',
          name='contained'
    ))
      
    #fig.add_trace(go.Scatterpolar(
    #      r=[4, 3, 2.5, 1, 2],
    #      theta=domains_of_interest,
    #      fill='toself',
    #      name='Product B'
    #))
    
    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, max(plotlist_c_n_b)]
        )),
      showlegend=True
    )
    
    fig.write_html("Radarplot.html")
    fig.write_image("Radarplot.svg")
    
####

def DomainRadarPlotter():
    ####
    # List the most appropiate ontologies for each domain of interest by filtering
    # out only the entries without missing.
    md_dict = load_ontologies_metadata()
    key_dom_interest = "Domain of Interest Represented (contained, related: broader/narrower, missing)"

    #list the domains of interest used in the first key of md_dict, assuming 
    #every sheet in the template requests the same domains of interest
    domains_of_interest = list(md_dict[list(md_dict.keys())[0]][key_dom_interest].keys())
    # contained domains
    domain_dict_c = {}
    # contained and narrower related domains
    domain_dict_c_n = {}
    # contained, narrower and broader related domains
    domain_dict_c_n_b = {}

    for domain in domains_of_interest:
        # contained ontologies
        onto_list_c = []
        # contained and narrower related ontologies
        onto_list_c_n = []
        # contained, narrower and broader related ontologies
        onto_list_c_n_b = []
        
        for onto_abbrev in md_dict:
            dict_entry = md_dict[onto_abbrev][key_dom_interest][domain]
            
            if ("contained" in dict_entry):
                onto_list_c.append(onto_abbrev) 
                
            if ("contained" in dict_entry) or ("related: narrower" in dict_entry):
                onto_list_c_n.append(onto_abbrev) 
                
            if ("contained" in dict_entry) or ("related: narrower" in dict_entry) or ("related: broader" in dict_entry):
                onto_list_c_n_b.append(onto_abbrev) 
        
        domain_dict_c[domain] = onto_list_c
        domain_dict_c_n[domain] = onto_list_c_n
        domain_dict_c_n_b[domain] = onto_list_c_n_b
    # domain_dict now contains all domains of interest and the respective ontologies
    # that contain this domain or are at least narrow related to the domain.
    ##
    
    plotlist_c = [len(domain_dict_c[i]) for i in domains_of_interest]
    plotlist_c_n = [len(domain_dict_c_n[i]) for i in domains_of_interest]
    plotlist_c_n_b = [len(domain_dict_c_n_b[i]) for i in domains_of_interest]
    
    # Extending the list by the first entries to close the radar plots:
    
    del domains_of_interest[-1]
    del plotlist_c_n_b[-1]
    del plotlist_c_n[-1]
    del plotlist_c[-1]
    plotlist_c.extend([plotlist_c[0]])
    plotlist_c_n.extend([plotlist_c_n[0]])
    plotlist_c_n_b.extend([plotlist_c_n_b[0]])
    domains_of_interest.extend([domains_of_interest[0]])
    
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
          r= plotlist_c_n_b,
          theta=domains_of_interest,
          fill='toself',
          #line_close=True,
          name='contained, related: narrower, and related: broader'
    ))
      
    fig.add_trace(go.Scatterpolar(
          r=plotlist_c_n,
          theta=domains_of_interest,
          fill='toself',
          name='contained and related: narrower'
    ))

    fig.add_trace(go.Scatterpolar(
          r=plotlist_c,
          theta=domains_of_interest,
          fill='toself',
          name='contained'
    ))
      
    #fig.add_trace(go.Scatterpolar(
    #      r=[4, 3, 2.5, 1, 2],
    #      theta=domains_of_interest,
    #      fill='toself',
    #      name='Product B'
    #))
    
    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, max(plotlist_c_n_b)]
        )),
      showlegend=True
    )
    
    fig.write_html("SpiderplotX.html")
    fig.write_image("SpiderplotX.svg")
    
####


####
def run():    
    Master_Table = './master_table/MT_OntoWorldMap_2023-06-13.xlsx'
    ConvertExcelToMD(Master_Table)
    UpdateMainReadme()
