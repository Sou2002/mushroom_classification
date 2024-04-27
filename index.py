import streamlit as st

st.title("Mushroom Classification")

st.markdown("<h1>Attributes</h1>", unsafe_allow_html=True)

with st.form("form 1"):
    col1, col2, col3 = st.columns(3)
    col1.selectbox('Cap Shape', options=(
        'Bell', 'Conical', 'Convex', 'Flat', 'Knobbed'), index=None, placeholder='Choose an option')
    col2.selectbox('Cap Surface', options=(
        'Fibrous', 'Grooves', 'Scaly', 'Smooth'), index=None, placeholder='Choose an option')
    col3.selectbox('Cap Color', options=('Brown', 'Buff', 'Cinnamon',
                                         'Gray', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    col1.selectbox('Bruises', options=('Yes', 'No'),
                   index=None, placeholder='Choose an option')
    col2.selectbox('Odor', options=('Almond', 'Anise', 'Creosote',
                                    'Fishy', 'Foul', 'Musty', 'None', 'Pungent', 'Spicy'), index=None, placeholder='Choose an option')
    col3.selectbox('Gill Attachment', options=(
        'Attached', 'Descending', 'Free', 'Notched'), index=None, placeholder='Choose an option')
    col1.selectbox('Gill Spacing', options=('Closed', 'Crowded',
                   'Distant'), index=None, placeholder='Choose an option')
    col2.selectbox('Gill Size', options=('Broad', 'Narrow'),
                   index=None, placeholder='Choose an option')
    col3.selectbox('Gill Color', options=('Black', 'Brown', 'Buff', 'Chocolate',
                                          'Gray', 'Green', 'Orange', 'Pink', 'Purple', 'Red', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    col1.selectbox('Stalk Shape', options=('Enlarging', 'Tapering'),
                   index=None, placeholder='Choose an option')
    col2.selectbox('Stalk Root', options=(
        'Bulbous', 'Club', 'Cup', 'Equal', 'rhizomorphs'), index=None, placeholder='Choose an option')
    col3.selectbox('Stalk Serface Above Ring', options=(
        'Fibrous', 'Scaly', 'Silky', 'Smooth'), index=None, placeholder='Choose an option')
    col1.selectbox('Stalk Serface Below Ring', options=(
        'Fibrous', 'Scaly', 'Silky', 'Smooth'), index=None, placeholder='Choose an option')
    col2.selectbox('Stalk Color Above Ring', options=(
        'Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    col3.selectbox('Stalk Color Below Ring', options=(
        'Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    col1.selectbox('Veil Type', options=('Partial', 'Universal'),
                   index=None, placeholder='Choose an option')
    col2.selectbox('Veil Color', options=(
        'Brown', 'Orange', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    col3.selectbox('Ring Number', options=('None', 'One', 'Two'),
                   index=None, placeholder='Choose an option')
    col1.selectbox('Ring Type', options=('Cobwebby', 'Evanescent',
                   'Flaring', 'Large', 'None', 'Pendant', 'Sheathing', 'Zone'), index=None, placeholder='Choose an option')
    col2.selectbox('Spore Print Color', options=('Black', 'Brown', 'Buff',
                   'Chocolate', 'Gray', 'Orange', 'Purple', 'White', 'Yellow'), index=None, placeholder='Choose an option')
    col3.selectbox('Population', options=('Abundant', 'Clustered',
                   'Numerous', 'Scattered', 'Several', 'Solitary'), index=None, placeholder='Choose an option')
    col1.selectbox('Habitat', options=('Grasses', 'Leaves',
                   'Meadows', 'Paths', 'urban', 'Waste', 'Woods'), index=None, placeholder='Choose an option')

    st.form_submit_button("Submit")
