from owlready2 import *
from tabulate import tabulate
import itertools
import pandas as pd
import os
import seaborn as sns
import json
import urllib 
import pandas as pd
import time

import sys
sys.setrecursionlimit(100000)


#"C:\Program Files\Java\jdk-11.0.2\bin\javaw.exe"

def ontology_classes_loader(ontology):
    # Create sets of class labels for each ontology
    # using label depending on ontology!
    
    # iris
    try:
        onto1_iris = list([cls.iri for cls in ontology.classes()])
    except:
        print("IRIs of ontology " + ontology.name + " not (well) defined and could not be read!")
        onto1_iris=[]
        return None
    
    iri_dict ={}
    
    for iri in onto1_iris:
       
        try:
            if type(ontology.search_one(iri = iri).label.first()) == locstr: 
                # some ontologies use locstrings to account for different languages
                class_label = ontology.search_one(iri = iri).label.first().split()[0]
            else:
                class_label = ontology.search_one(iri = iri).label.first()
        except:
            class_label = None
        
        try: 
            if type(ontology.search_one(iri = iri).prefLabel.first()) == locstr: 
                # some ontologies use locstrings to account for different languages
                class_prefLabel = ontology.search_one(iri = iri).prefLabel.first().split()[0]
            else:
                class_prefLabel = ontology.search_one(iri = iri).prefLabel.first()
        except:
            class_prefLabel = None
        
        try:
            if type(ontology.search_one(iri = iri).altLabel.first()) == locstr:
                # some ontologies use locstrings to account for different languages
                class_altLabel = ontology.search_one(iri = iri).altLabel.first().split()[0]
            else:
                class_altLabel = ontology.search_one(iri = iri).altLabel.first()
        except:
            class_altLabel = None
            
        try:
            class_name = ontology.search_one(iri = iri).name
        except:
            class_name = None
        
        ##
        try:
            class_def = class_definition_readin(ontology.search_one(iri = iri))
        except:
            class_def = None
        
        ##
        iri_dict[str(iri)] = {"label": class_label,
                                   "prefLabel": class_prefLabel,
                                   "altLabel": class_altLabel,
                                   "name": class_name,
                                   "definition":class_def}
    return iri_dict


####

def class_definition_readin(ontology_class):
    try: 
        if ontology_class.definition:
            definition_string = ontology_class.definition
        else: #causing Error to break the try
            sys.exit(1)
    except:
        try:
            if ontology_class.hasDefinition:
                definition_string = ontology_class.hasDefinition
            else:
                sys.exit(1)
        except:
            try:
                if getattr(ontology_class,'IAO_0000115'):
                    definition_string = getattr(ontology_class,'IAO_0000115')
                else:
                    sys.exit(1)                           
            except:
                try:
                    if definition_string == []:
                        definition_string = ontology_class.comment
                    else:
                        sys.exit(1)        
                except:
                    definition_string = []
            
    return definition_string

####
#imported by convert.py

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

def get_ontology_URLs():
    ## Reads in the URLs of the ontology files and returns returns them as 
    #  dictionary with {ontology name : URL}
    md_dict = load_ontologies_metadata()
    URL_dict = {}
    for key in md_dict:
        URL = md_dict[key]["References"]["Persistent URI of Ontology File (or perma link to latest Version)"]        
        URL_dict[key] = URL
    
    return URL_dict    
####

####
def ttl_to_owl(url):
    ## Conversion of ttl-ontology to owl-ontology with ROBOT
    #  Input: URL of ontology file
    #  Output: File name of ontology downloaded into subdirectory ./ontologies/ as str
    ##
    filename = url.rpartition('/')[-1] # gets last bit of URL after / to obtain "filename.ttl"
    onto_name = filename.split('.')[0]   
    ##
    # Finds ontology abbreviation based on URL of ontology in ontology URL dictionary
    onto_URLs = get_ontology_URLs()
    onto_abbrev = list(onto_URLs.keys())[list(onto_URLs.values()).index(url)]
    ##
    
    ontology_output_filename = onto_abbrev + '.owl'
    
    # if isfile == true, owl file is already contained in ./ontologies/ and no reload or 
    # conversion of ttl-ontology from web is necessary. So only if no owl file is 
    # contained, the merge and convert is executed.
    if not os.path.isfile('./ontologies/' + ontology_output_filename): 
        onto_txt = urllib.request.urlopen(url)
        onto_txt = onto_txt.read()#readlines()
    
        with open('./ontologies/'+onto_name+'.ttl', 'wb') as onto_file:
            onto_file.write(onto_txt)
        
        #os.system(".\\robot\\robot convert --input .\\ontologies\\{} --format owl --output .\\ontologies\\{}".format(filename, ontology_output_filename))
        os.system(".\\robot\\robot merge --input .\\ontologies\\{} --output .\\ontologies\\{}".format(filename,filename))
        os.system(".\\robot\\robot convert --input .\\ontologies\\{} --format owl --output .\\ontologies\\{}".format(filename, ontology_output_filename))
        
    return ontology_output_filename
