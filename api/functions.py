import pandas as pd
from owlready2 import get_ontology, destroy_entity, Thing, types, owl
import ontospy
from ontospy.gendocs.viz.viz_html_single import *


def update_class(class_name, sub_class_name, relationship, domain, range):
    # File handler type, gets a hold to the ontology(OWL FILE)
    onto = get_ontology(r"spr-owl-data.owl").load()

    with onto:
        try:
            my_new_class = types.new_class(class_name, (Thing,))
            my_new_subclass = types.new_class(sub_class_name, (my_new_class,))
        except:
            print("errorrrrr")
        try:
            new_property = type(relationship, (owl.ObjectProperty,), {
                'domain': [onto[domain]], 'range': [onto[range]]})
        except:
            print("errorr")

    onto.save(file="spr-owl-data.owl")

    # -------------------------------------------------------------------------------------------------------

    # To view added classes and subclasses, use this. onto.classes return generated which can be listed out with using list(onto.classes)
    # At the bottom you can see added classes, in the console
    onto_classes = list(onto.classes())
    return onto_classes


def get_data_summary():
    g = ontospy.Ontospy(r"spr-owl-data.owl")

    v = HTMLVisualizer(g)  # => instantiate the visualization object
    v.build()  # => render visualization. You can pass an 'output_path' parameter too
    v.preview()  # => open in browser


def delete_class(class_name):
    onto = get_ontology(r"spr-owl-data.owl").load()
    entity = onto[class_name]
    # -------------------------------------------------------------------------------------------------------

    # Delete class or subclasses
    try:
        destroy_entity(entity)
    except:
        print('Already Deleted')

    # -------------------------------------------------------------------------------------------------------

    # Save file, add location of the owl file in file='FILE_LOCATION'
    onto.save(file="spr-owl-data.owl")

    onto_classes = list(onto.classes())
    return onto_classes


def create_class(file_obj):
    analysis_data_frame = pd.ExcelFile(file_obj)

    SPR_label_mapping_data_frame = pd.read_excel(
        analysis_data_frame, 'SPR Label Mapping')

    SPR_label_mapping_data_frame.dropna(inplace=True)

    SPR_label_mapping_data_frame['SPR Label Name'] = SPR_label_mapping_data_frame['SPR Label Name'].apply(
        lambda x: x.split(': ')[1])
    SPR_label_mapping_data_frame['SPR Label Name'] = SPR_label_mapping_data_frame['SPR Label Name'].apply(
        lambda x: x.replace(' ', '_'))

    # File handler type, gets a hold to the ontology(OWL FILE)
    with open('spr-owl-data.owl', 'w') as fp:
        pass
    onto = get_ontology(r"spr-owl-data.owl").load()

    my_new_class = ""

    SPR_label_mapping_data_frame_gb = SPR_label_mapping_data_frame.groupby(by=[
                                                                           'SPR Label Name'])

    for class_name in SPR_label_mapping_data_frame['SPR Label Name'].unique():
        sub_class = SPR_label_mapping_data_frame_gb.get_group((class_name))[
            'SP3D Classname'].values
        with onto:
            my_new_class = types.new_class(class_name, (Thing,))

        if (len(sub_class) > 1):

            for sub_class_name in sub_class:
                with onto:
                    my_new_subclass = types.new_class(
                        sub_class_name, (my_new_class,))

        else:
            with onto:
                my_new_subclass = types.new_class(
                    sub_class[0], (my_new_class,))

        onto.save(file="spr-owl-data.owl")

    onto_classes = list(onto.classes())
    return onto_classes


def get_user_query_output(user_text):
    tokens = user_text.split(" ")

    onto = get_ontology(r"spr-owl-data.owl").load()
    search_result = {}
    onto_classes = {}

    for onto_class in list(onto.classes()):
        onto_classes[str(onto_class)] = onto_class

    for token in tokens:
        if token in onto_classes:
            target_onto_class = onto_classes[token]

            search_result['subclass'] = target_onto_class.descendants()
            search_result['part_of'] = target_onto_class.ancestors()
            # for i in list(onto.object_properties())[1:]:
            #     val = onto[i.name]
            #     val2 = val.domain
            #     if len(str(val2[0]).split(".")) > 1:
            #         print(val2)
            #     if len(val2) > 1:
            #         print(val2[1])
            # print(onto.after.domain)
            # print(target_onto_class.object_properties())
            # search_result['relationship'] = target_onto_class.object_properties()

    return str(search_result)
