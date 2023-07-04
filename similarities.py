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

def ontology_comparison(onto1, onto2):
    ### DEPRECATED FUNCTION!
    
    # Load the two ontologies
    #onto1 = get_ontology("file://./ontology_files/" + onto_name1).load()
    #onto2 = get_ontology("file://./ontology_files/" + onto_name2).load()
    onto_name1 = onto1.name
    onto_name2 = onto2.name
    # Create sets of class labels for each ontology
    ## using label depending on ontology!
    
    # label
    try:
        onto1_labels = set([cls.label.first() for cls in onto1.classes()])
    except:
        print("Class labels of ontology " + onto_name1 + " not (well) defined and could not be read!")
        onto1_labels= set()
    
    # prefLabel
    try:
        onto1_prefLabels = set([cls.prefLabel.first() for cls in onto1.classes()])
    except:
        print("Class prefLabels of ontology " + onto_name1 + " not (well) defined and could not be read!")
        onto1_prefLabels= set()
        
    # altLabel
    try:
        onto1_altLabels = set([cls.altLabel.first() for cls in onto1.classes()])
    except:
        print("Class altLabels of ontology " + onto_name1 + " not (well) defined and could not be read!")
        onto1_altLabels= set()
        
    # name
    try:
        onto1_names = set([cls.name for cls in onto1.classes()])
    except:
        print("Class names of ontology " + onto_name1 + " not (well) defined and could not be read!")
        onto1_names= set()
        
    # Concatenate prefLabels, labels and altLabels
    onto1_combined = ((onto1_labels.union(onto1_prefLabels)).union(onto1_altLabels)).union(onto1_names)
    
    ## 
    # Onto 2: 
    # label
    try:
        onto2_labels = set([cls.label.first() for cls in onto2.classes()])
    except:
        print("Class labels of ontology " + onto_name2 + " not (well) defined and could not be read!")
        onto2_labels= set()
        
    # prefLabel
    try:
        onto2_prefLabels = set([cls.prefLabel.first() for cls in onto2.classes()])
    except:
        print("Class prefLabels of ontology " + onto_name2 + " not (well) defined and could not be read!")
        onto2_prefLabels= set()
        
    # altLabel
    try:
        onto2_altLabels = set([cls.altLabel.first() for cls in onto2.classes()])
    except:
        print("Class altLabels of ontology " + onto_name2 + " not (well) defined and could not be read!")
        onto2_altLabels = set()
        
    # name
    try:
        onto2_names = set([cls.name for cls in onto2.classes()])
    except:
        print("Class names of ontology " + onto_name2 + " not (well) defined and could not be read!")
        onto2_names = set()
        
    # Concatenate prefLabels, labels and altLabels
    onto2_combined = ((onto2_labels.union(onto2_prefLabels)).union(onto2_altLabels)).union(onto2_names)
    
    ## 
    # Find the intersection of the two sets of class labels
    
    try:
        common_labels = onto1_combined.intersection(onto2_combined)
    except:
        print("No common labels found for ontologies " + onto_name1 + " and " + onto_name2 +".\n Might also be caused by wrong label accessing!")
    ######
    
    # delete none entries
    common_labels = [i for i in common_labels if i is not None]
    
    ######
    # Find the classes in each ontology with the common labels
    # label
    try:
        onto1_classes_label = [onto1.search_one(label=label) for label in common_labels if label is not None]
    except:
        print("No common labels found for ontologies " + onto_name1 + " and " + onto_name2 +".\n Might also be caused by wrong label accessing! len(common_labels)= " + str(len(common_labels)))
        print(common_labels)
    # prefLabel
    try:
        onto1_classes_prefLabel = [onto1.search_one(prefLabel=label) for label in common_labels if label is not None]
    except:
        print("No common labels found for ontologies " + onto_name1 + " and " + onto_name2 +".\n Might also be caused by wrong label accessing! len(common_labels)= " + str(len(common_labels)))
        print(common_labels)
    # altLabel
    try:
        onto1_classes_altLabel = [onto1.search_one(altLabel=label) for label in common_labels if label is not None]
    except:
        print("No common labels found for ontologies " + onto_name1 + " and " + onto_name2 +".\n Might also be caused by wrong label accessing! len(common_labels)= " + str(len(common_labels)))
        print(common_labels)
    # name
    try:        
        onto1_classes_name = [onto1.search_one(name=label) for label in common_labels if label is not None]
    except:
        print("No common labels found for ontologies " + onto_name1 + " and " + onto_name2 +".\n Might also be caused by wrong label accessing! len(common_labels)= " + str(len(common_labels)))
        print(common_labels)        
    ######
    
    concat_list = [onto1_classes_label,onto1_classes_prefLabel,onto1_classes_altLabel,onto1_classes_name]
    
    onto1_classes = set().union(*concat_list)
    onto1_classes = set([i for i in onto1_classes if i is not None])
    # Print out the matching classes
   # for i, cls1 in enumerate(onto1_classes):
   #     cls2 = onto2_classes[i]
   #     print(f"{cls1.name} ({cls1.label.first()}) in Ontology 1 matches {cls2.name} ({cls2.label.first()}) in Ontology 2")
   
    result_dict = {}
    for i in common_labels:
        labeldict1 ={"label":None,
                     "prefLabel":None,
                     "altLabel":None,
                     "name":None}
        
        labeldict2 ={"label":None,
                     "prefLabel":None,
                     "altLabel":None,
                     "name":None}
        
        
        # searching for each label, prefLabel, altLabel and name in the ontology.
        # first for label, then for prefLabel, ... and listing all the other 
        # descriptors in the dict
        try:
            labeldict1["label"] = {"label": onto1.search_one(label = i).label.first(),
                                   "prefLabel": onto1.search_one(label = i).prefLabel.first(),
                                   "altLabel": onto1.search_one(label = i).altLabel.first(),
                                   "name": onto1.search_one(label = i).name,
                                   "iri": onto1.search_one(label = i).get_iri(onto1.search_one(label = i))
                                   }
        except:
            pass

        try:
            #labeldict1["prefLabel"] = onto1.search_one(prefLabel = i)
            labeldict1["prefLabel"] = {"label": onto1.search_one(prefLabel = i).label.first(),
                                       "prefLabel": onto1.search_one(prefLabel = i).prefLabel.first(),
                                       "altLabel": onto1.search_one(prefLabel = i).altLabel.first(),
                                       "name": onto1.search_one(prefLabel = i).name,
                                       "iri": onto1.search_one(prefLabel = i).get_iri(onto1.search_one(prefLabel = i))
                                       }
        except:
            pass
       
        try:
            labeldict1["altLabel"] = {"label": onto1.search_one(altLabel = i).label.first(),
                           "prefLabel": onto1.search_one(altLabel = i).prefLabel.first(),
                           "altLabel": onto1.search_one(altLabel = i).altLabel.first(),
                           "name": onto1.search_one(altLabel = i).name,
                           "iri": onto1.search_one(altLabel = i).get_iri(onto1.search_one(altLabel = i))
                           }
        except:
            pass
        
        try:
            labeldict1["name"] = {"label": onto1.search_one(name = i).label.first(),
                                   "prefLabel": onto1.search_one(name = i).prefLabel.first(),
                                   "altLabel": onto1.search_one(name = i).altLabel.first(),
                                   "name": onto1.search_one(name = i).name,
                                   "iri": onto1.search_one(name = i).get_iri(onto1.search_one(name = i))
                                   }
        except:
            pass
        
        
        ## same with onto 2
        try:
            labeldict2["label"] = {"label": onto2.search_one(label = i).label.first(),
                           "prefLabel": onto2.search_one(label = i).prefLabel.first(),
                           "altLabel": onto2.search_one(label = i).altLabel.first(),
                           "name": onto2.search_one(label = i).name,
                           "iri": onto2.search_one(label = i).get_iri(onto2.search_one(label = i))
                           }
        except:
            pass
        try:
            labeldict2["prefLabel"] = {"label": onto2.search_one(prefLabel = i).label.first(),
                           "prefLabel": onto2.search_one(prefLabel = i).prefLabel.first(),
                           "altLabel": onto2.search_one(prefLabel = i).altLabel.first(),
                           "name": onto2.search_one(prefLabel = i).name,
                           "iri": onto2.search_one(prefLabel = i).get_iri(onto2.search_one(prefLabel = i))
                           }
        except:
            pass
        
        try:
            labeldict2["altLabel"] = {"label": onto2.search_one(altLabel = i).label.first(),
                           "prefLabel": onto2.search_one(altLabel = i).prefLabel.first(),
                           "altLabel": onto2.search_one(altLabel = i).altLabel.first(),
                           "name": onto2.search_one(altLabel = i).name,
                           "iri": onto2.search_one(altLabel = i).get_iri(onto2.search_one(altLabel = i))
                           }
        except:
            pass
        
        try:
            labeldict2["name"] = {"label": onto2.search_one(name = i).label.first(),
                           "prefLabel": onto2.search_one(name = i).prefLabel.first(),
                           "altLabel": onto2.search_one(name = i).altLabel.first(),
                           "name": onto2.search_one(name = i).name,
                           "iri": onto2.search_one(name = i).get_iri(onto2.search_one(name = i))
                           }
        except:
            pass
        
        result_dict[str(i)] = {onto_name1:labeldict1,
                          onto_name2:labeldict2}
   
    
    for label in result_dict:
        if result_dict[str(label)][onto_name1] != result_dict[str(label)][onto_name1]:
            print("Multiple Classes detected for label '{}' in ontologies {} and {}".format(label, onto_name1, onto_name2))
            
        else:
            # If all entries in subdict of label, onto_name1 are same, 
            # The entries are "condensed" to remove duplicates 
            condensed_dict_list = []
            for key in result_dict[str(label)][onto_name1]:
                if result_dict[str(label)][onto_name1][key] not in condensed_dict_list and result_dict[str(label)][onto_name1][key] != None:
                    condensed_dict_list.append(result_dict[str(label)][onto_name1][key])
        
            result_dict[str(label)][onto_name1] = condensed_dict_list
            
            # same for onto_name2
            condensed_dict_list = []
            for key in result_dict[str(label)][onto_name2]:
                if result_dict[str(label)][onto_name2][key] not in condensed_dict_list and result_dict[str(label)][onto_name2][key] != None:
                    condensed_dict_list.append(result_dict[str(label)][onto_name2][key])
            
            result_dict[str(label)][onto_name2] = condensed_dict_list
    
    ##
    # removing empty entries: 
    temp_dict = dict(result_dict)
    for label in result_dict:
        if result_dict[str(label)][onto_name1] == [] and result_dict[str(label)][onto_name2] == []:
            del temp_dict[str(label)]
    
    # another cleaning step for comparison of different labeling types in list:
    key_set = set(list(temp_dict.keys()))
    temp_dict_out = dict(temp_dict)
    
    for label in temp_dict:
        if temp_dict[label][onto_name1] == temp_dict[label][onto_name2]:
            dict_list = []
            for entries in temp_dict[label][onto_name1]:
                for keys in entries:
                    if entries[keys] != None and keys != "iri":
                        dict_list.append(entries[keys])
            
            throw_list = list(key_set.intersection(dict_list))
    # ab hier:        
            if len(throw_list) > 1:
                for i in list(temp_dict.keys()):
                    for dicts in temp_dict[i][onto_name1]:
                        if dicts["label"] != None:
                            try:
                                throw_list.remove(dicts["label"])
                                for i in throw_list:
                                    del temp_dict_out[str(i)]
                                    key_set = set(list(temp_dict_out.keys()))
                            except:
                                pass        
    
    return onto1_classes, common_labels, temp_dict_out, result_dict