####

####
def rdf_to_owl(url):
    ## Conversion of ttl-ontology to owl-ontology with ROBOT
    #  Input: URL of ontology file
    #  Output: File name of ontology downloaded into subdirectory ./ontologies/ as str
    ##
    filename = url.rpartition('/')[-1] # gets last bit of URL after / to obtain "filename.ttl"
    onto_name = filename.split('.')[0]   
    ##
    # Finds ontology abbreviation based on URL of ontology in ontology URL dictionary
    onto_URLs = get_ontology_URLs()
    onto_abbrev = list(onto_URLs.keys())[list(onto_URLs.values()).index(url)]
    ##
    
    ontology_output_filename = onto_abbrev + '.owl'
    
    # if isfile == true, owl file is already contained in ./ontologies/ and no reload or 
    # conversion of ttl-ontology from web is necessary. So only if no owl file is 
    # contained, the merge and convert is executed.
    if not os.path.isfile('./ontologies/' + ontology_output_filename): 
        onto_txt = urllib.request.urlopen(url)
        onto_txt = onto_txt.read()#readlines()
    
        with open('./ontologies/'+onto_name+'.rdf', 'wb') as onto_file:
            onto_file.write(onto_txt)
        
        #os.system(".\\robot\\robot convert --input .\\ontologies\\{} --format owl --output .\\ontologies\\{}".format(filename, ontology_output_filename))
        #os.system(".\\robot\\robot merge --input .\\ontologies\\{} --output .\\ontologies\\{}".format(filename,filename))
        os.system(".\\robot\\robot convert --input .\\ontologies\\{} --format owl --output .\\ontologies\\{}".format(onto_name+'.rdf', ontology_output_filename))
        
    return ontology_output_filename
####


####
def load_ontology_from_name(onto_name):
    ## Tries to load in the ontology by accessing the URL to an owl-file
    #  
    onto_URLs = get_ontology_URLs()
    URL = onto_URLs[onto_name]
    onto_loaded = None
    
    if onto_name == 'CHEMINF': 
        #contains deprecated classes and object properties, thus needs to be cleaned
        # and loaded manually, else owlready2 will crash
        try: 
            print("Loading Ontology: {} from local path ./ontologies/".format(onto_name))
            onto_loaded = get_ontology("./ontologies/"+onto_name+'.owl').load()
            print("Successfully loaded Ontology: {}".format(onto_name))
        except:
            print("Need to place file here: ./ontologies/{}.owl".format(onto_name))
            onto_loaded = None
            pass        
    elif onto_name == 'M3': 
        #contains deprecated classes and object properties, thus needs to be cleaned
        # and loaded manually, else owlready2 will crash
        try: 
            print("Loading Ontology: {} from local path ./ontologies/".format(onto_name))
            onto_loaded = get_ontology("./ontologies/M3.owl").load()
            print("Successfully loaded Ontology: {}".format(onto_name))
        except:
            print("Need to place file here: ./ontologies/{}.owl".format(onto_name))
            onto_loaded = None
            pass     
    
    elif URL.endswith('.owl'):
        try: 
            print("Loading Ontology: {}".format(onto_name))
            onto_loaded = get_ontology(URL).load()
            print("Successfully loaded Ontology: {}".format(onto_name))
        except:
            print("Something went wrong, ontology name: {}".format(onto_name))
            try:
                try: 
                    print("Trying to load Ontology: {} from local path ./ontologies/".format(onto_name))
                    onto_loaded = get_ontology("./ontologies/"+onto_name+'.owl').load()
                    print("Successfully loaded Ontology: {}".format(onto_name))
                except:
                    print("Something went wrong, you need to place the owl-file here: ./ontologies/{}.owl".format(onto_name))
                    onto_loaded = None
                    pass
            except:
                pass
            
    elif URL.endswith('.ttl'):
        print("Ontology {} is provided as ttl, searching for owl verison of ontology in subdir ./ontologies/ and converting ontology from ttl to owl if not found".format(URL))
        ontology_in_owl = ttl_to_owl(URL)
        
        onto_loaded = get_ontology('./ontologies/' + ontology_in_owl).load()

    else:
        #TODO: try to load from ./ontologies/ if there is a manual added version of the OWL, such as for OntoCAPE.
        print("Unknown file-ending for ontology {}, please check the URL!\n    URL: {}\n".format(onto_name, URL))
        try:
            """
            print("Trying to load ontology {} from local path ./ontologies/".format(onto_name))
            onto_loaded = get_ontology("./ontologies/"+onto_name+'.owl').load()
            print("Successfully loaded Ontology: {}".format(onto_name))
            """
            ontology_in_owl = rdf_to_owl(URL)
            onto_loaded = get_ontology('./ontologies/' + ontology_in_owl).load()
        except:
            print("Something went wrong, ontology name: ".format(onto_name))
            onto_loaded = None
            pass
    
    return onto_loaded
