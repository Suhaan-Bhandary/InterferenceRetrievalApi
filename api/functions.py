import pandas as pd
from owlready2 import get_ontology, destroy_entity, Thing, types, owl
import ontospy
from ontospy.gendocs.viz.viz_html_single import *
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz
import nltk
nltk.download('punkt')


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


def find_matching_words(user_input, database_words):
    user_input_tokens = word_tokenize(user_input.lower())
    matching_words = []
    threshold = 34

    for word in database_words:
        word_tokens = word_tokenize(word.lower())
        score = fuzz.ratio(user_input_tokens, word_tokens)

        if score >= threshold:  # Adjust threshold as per your requirements
            matching_words.append(word)

    return matching_words


def get_user_query_output(user_text):
    onto = get_ontology(r"spr-owl-data.owl").load()
    lst = []
    temp = list(onto.classes()) + list(onto.object_properties()) + \
        list(onto.data_properties())
    for i in temp:
        lst.append(str(i))
    lst.pop(-26)
    database = lst
    matching_words = find_matching_words(user_text, database)
    print(matching_words)
    return_json = []
    for i in matching_words:
        data = {}
        word = i.split('.')[1]
        if (str(type(onto[word])) == "<class 'owlready2.entity.ThingClass'>"):
            data['class_name'] = word
            data['sub_class_name'] = str(list(onto[word].ancestors()))
            data['parent_class_name'] = str(list(onto[word].descendants()))
            print("ancestor " + str(list(onto[word].ancestors())))
            print("descendant  " + str(list(onto[word].descendants())))

        if (str(type(onto[word])) == "<class 'owlready2.prop.ObjectPropertyClass'>"):
            data['relationship'] = word
            data['relationship-domain'] = str(onto[word].domain)
            data['relationship-range'] = str(onto[word].range)
            print(str(onto[word].domain) + " is " +
                  word + " " + str(onto[word].range))

        try:
            data_prop = list(onto[word].get_class_properties())
            data['attribute'] = []
            if (len(data_prop) > 1):
                for j in data_prop:
                    print(j)
                    print(getattr(onto[word], j.name))
                    data['attribute'].append(
                        {'Attribute_name': j, 'Attribute_value': getattr(onto[word], j.name)})
            else:
                print(data_prop[0])
                data['attribute'].append({'Attribute_name': data_prop[0], 'Attribute_value': getattr(
                    onto[word], data_prop[0].name)})

                print(getattr(onto[word], data_prop[0].name))
        except:
            print("None")
        return_json.append(data)

    print(return_json)

    return return_json
