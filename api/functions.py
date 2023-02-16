import pandas as pd
from owlready2 import get_ontology, destroy_entity, Thing, types



def create_class():
    # File handler type, gets a hold to the ontology(OWL FILE)
    onto = get_ontology(r"tech-int.owl").load()

    # -------------------------------------------------------------------------------------------------------

    # Create a class with this handles
    with onto:
        class Drug(Thing):
            pass

    # -------------------------------------------------------------------------------------------------------

    # Create Subclass
    # <---- Add spr_class_name in brackets class SUBCLASS_NAME(CLASS_NAME)
    class DrugAssociation(Drug):
        pass

    # -------------------------------------------------------------------------------------------------------

    # Save file, add location of the owl file in file='FILE_LOCATION'
    onto.save(file="tech-int.owl")

    # -------------------------------------------------------------------------------------------------------

    # To view added classes and subclasses, use this. onto.classes return generated which can be listed out with using list(onto.classes)
    # At the bottom you can see added classes, in the console
    onto_classes = list(onto.classes())
    return onto_classes


def delete_class():
    onto = get_ontology(r"tech-int.owl").load()

    # -------------------------------------------------------------------------------------------------------

    # Delete class or subclasses
    try:
        destroy_entity(onto.Drug)
    except:
        print('Already Deleted')
        print()

    # -------------------------------------------------------------------------------------------------------

    # To view deleted classes and subclasses, use onto.classes return generated which can be listed out with using list(onto.classes)
    # At the bottom you can see deleted classes, in the console
    print(list(onto.classes()))

    # -------------------------------------------------------------------------------------------------------

    # Save file, add location of the owl file in file='FILE_LOCATION'
    onto.save(file="tech-int.owl")


def update_class():
    analysis_data_frame = pd.ExcelFile('MDB2_Analysis.xlsx')

    SPR_label_mapping_data_frame = pd.read_excel(
        analysis_data_frame, 'SPR Label Mapping')

    SPR_label_mapping_data_frame.dropna(inplace=True)

    SPR_label_mapping_data_frame['SPR Label Name'] = SPR_label_mapping_data_frame['SPR Label Name'].apply(lambda x: x.split(': ')[1])
    SPR_label_mapping_data_frame['SPR Label Name']  = SPR_label_mapping_data_frame['SPR Label Name'].apply(lambda x: x.replace(' ','_'))
    

    # File handler type, gets a hold to the ontology(OWL FILE)
    with open('spr-owl-data.owl', 'w') as fp:
        pass
    onto = get_ontology(r"spr-owl-data.owl").load()

    my_new_class = ""
    
    SPR_label_mapping_data_frame_gb = SPR_label_mapping_data_frame.groupby(by=['SPR Label Name'])

    for class_name in SPR_label_mapping_data_frame['SPR Label Name'].unique():
        sub_class = SPR_label_mapping_data_frame_gb.get_group((class_name))['SP3D Classname'].values
        with onto:
            my_new_class = types.new_class(class_name, (Thing,))
            
        if(len(sub_class) > 1):
            
            for sub_class_name in sub_class:
                with onto:
                    my_new_subclass = types.new_class(sub_class_name,(my_new_class,))

        else:
            with onto:
                    my_new_subclass = types.new_class(sub_class[0],(my_new_class,))

        
            
            
        onto.save(file = "spr-owl-data.owl") 

        

    # print(list(onto.classes()))

    return list(onto.classes())



# print(update_class())