####

####
def onto_format_validation(onto_name, URL):
    ## prints compatibility of provided links with owlready2
    #  
    if URL.endswith('.owl'):
        #print("OWL: {}, {}".format(onto_name, URL))
        return True
    elif URL.endswith('.ttl'):
        #print("TTL: {}, {} -> will need formatting".format(onto_name, URL))
        return True
    else:
        print("Non-Conform: {}, {} -> not compatible".format(onto_name, URL))
        return False
    
####
# search for same values in nested dicts
# with input dictionary and value to be searched, it outputs the 
# path to the searched value for each dictionary
def search_value_in_nested_dict(dictionary, value, keys=None, path=None):
    if keys is None:
        keys = []
    if path is None:
        path = []

    for key, val in dictionary.items():
        # Update the current key path
        current_path = path + [key]  

        if str(val).lower() == str(value).lower():
            keys.append(tuple(current_path))

        # recursive call of the function such that the lowest part of the nested dict is queried
        if isinstance(val, dict): 
            search_value_in_nested_dict(val, value, keys, current_path)
    
    result_dict = {}
    for key_path in keys:
        current_dict = result_dict
        for key in key_path[:-1]:
            current_dict.setdefault(key, {})
            current_dict = current_dict[key]
        current_dict[key_path[-1]] = value
        
    return result_dict

####


####

def class_description_loader():
    onto_URLs = get_ontology_URLs()
    ontoNameList_output = list(onto_URLs.keys())
       
    ontoNameList_output.remove("OntoCAPE")
   # ontoNameList_output.remove("EMMO")
    
    iri_dictionary = {}    
    
    for ontologyname in ontoNameList_output:
        ontology = None
        print(ontologyname)
        ontology = load_ontology_from_name(ontologyname)
        
        if ontology != None:
            iri_dictionary[ontologyname] = ontology_classes_loader(ontology)
        else:
            print(ontologyname + " was empty!")
    
        with open('iriDictionary.json', 'w') as fp:
            json.dump(iri_dictionary, fp)
    
    return iri_dictionary
####

