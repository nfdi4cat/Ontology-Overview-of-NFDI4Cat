from owlready2 import *
import itertools
import pandas as pd
import os
import seaborn as sns
import json
import urllib  # the lib that handles the url stuff

def ontology_comparison(onto_name1, onto_name2):
    # Load the two ontologies
    onto1 = get_ontology("file://./ontology_files/" + onto_name1).load()
    onto2 = get_ontology("file://./ontology_files/" + onto_name2).load()
    
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
                            
                        """             
                        else:
                            for i in throw_list[1:]:
                                del temp_dict_cleaned[str(i)]
                                key_set = set(list(temp_dict_cleaned.keys()))
                        """
    
    """
    temp_dict = dict(temp_dict_cleaned)
    for i in list(temp_dict_cleaned.keys()):
        for dicts in temp_dict_cleaned[i][onto_name1]:
            if dicts["label"] != None:
                try: 
                    temp_dict[dicts["label"]] = temp_dict_cleaned[dicts["prefLabel"]]
                    del temp_dict[dicts["prefLabel"]]
                    
                except:
                    
                    try:
                        temp_dict[dicts["label"]] = temp_dict_cleaned[dicts["altLabel"]]
                        del temp_dict[dicts["altLabel"]]
                    except:
                        try:
                            temp_dict[dicts["label"]] = temp_dict_cleaned[dicts["name"]]
                            del temp_dict[dicts["name"]]
                        except:    
                            pass
      """              
                #onto_class = onto1.search_one(label = str(i))
                #if onto_class == None:
                #    print("class '{}' not existent in AFO.owl".format(i))
        
    
    return onto1_classes, common_labels, temp_dict_out, result_dict

####

def load_ontologies_metadata():
    ## Reads in the metadata-json files of each ontology, omitting the 
    #  GeneralStructure and md-translator files as they do not contain metadata.
    #  output: metadata_dict that contains the acronyms of the ontologies as keys
    #          and the respective json-file as dictionary are the values
    json_list = [f for f in os.listdir('./json/') if (f.endswith('.json') and f != "GeneralStructure.json" and f!= "md-translator.json")]
    metadata_dict = {}
    for json_name in json_list:
        with open('./json/' + json_name) as file:
            onto_metadata = json.load(file)
            metadata_dict[onto_metadata["Ontology"]["Ontology Acronym"]] = onto_metadata
  
    return metadata_dict        

####

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
    ontology_output_filename = onto_name + '.owl'
    
    onto_txt = urllib.request.urlopen(url)
    onto_txt = onto_txt.read()#readlines()

    with open('./ontologies/'+onto_name+'.ttl', 'wb') as onto_file:
        onto_file.write(onto_txt)
    
    os.system(".\\robot\\robot convert --input .\\ontologies\\{} --format owl --output .\\ontologies\\{}".format(filename, ontology_output_filename))
    
    return ontology_output_filename
####

####
def load_ontology_from_URL(onto_name, URL):
    ## Tries to load in the ontology by accessing the URL to an owl-file
    #  
    if URL.endswith('.owl'):
        try: 
            onto_loaded = get_ontology(URL).load()
            print("Successfully loaded Ontology: {}".format(onto_name))
        except:
            print("Something went wrong, ontology name: ".format(onto_name))
            onto_loaded = None
            pass
        
    elif URL.endswith('.ttl'):
        print("Ontology {} is provided as ttl, attempting download".format(URL))
        ontology_in_owl = ttl_to_owl(URL)
        onto_loaded = get_ontology('./ontologies./' + ontology_in_owl).load()

    else:
        print("Unknown file-ending for ontology {}, please check the URL!\n    URL: {}".format(onto_name, URL))
        onto_loaded = None   
    
    
    return onto_loaded
####

