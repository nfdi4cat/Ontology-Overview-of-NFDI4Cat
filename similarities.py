from owlready2 import *
import itertools
import pandas as pd
import os

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
        
        result_dict[i] = {onto_name1:labeldict1,
                          onto_name2:labeldict2}
   
    
    for label in result_dict:
        if result_dict[label][onto_name1] != result_dict[label][onto_name1]:
            print("Multiple Classes detected for label '{}' in ontologies {} and {}".format(label, onto_name1, onto_name2))
            
        else:
            # If all entries in subdict of label, onto_name1 are same, 
            # The entries are "condensed" to remove duplicates 
            condensed_dict_list = []
            for key in result_dict[label][onto_name1]:
                if result_dict[label][onto_name1][key] not in condensed_dict_list and result_dict[label][onto_name1][key] != None:
                    condensed_dict_list.append(result_dict[label][onto_name1][key])
        
            result_dict[label][onto_name1] = condensed_dict_list
            
            # same for onto_name2
            condensed_dict_list = []
            for key in result_dict[label][onto_name2]:
                if result_dict[label][onto_name2][key] not in condensed_dict_list and result_dict[label][onto_name2][key] != None:
                    condensed_dict_list.append(result_dict[label][onto_name2][key])
            
            result_dict[label][onto_name2] = condensed_dict_list
    
    # removing empty entries:
    temp_dict = dict(result_dict)
    for label in result_dict:
        if result_dict[label][onto_name1] == [] and result_dict[label][onto_name2] == []:
            del temp_dict[label]
    
    
    return onto1_classes, common_labels, result_dict, temp_dict


#onto_list = ["AFO.owl", "BFO.owl", "BAO.owl", "CHMO.owl"]
onto_list = [s for s in os.listdir('./ontology_files/') if s.endswith('.owl')]

df_numbers = pd.DataFrame(index = onto_list, columns = onto_list)

onto_combinations = list(itertools.combinations(onto_list, 2))

for onto_name in onto_list:
    onto = get_ontology("file://./ontology_files/" + onto_name).load()
    try:
        #onto_labels = set([cls.label.first() for cls in onto.classes()])
        df_numbers[onto_name][onto_name] = len(list(onto.classes()))+1 # +1 for owl:Thing
    except: 
        print("Class labels of ontology " + onto_name + "not well defined and could not be read!")


for comb in onto_combinations:
    try:
        df_numbers[comb[0]][comb[1]] = len(ontology_comparison(comb[0],comb[1])[0])
    except:
        df_numbers[comb[0]][comb[1]] = 0
        print(comb)

        
print(df_numbers)


classList, labelList, resDict, condDict = ontology_comparison("AFO.owl","BFO.owl")

resDict["temporal region"]
##
#classList, labelList, resDict = ontology_comparison("AFO.owl","BFO.owl")
#with open("tester123.json", "w") as f:
#    print(resDict, file =f)

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
onto_bfo = get_ontology("./ontology_files/BFO.owl").load()
for i in list(condDict.keys()):
    
    
    

##
# Ab hier: Dict Entries vergleichen
# bspw: resDict["temporal region"]
# müsste eigentlich das selbe sein wie resDict["BFO_0000008"]??

#same_list = []
#for label in resDict:
    #if resDict[label]["AFO.owl"] == resDict[label]["BFO.owl"]:
    #    same_list += [label]
    
#    list(resDict[label].keys())
    
    
    
    
    
        