#TODO reshape for iriDictionary.json search 
def store_similarities_from_json(onto_combination, match_list, iriDict_onto, export_str="xlsx"):
    # onto_combination = tuple of ontology names
    # match_list = Nested list of dictionaries, where each list entry contains 
    # a dictionary with a key for each ontology contained in onto_combination.
    # The values of these keys contain themselves information on mapped classes 
    # in form of IRI:{label:<label>, prefLabel:<prefLabel>, altLabel:<altLabel>, name:<name>}
    #
    # export_str = specifier if the output should be as XLSX or JSON file
    # Output: Dataframe or json with first two columns containing IRI and 
    # {label, prefLabel, altLabel, name} of each mapped class within the first ontology.
    # The other two columns contain the same information (IRI and labeling of 
    # classes) for the second ontology.
    
    # Initialize lists to store the data
    onto1_data1 = []
    onto1_data2 = []
    
    onto2_data1 = []
    onto2_data2 = []
    
    def_list = []
    
    """
    #load second ontology
    onto2 = load_ontology_from_name(onto_combination[1])
    
    # load iriDictionary
    with open("./iriDictionary.json") as f: 
        iri_dictionary = json.load(f)
    """
    
    # iterate through match_list
    for entry in match_list:
        if type(entry[0]) == list:
            onto1_entry1 = list(entry[0][0].get(onto_combination[0]).keys())[0]
            onto1_entry2 = list(entry[0][0].get(onto_combination[0]).values())[0]
        else: 
            onto1_entry1 = list(entry[0].get(onto_combination[0]).keys())[0]
            onto1_entry2 = list(entry[0].get(onto_combination[0]).values())[0]
      
        if type(entry[0]) == list:
            onto2_entry1 = list(entry[0][1].get(onto_combination[1]).keys())[0]
            onto2_entry2 = list(entry[0][1].get(onto_combination[1]).values())[0]
        else:
            onto2_entry1 = list(entry[1].get(onto_combination[1]).keys())[0]
            onto2_entry2 = list(entry[1].get(onto_combination[1]).values())[0]
    
        onto1_data1.append(onto1_entry1)
        onto1_data2.append(onto1_entry2)
        
        onto2_data1.append(onto2_entry1)
        onto2_data2.append(onto2_entry2)
        
        class_def = iriDict_onto[onto2_entry1]["definition"]
        #class_def = class_definition_readin(onto2.search_one(iri = onto2_entry1))
        def_list.append(class_def)
    # Create DataFrame from the data
    df = pd.DataFrame({onto_combination[0]+'_IRI': onto1_data1, onto_combination[0]+'_DESC':onto1_data2, onto_combination[1]+'_IRI': onto2_data1, onto_combination[1]+'_DESC':onto2_data2,onto_combination[1]+'_DEF':def_list})
    
    if export_str.lower() == "xlsx":
        df.to_excel("./mapping/"+onto_combination[0]+"_"+onto_combination[1]+".xlsx")
    
    elif export_str.lower() == "json":
        
        df.to_json("./mapping/"+onto_combination[0]+"_"+onto_combination[1]+".json")
    else:
        print("Error: No export Style chosen for Mapping")
    return df

####


####

def store_similarities(onto_combination, match_list,export_str="xlsx"):
    # onto_combination = tuple of ontology names
    # match_list = Nested list of dictionaries, where each list entry contains 
    # a dictionary with a key for each ontology contained in onto_combination.
    # The values of these keys contain themselves information on mapped classes 
    # in form of IRI:{label:<label>, prefLabel:<prefLabel>, altLabel:<altLabel>, name:<name>}
    # Output: Dataframe with first two columns containing IRI and 
    # {label, prefLabel, altLabel, name} of each mapped class within the first ontology.
    # The other two columns contain the same information (IRI and labeling of 
    # classes) for the second ontology.
    
    # Initialize lists to store the data
    onto1_data1 = []
    onto1_data2 = []
    
    onto2_data1 = []
    onto2_data2 = []
    
    def_list = []
    
    #load second ontology
    onto2 = load_ontology_from_name(onto_combination[1])
    
    # iterate through match_list
    for entry in match_list:
        if type(entry[0]) == list:
            onto1_entry1 = list(entry[0][0].get(onto_combination[0]).keys())[0]
            onto1_entry2 = list(entry[0][0].get(onto_combination[0]).values())[0]
        else: 
            onto1_entry1 = list(entry[0].get(onto_combination[0]).keys())[0]
            onto1_entry2 = list(entry[0].get(onto_combination[0]).values())[0]
      
        if type(entry[0]) == list:
            onto2_entry1 = list(entry[0][1].get(onto_combination[1]).keys())[0]
            onto2_entry2 = list(entry[0][1].get(onto_combination[1]).values())[0]
        else:
            onto2_entry1 = list(entry[1].get(onto_combination[1]).keys())[0]
            onto2_entry2 = list(entry[1].get(onto_combination[1]).values())[0]
    
        onto1_data1.append(onto1_entry1)
        onto1_data2.append(onto1_entry2)
        
        onto2_data1.append(onto2_entry1)
        onto2_data2.append(onto2_entry2)
        
        class_def = class_definition_readin(onto2.search_one(iri = onto2_entry1))
        def_list.append(class_def)
    # Create DataFrame from the data
    df = pd.DataFrame({onto_combination[0]+'_IRI': onto1_data1, onto_combination[0]+'_DESC':onto1_data2, onto_combination[1]+'_IRI': onto2_data1, onto_combination[1]+'_DESC':onto2_data2,onto_combination[1]+'_DEF':def_list})
    
    if export_str == "xlsx":
        df.to_excel("./mapping/"+onto_combination[0]+"_"+onto_combination[1]+".xlsx")
    
    elif export_str == "json":
        
        df.to_json("./mapping/"+onto_combination[0]+"_"+onto_combination[1]+".json")
    else:
        print("Error: No export Style chosen for Mapping")
    return df

