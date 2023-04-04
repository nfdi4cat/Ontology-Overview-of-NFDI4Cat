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
    
    try:
        onto1_labels = set([cls.label.first() for cls in onto1.classes()])
    except:
        print("Class labels of ontology " + onto_name1 + "not well defined and could not be read!")
    
    try:
        onto2_labels = set([cls.label.first() for cls in onto2.classes()])
    
    except:
        print("Class labels of ontology " + onto_name2 + "not well defined and could not be read!")
    
    # Find the intersection of the two sets of class labels
    
    try:
        common_labels = onto1_labels.intersection(onto2_labels)
    except:
        print("No common labels found for ontologies " + onto_name1 + " and " + onto_name2 +".\n Might also be caused by wrong label accessing!")
    
    # Find the classes in each ontology with the common labels
    try:
        onto1_classes = [onto1.search_one(label=label) for label in common_labels if label is not None]
    except:
        print("No common labels found for ontologies " + onto_name1 + " and " + onto_name2 +".\n Might also be caused by wrong label accessing! len(common_labels)= " + str(len(common_labels)))
        print(common_labels)
    #onto2_classes = [onto2.search_one(label=label) for label in common_labels]
    
    # Print out the matching classes
   # for i, cls1 in enumerate(onto1_classes):
   #     cls2 = onto2_classes[i]
   #     print(f"{cls1.name} ({cls1.label.first()}) in Ontology 1 matches {cls2.name} ({cls2.label.first()}) in Ontology 2")
        
    return onto1_classes


#onto_list = ["AFO.owl", "BFO.owl", "BAO.owl", "CHMO.owl"]
onto_list = [s for s in os.listdir('./ontology_files/') if s.endswith('.owl')]

df_numbers = pd.DataFrame(index = onto_list, columns = onto_list)

onto_combinations = list(itertools.combinations(onto_list, 2))

for onto_name in onto_list:
    onto = get_ontology("file://./ontology_files/" + onto_name).load()
    try:
        onto_labels = set([cls.label.first() for cls in onto.classes()])
        df_numbers[onto_name][onto_name] = len(onto_labels)
    except: 
        print("Class labels of ontology " + onto_name + "not well defined and could not be read!")


for comb in onto_combinations:
    try:
        df_numbers[comb[0]][comb[1]] = len(ontology_comparison(comb[0],comb[1]))
    except:
        df_numbers[comb[0]][comb[1]] = 0
        print(comb)
        
print(df_numbers)