####
def onto_format_validation(onto_name, URL):
    ## prints compatibility of provided links with owlready2
    #  
    if URL.endswith('.owl'):
        #print("OWL: {}, {}".format(onto_name, URL))
        pass
    elif URL.endswith('.ttl'):
        #print("TTL: {}, {} -> will need formatting".format(onto_name, URL))
        pass
    else:
        print("Non-Conform: {}, {} -> not compatible".format(onto_name, URL))
    
####
#print out ontologies without proper URLs -> 
#TODO: fix those links
onto_URLs = get_ontology_URLs()

for i in onto_URLs:
    onto_format_validation(i, onto_URLs[i])   
####    

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
        if "contained" in md_dict[onto_abbrev][key_dom_interest][domain]:
            onto_list.append(onto_abbrev)
    
    domain_dict[domain] = onto_list
####

#for key in onto_URLs:
#    load_ontology_from_URL(key, onto_URLs[key])

"""
#onto_list = ["AFO.owl", "BFO.owl", "BAO.owl", "CHMO.owl"]
onto_list = [s for s in os.listdir('./ontology_files/') if s.endswith('.owl')]

df_numbers = pd.DataFrame(index = onto_list, columns = onto_list)

onto_combinations = list(itertools.combinations(onto_list, 2))

for onto_name in onto_list:
    print("current ontology: {}".format(onto_name))
    onto = get_ontology("file://./ontology_files/" + onto_name).load()
    print("... loaded successfully")
    try:
        #onto_labels = set([cls.label.first() for cls in onto.classes()])
        df_numbers[onto_name][onto_name] = len(list(onto.classes()))+1 # +1 for owl:Thing
    except: 
        print("Class labels of ontology " + onto_name + "not well defined and could not be read!")


for comb in onto_combinations:
    try:
        classList, labelList, compDict, resDict = ontology_comparison(comb[0],comb[1])
        df_numbers[comb[0]][comb[1]] = len(list(compDict.keys()))
    except:
        df_numbers[comb[0]][comb[1]] = 0
        print(comb)

        
print(df_numbers)
df_numbers.to_excel("MappingHeatmap.xlsx")

sns.heatmap(df_numbers.fillna(0), annot=True, fmt='.1f', cmap='YlGnBu')

#classList, labelList, resDict = ontology_comparison("AFO.owl","BFO.owl")

#resDict["temporal region"]
##
#classList, labelList, compDict, resDict = ontology_comparison("AFO.owl","CHMO.owl")
classList, labelList, compDict, resDict = ontology_comparison("AFO.owl","BFO.owl")

df_resIRIs = pd.DataFrame(columns = ["label","AFO.owl","CHMO.owl"])
labelList = []
onto1List = []
onto2List = []

for i in resDict:
    labelList.append(i)
    for subdict in resDict[i]["AFO.owl"]:
        onto1List.append(subdict["iri"])
        
df_resIRIs["label"] = labelList

#with open("tester123.json", "w") as f:
#    print(resDict, file =f)

"""

"""
for labelStr in resDict:
    for onto in resDict[labelStr]:
        for subdict in resDict[labelStr][onto]:
                try:
                    resDict[subdict["prefLabel"]][onto] = None
                except:
                    pass
                
                try:
                    resDict[subdict["altLabel"]][onto] = None
                except:
                    pass
                
                try:
                    resDict[subdict["name"]][onto] = None
                except:
                    pass
                
 """           
#onto_bfo = get_ontology("./ontology_files/AFO.owl").load()
#for i in list(resDict.keys()):
#    onto_class = onto_bfo.search_one(label = str(i))
#    if onto_class == None:
#        print("class '{}' not existent in AFO.owl".format(i))
    
    

##
# Ab hier: Dict Entries vergleichen
# bspw: resDict["temporal region"]
# müsste eigentlich das selbe sein wie resDict["BFO_0000008"]??

#same_list = []
#for label in resDict:
    #if resDict[label]["AFO.owl"] == resDict[label]["BFO.owl"]:
    #    same_list += [label]
    
#    list(resDict[label].keys())
    
    
    
    
    
        