####

def Ontology_Mapping():
    # Generates the Mapping Heatmap.xlsx, that gets mappings for each combination 
    # of ontologies. This is done by comparing each set of classes of the 
    # combination of ontologies against each other by searching for same iris.
    # Then, all classes that were not found by same iri, the labels, 
    # preferred labels, alternate labels and names of the classes of the first 
    # ontology are searched for in the labels, preferred labels, alternate 
    # labels and names of the second ontology.
    # For each combination of ontologies, the function store_similarities() is
    # called to store the mapping as excel-file in the subdirectory ./mapping/
    
    onto_URLs = get_ontology_URLs()
    ontoNameList = list(onto_URLs.keys())
    ontoNameList_output = list(onto_URLs.keys())
    
    #[ontoNameList_output.remove(key) for key in ontoNameList if not onto_format_validation(key,onto_URLs[key])]
    
    ontoNameList_output.remove("OntoCAPE")
    #ontoNameList_output.remove("EMMO")
    
    onto_combinations = list(itertools.combinations(ontoNameList_output, 2))
    df_numbers = pd.DataFrame(index = ontoNameList_output, columns = ontoNameList_output)
    
    #TODO: substitute with class_description_loader()
    with open("./iriDictionary.json") as f: 
        iri_dictionary = json.load(f)
    
    
    #onto_combinations = [('AFO', 'BAO')]
    #TODO: transfer to function
    for comb in onto_combinations:
        onto_dict1 = iri_dictionary[comb[0]]
        onto_dict2 = iri_dictionary[comb[1]]
        
        iri_list_dict_1 = list(onto_dict1.keys())
        
        match_list = []
        
        # search for same iris 
        for iri in iri_list_dict_1:
            class_match = None
            try:
                class_match = onto_dict2[iri]
            except:
                class_match = None   
            
            if class_match:
                match_list.append([{comb[0]:{iri:{'iri':iri}}},{comb[1]:{iri:{'iri':iri}}}])
         
        # delete already found iris from dict
        iri_list_dict_1_cleaned = iri_list_dict_1
        [iri_list_dict_1_cleaned.remove(list(entry[0][comb[0]].keys())[0]) for entry in match_list]
        
        label_list1 = [onto_dict1[iri]["label"] for iri in iri_list_dict_1_cleaned]
        prefLabel_list1 = [onto_dict1[iri]["prefLabel"] for iri in iri_list_dict_1_cleaned]
        altLabel_list1 = [onto_dict1[iri]["altLabel"] for iri in iri_list_dict_1_cleaned]
        name_list1 = [onto_dict1[iri]["name"] for iri in iri_list_dict_1_cleaned]
    
        #search for same preflabels, labels, altlabels, names
        for i in range(len(label_list1)):
            string_list = [label_list1[i], prefLabel_list1[i], altLabel_list1[i], name_list1[i]]
            append_dict = []
            for value in string_list:
                if value != None:
                    value_dict = search_value_in_nested_dict(onto_dict2,value)
                    if value_dict:        
                        if label_list1[i] != None: #try to insert label of first ontology
                            append_dict.append([{comb[0]:{iri_list_dict_1_cleaned[i]:onto_dict1[iri_list_dict_1_cleaned[i]]}}, {comb[1]:value_dict}])
                        elif prefLabel_list1[i] != None: #try to insert prefLabel of first ontology
                            append_dict.append([{comb[0]:{iri_list_dict_1_cleaned[i]:onto_dict1[iri_list_dict_1_cleaned[i]]}}, {comb[1]:value_dict}]) 
                        elif altLabel_list1[i] != None: #try to insert altLabel of first ontology
                            append_dict.append([{comb[0]:{iri_list_dict_1_cleaned[i]:onto_dict1[iri_list_dict_1_cleaned[i]]}}, {comb[1]:value_dict}])
                        elif name_list1[i] != None: #try to insert name of first ontology
                            append_dict.append([{comb[0]:{iri_list_dict_1_cleaned[i]:onto_dict1[iri_list_dict_1_cleaned[i]]}}, {comb[1]:value_dict}])
                            
                        else: # iri has no label, thus, no label is inserted but the value of the string list
                            append_dict.append([{comb[0]:{iri_list_dict_1_cleaned[i]:{value}}}, {comb[1]:value_dict}])
           
            if append_dict:
                match_list.append(append_dict)
    
        store_similarities(comb,match_list)
        
        df_numbers[comb[0]][comb[1]] = len(match_list)
    
    #print(df_numbers)
    df_numbers.to_excel("MappingHeatmap.xlsx")
    
    return df_numbers
