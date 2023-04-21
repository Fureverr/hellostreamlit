import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    'What is your favourite color?',
    ('Blue','Red','Green')
)
st.write('Your favourite color is ',option)

# DAY 11
# multiselect
st.header('st.multiselect')

options = st.multiselect(
    'What is your favorite colors?',
    ['Green','Yellow','Red','Blue'],
    ['Yellow','Red']
)

st.write('Your selected:',options)

# DAY 12
# checkbox

st.header('st.checkbox')

st.write('What would you like to order ?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great!Here's some more 🍦")

if coffee:
    st.write("Okay,here's some coffee ☕")

if cola:
    st.write("Here you go 🥤")