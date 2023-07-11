from owlready2 import *
from tabulate import tabulate
import itertools
import pandas as pd
import os
import seaborn as sns
import json
import urllib 
import pandas as pd
import convert
import time

import sys
sys.setrecursionlimit(100000)


def ontology_classes_loader(ontology):
    # Create sets of class labels for each ontology
    # using label depending on ontology!
    
    # iris
    try:
        onto1_iris = list([cls.iri for cls in ontology.classes()])
    except:
        print("IRIs of ontology " + onto_name + " not (well) defined and could not be read!")
        onto1_iris=[]
        return None
    
    iri_dict ={}
    
    for iri in onto1_iris:
       
        try:
            class_label = onto1.search_one(iri = iri).label.first()
        except:
            class_label = None
        
        try: 
            class_prefLabel = onto1.search_one(iri = iri).prefLabel.first()
        except:
            class_prefLabel = None
        
        try:
            class_altLabel = onto1.search_one(iri = iri).altLabel.first()
        except:
            class_altLabel = None
            
        try:
            class_name = onto1.search_one(iri = iri).name
        except:
            class_name = None
        
        
        iri_dict[str(iri)] = {"label": class_label,
                                   "prefLabel": class_prefLabel,
                                   "altLabel": class_altLabel,
                                   "name": class_name,
                                   }
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
                if getattr(b,'IAO_0000115'):
                    definition_string = getattr(b,'IAO_0000115')
                else:
                    sys.exit(1)                           
            except:
                try:
                    if ontology_class.comment:
                        definition_string = ontology_class.comment
                    else:
                        sys.exit(1)        
                except:
                    definition_string = []
            
    return definition_string

####
def get_ontology_URLs():
    ## Reads in the URLs of the ontology files and returns returns them as 
    #  dictionary with {ontology name : URL}
    md_dict = convert.load_ontologies_metadata()
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
    ontology_output_filename = onto_name + '.owl'
    
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
def load_ontology_from_name(onto_name):
    ## Tries to load in the ontology by accessing the URL to an owl-file
    #  
    onto_URLs = get_ontology_URLs()
    URL = onto_URLs[onto_name]
    
    if URL.endswith('.owl'):
        try: 
            print("Loading Ontology: {}".format(onto_name))
            onto_loaded = get_ontology(URL).load()
            print("Successfully loaded Ontology: {}".format(onto_name))
        except:
            print("Something went wrong, ontology name: ".format(onto_name))
            onto_loaded = None
            pass
        
    elif URL.endswith('.ttl'):
        print("Ontology {} is provided as ttl, searching for owl verison of ontology in subdir ./ontologies/ and converting ontology from ttl to owl if not found".format(URL))
        ontology_in_owl = ttl_to_owl(URL)
        
        onto_loaded = get_ontology('./ontologies./' + ontology_in_owl).load()

    else:
        #TODO: try to load from ./ontologies/ if there is a manual added version of the OWL, such as for OntoCAPE.
        print("Unknown file-ending for ontology {}, please check the URL!\n    URL: {}\n".format(onto_name, URL))
              #searching for ontology owl-file in subdirectory ./ontologies/".format(onto_name, URL))
        #try:
        #    onto_loaded = get_ontology('./ontologies/' + onto_name + '.owl').load()
        #   print("Ontology-file found and loaded.")
        #except:
        #    print("... failed")
        onto_loaded = None   
    
    
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
    ontoNameList = list(onto_URLs.keys())
    ontoNameList_output = list(onto_URLs.keys())
    
    [ontoNameList_output.remove(key) for key in ontoNameList if not onto_format_validation(key,onto_URLs[key])]
    
    ontoNameList_output.remove("CHEMINF")
    ontoNameList_output.remove("EMMO")
    
    onto_combinations = list(itertools.combinations(ontoNameList_output, 2))
    df_numbers = pd.DataFrame(index = ontoNameList_output, columns = ontoNameList_output)
    
    iri_dictionary = {}
    
    for ontologyname in ontoNameList_output:
        ontology = None
        ontology = load_ontology_from_name(ontologyname)
        iri_dictionary[ontologyname] = ontology_classes_loader(ontology)
    
    with open('iriDictionary.json', 'w') as fp:
        json.dump(iri_dictionary, fp)
    
    return iri_dictionary
####

####

#TODO: Code aufraeumen!
def store_similarities(onto_combination, match_list):
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
    
    df.to_excel("./mapping/"+onto_combination[0]+"_"+onto_combination[1]+".xlsx")
    
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
    
    [ontoNameList_output.remove(key) for key in ontoNameList if not onto_format_validation(key,onto_URLs[key])]
    
    ontoNameList_output.remove("CHEMINF")
    ontoNameList_output.remove("EMMO")
    
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
    df = Ontology_Mapping()
####

####
def Similarity_Search_from_List(input_list,list_name):
    # Uses list of strings as input to output matching classes from ontology 
    # collection.
    onto_URLs = get_ontology_URLs()
    ontoNameList = list(onto_URLs.keys())
    ontoNameList_output = list(onto_URLs.keys())
    
    [ontoNameList_output.remove(key) for key in ontoNameList if not onto_format_validation(key,onto_URLs[key])]
    
    ontoNameList_output.remove("CHEMINF")
    ontoNameList_output.remove("EMMO")
    
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
        
        store_similarities(comb,match_list)
        
        df_numbers[comb[1]][comb[0]] = len(match_list)
    
    #print(df_numbers)
    df_numbers.to_excel("MappingHeatmap_"+list_name+".xlsx")
    
    return df_numbers
        
####
def run_similarity_from_vocabulary(): 
    test_ontology = get_ontology('./ontologies/voc4cat.owl').load()
    ind_list = list(test_ontology.individuals())
    #prefList = [[str(i.prefLabel[0]),i.altLabel] for i in ind_list]
    prefList = [str(i.prefLabel[0]) for i in ind_list]
    Similarity_Search_from_List(prefList,"input_list")
####

t = time.time()

df = pd.read_excel("Combined Cleaned Vocabulary.xlsx", sheet_name = "Concepts", skiprows=1)
column_data = list(df["Preferred Label*"])
data_frame_numbers = Similarity_Search_from_List(column_data,"Combined Cleaned Vocabulary")

elapsed = time.time() - t

print(elapsed)


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




    
        