####

####
def run():
    #class_description_loader()
    df = Ontology_Mapping()
####

def Similarity_Search_from_List(input_list,list_name, export_str="xlsx"):
    # Uses list of strings as input to output matching classes from ontology 
    # collection.
    onto_URLs = get_ontology_URLs()
    ontoNameList = list(onto_URLs.keys())
    ontoNameList_output = list(onto_URLs.keys())
    
    #[ontoNameList_output.remove(key) for key in ontoNameList if not onto_format_validation(key,onto_URLs[key])]
    
    ontoNameList_output.remove("OntoCAPE")
    ontoNameList_output.remove("M3")
    
    #onto_combinations = list(itertools.combinations(ontoNameList_output, 2))
    df_numbers = pd.DataFrame(index = [list_name], columns = ontoNameList_output)

    
    with open("./iriDictionary.json") as f: 
        iri_dictionary = json.load(f)
    
    for ontology in ontoNameList_output:
        onto_dict1 = iri_dictionary[ontology]
        
        comb = (list_name, ontology)
        
        match_list = []
       
        #search for same preflabels, labels, altlabels, names
      
        for value in input_list:
            append_dict = []  
            value_dict = search_value_in_nested_dict(onto_dict1,value)
            if value_dict:
                append_dict.append([{comb[0]:{'no IRI':{value}}}, {comb[1]:value_dict}])                        
       
            if append_dict:
                match_list.append(append_dict)
        
        store_similarities(comb,match_list,export_str)
        
        df_numbers[comb[1]][comb[0]] = len(match_list)
    
    #print(df_numbers)
    if export_str == "xlsx":
        df_numbers.to_excel("MappingHeatmap_"+list_name+".xlsx")
    elif export_str == "json":
        df_numbers.to_json("MappingHeatmap_"+list_name+".json")
    else:
        print("Error: No export Style chosen for Mapping")
    return df_numbers
        

####
def Similarity_Search_from_List_dict(input_list,list_name, export_str="xlsx"):
    # Uses list of strings as input to output matching classes from ontology 
    # collection.
   
    """
    onto_URLs = get_ontology_URLs()
    ontoNameList = list(onto_URLs.keys())
    ontoNameList_output = list(onto_URLs.keys())
    
    #[ontoNameList_output.remove(key) for key in ontoNameList if not onto_format_validation(key,onto_URLs[key])]
    
    ontoNameList_output.remove("OntoCAPE")
    ontoNameList_output.remove("CAO")
    """
    #onto_combinations = list(itertools.combinations(ontoNameList_output, 2))

    
    with open("./iriDictionary.json") as f: 
        iri_dictionary = json.load(f)

    ontoNameList_output = list(iri_dictionary.keys())
    
    df_numbers = pd.DataFrame(index = [list_name], columns = ontoNameList_output)
    
    for ontology in ontoNameList_output:
        onto_dict1 = iri_dictionary[ontology]
        
        comb = (list_name, ontology)
        
        match_list = []
       
        #search for same preflabels, labels, altlabels, names
      
        for value in input_list:
            append_dict = []  
            value_dict = search_value_in_nested_dict(onto_dict1,value)
            if value_dict:
                append_dict.append([{comb[0]:{'no IRI':{value}}}, {comb[1]:value_dict}])                        
       
            if append_dict:
                match_list.append(append_dict)
        
        store_similarities_from_json(comb,match_list,onto_dict1,export_str)
        
        df_numbers[comb[1]][comb[0]] = len(match_list)
    
    #print(df_numbers)
    if export_str == "xlsx":
        df_numbers.to_excel("MappingHeatmap_"+list_name+".xlsx")
    elif export_str == "json":
        df_numbers.to_json("MappingHeatmap_"+list_name+".json")
    else:
        print("Error: No export Style chosen for Mapping")
    return df_numbers
        
