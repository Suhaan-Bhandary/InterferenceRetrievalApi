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
    SPR_label_mapping_data_frame.dropna()

    # File handler type, gets a hold to the ontology(OWL FILE)
    onto = get_ontology(r"spr-owl-data.owl").load()

    for spr_data_row in SPR_label_mapping_data_frame['SPR Label Name'].dropna():
        # Getting the spr_class_name from the i
        spr_class_name = spr_data_row.split(': ')[1]
        print(spr_class_name)

        formatted_spr_class_name = spr_class_name.replace(' ', '_')
        print(formatted_spr_class_name)

        with onto:
            my_new_class = types.new_class(formatted_spr_class_name, (Thing,))
            onto.save(file="spr-owl-data.owl")

    return list(onto.classes())
