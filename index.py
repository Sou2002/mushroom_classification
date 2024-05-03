import streamlit as st
import requests
import json

st.set_page_config(layout="wide")

st.title("Mushroom Classification")

st.markdown("### Select Characteristics")

my_dict: dict = {}

with st.form("form 1"):
    col1, col2, col3 = st.columns(3)
    my_dict['cap-shape'] = col1.selectbox('Cap Shape', options=(
        'Bell', 'Conical', 'Convex', 'Flat', 'Knobbed'), index=None, placeholder='Choose an option')
    my_dict['cap-surface'] = col2.selectbox('Cap Surface', options=(
        'Fibrous', 'Grooves', 'Scaly', 'Smooth'), index=None, placeholder='Choose an option')
    my_dict['cap-color'] = col3.selectbox('Cap Color', options=('Brown', 'Buff', 'Cinnamon',
                                                                'Gray', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    my_dict['bruises'] = col1.selectbox('Bruises', options=('Yes', 'No'),
                                        index=None, placeholder='Choose an option')
    my_dict['odor'] = col2.selectbox('Odor', options=('Almond', 'Anise', 'Creosote',
                                                      'Fishy', 'Foul', 'Musty', 'None', 'Pungent', 'Spicy'), index=None, placeholder='Choose an option')
    my_dict['gill-attachment'] = col3.selectbox('Gill Attachment', options=(
        'Attached', 'Descending', 'Free', 'Notched'), index=None, placeholder='Choose an option')
    my_dict['gill-spacing'] = col1.selectbox('Gill Spacing', options=('Close', 'Crowded',
                                                                       'Distant'), index=None, placeholder='Choose an option')
    my_dict['gill-size'] = col2.selectbox('Gill Size', options=('Broad', 'Narrow'),
                                          index=None, placeholder='Choose an option')
    my_dict['gill-color'] = col3.selectbox('Gill Color', options=('Black', 'Brown', 'Buff', 'Chocolate',
                                                                  'Gray', 'Green', 'Orange', 'Pink', 'Purple', 'Red', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    my_dict['stalk-shape'] = col1.selectbox('Stalk Shape', options=('Enlarging', 'Tapering'),
                                            index=None, placeholder='Choose an option')
    my_dict['stalk-root'] = col2.selectbox('Stalk Root', options=(
        'Bulbous', 'Club', 'Cup', 'Equal', 'Rhizomorphs'), index=None, placeholder='Choose an option')
    my_dict['stalk-surface-above-ring'] = col3.selectbox('Stalk Serface Above Ring', options=(
        'Fibrous', 'Scaly', 'Silky', 'Smooth'), index=None, placeholder='Choose an option')
    my_dict['stalk-surface-below-ring'] = col1.selectbox('Stalk Serface Below Ring', options=(
        'Fibrous', 'Scaly', 'Silky', 'Smooth'), index=None, placeholder='Choose an option')
    my_dict['stalk-color-above-ring'] = col2.selectbox('Stalk Color Above Ring', options=(
        'Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    my_dict['stalk-color-below-ring'] = col3.selectbox('Stalk Color Below Ring', options=(
        'Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    my_dict['veil-type'] = col1.selectbox('Veil Type', options=('Partial', 'Universal'),
                                          index=None, placeholder='Choose an option')
    my_dict['veil-color'] = col2.selectbox('Veil Color', options=(
        'Brown', 'Orange', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    my_dict['ring-number'] = col3.selectbox('Ring Number', options=('None', 'One', 'Two'),
                                            index=None, placeholder='Choose an option')
    my_dict['ring-type'] = col1.selectbox('Ring Type', options=('Cobwebby', 'Evanescent',
                                                                'Flaring', 'Large', 'None', 'Pendant', 'Sheathing', 'Zone'), index=None, placeholder='Choose an option')
    my_dict['spore-print-color'] = col2.selectbox('Spore Print Color', options=('Black', 'Brown', 'Buff',
                                                                                'Chocolate', 'Gray', 'Orange', 'Purple', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    my_dict['population'] = col3.selectbox('Population', options=('Abundant', 'Clustered',
                                                                  'Numerous', 'Scattered', 'Several', 'Solitary'), index=None, placeholder='Choose an option')
    my_dict['habitat'] = col1.selectbox('Habitat', options=('Grasses', 'Leaves',
                                                            'Meadows', 'Paths', 'Urban', 'Waste', 'Woods'), index=None, placeholder='Choose an option')

    submit = st.form_submit_button("Submit")

    url = 'http://localhost:8000/predict'

    if submit:
        if not all(my_dict.values()):
            st.error('##### **Please fill all the fields.**')
        else:
            headers = {'Content-Type': 'application/json'}
            req = requests.post(url, data=json.dumps(my_dict), headers=headers)
            st.write(req.text.strip('"'))