####
def run_similarity_from_vocabulary(): 
    test_ontology = get_ontology('./ontologies/voc4cat.owl').load()
    ind_list = list(test_ontology.individuals())
    #prefList = [[str(i.prefLabel[0]),i.altLabel] for i in ind_list]
    prefList = [str(i.prefLabel[0]) for i in ind_list]
    Similarity_Search_from_List(prefList,"input_list")
####



#TODO
## Similarity_Search_from_List -> store_similarities -> rewrite this function 
#  to not search ontologies but iridict json instead

"""
## py Script for simple execution
import similarities_search_only
concept_list = ["catalyst","reaction","chemical reaction"]
concept_list_name = "Concept_List_Arbitrary_Name"
output_format = "json"
similarities_search_only.Similarity_Search_from_List(concept_list, concept_list_name, output_format)

"""    

"""
t = time.time()
concept_list = ["catalyst","reaction","chemical reaction"]
concept_list_name = "Concept_List_Arbitrary_Name"
output_format = "json"
Similarity_Search_from_List(concept_list, concept_list_name, output_format)
elapsed = time.time()-t
print(elapsed)



t = time.time()
concept_list = [
    "Homogeneous catalysis",
    "Heterogeneous catalysis",
    "Enzyme catalysis",
    "Biocatalysis",
    "Photocatalysis",
    "Electrocatalysis",
    "Nanocatalysis",
    "Chiral catalysis",
    "Surface catalysis",
    "Industrial catalysis",
    "Organocatalysis",
    "Catalyst",
    "Catalyst poisoning",
    "Catalyst regeneration",
    "Catalyst characterization",
    "Computational catalysis",
    "reaction",
    "chemical reaction",
    "Catalyst stability",
    "Catalyst selectivity"
]
concept_list_name = "Concept_List_Arbitrary_Name"
output_format = "json"
Similarity_Search_from_List(concept_list, concept_list_name, output_format)
elapsed = time.time()-t
print(elapsed)
"""

"""
with open("PhotoCatVocabulary.txt") as file:
    lines = [line.rstrip("\n") for line in file]

t = time.time()

df = pd.read_excel("Combined Cleaned Vocabulary.xlsx", sheet_name = "Concepts", skiprows=1)
column_data = list(df["Preferred Label*"])
data_frame_numbers = Similarity_Search_from_List(column_data,"Combined Cleaned Vocabulary")

elapsed = time.time() - t

print(elapsed)
"""

"""
df = pd.read_excel("CombinedConcepts_condensed_09-2022_Test_AB.xlsx", sheet_name = "Concepts")

column_data = list(df["Preferred Label*"])

numbers = Similarity_Search_from_List(column_data,"CombinedConcepts_condensed_09-2022_")


with open('combinedVocabulary_nextcloud.txt', 'r') as file:
    # Read the contents of the file
    contents = file.read()

    # Split the contents into individual elements to create a list
    my_list = contents.split(',')
    
Similarity_Search_from_List(my_list,"concept_collection_")
"""

#https://github.com/pysemtec/semantic-python-overview
#https://arrow.apache.org/docs/python/index.html

####
#print out ontologies without proper URLs -> 
#TODO: find those links and fix it in MasterTable
#onto_URLs = get_ontology_URLs()
#for i in onto_URLs:
#    onto_format_validation(i, onto_URLs[i])   
####




    
        