####


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
def load_ontology_from_URL(onto_name):
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
        ontology = load_ontology_from_URL(ontologyname)
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
    
    # Create DataFrame from the data
    df = pd.DataFrame({onto_combination[0]+'_IRI': onto1_data1, onto_combination[0]+'_DESC':onto1_data2, onto_combination[1]+'_IRI': onto2_data1, onto_combination[1]+'_DESC':onto2_data2})
    
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
def Similarity_Search_from_List(input_list):
    # Uses list of strings as input to output matching classes from ontology 
    # collection.
    onto_URLs = get_ontology_URLs()
    ontoNameList = list(onto_URLs.keys())
    ontoNameList_output = list(onto_URLs.keys())
    
    [ontoNameList_output.remove(key) for key in ontoNameList if not onto_format_validation(key,onto_URLs[key])]
    
    ontoNameList_output.remove("CHEMINF")
    ontoNameList_output.remove("EMMO")
    
    #onto_combinations = list(itertools.combinations(ontoNameList_output, 2))
    df_numbers = pd.DataFrame(index = ['input_list'], columns = ontoNameList_output)

    
    with open("./iriDictionary.json") as f: 
        iri_dictionary = json.load(f)
    
    for ontology in ontoNameList_output:
        onto_dict1 = iri_dictionary[ontology]
        
        comb = ('input_list', ontology)
        
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
    df_numbers.to_excel("MappingHeatmap_Input_list.xlsx")
    
    return df_numbers
        
####
def run_similarity_from_vocabulary(): 
    test_ontology = get_ontology('./ontologies/Photocatalysis_LIKAT_template043_final.owl').load()
    ind_list = list(test_ontology.individuals())
    prefList = [str(i.prefLabel[0]) for i in ind_list]
    Similarity_Search_from_List(prefList)


####
#print out ontologies without proper URLs -> 
#TODO: find those links and fix it in MasterTable
#onto_URLs = get_ontology_URLs()
#for i in onto_URLs:
#    onto_format_validation(i, onto_URLs[i])   
####




    
        