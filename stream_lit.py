import streamlit as st
from calculator import calculate

# Title of the app
st.title("Basic calculator app 📱")

# Asking the user to select an operation
option = st.selectbox(
    'Please select the operation',
    ('addition', 'subtraction', 'multiplication', 'division')
)
st.write('You selected:', option)

# Ask the users for the integers
x = st.slider('Select your first integer?', 0, 130, 25)
st.write('You chose: ', x)
y = st.slider('Select your second integer?', 0, 130, 25)
st.write('You chose: ', y)


# converting the selected optins to a json format if passing as a payload to an api
inputs = {
    "operation": option,
    "x": x,
    "y": y
}

st.write("")

if st.button('Calculate'):
    res = calculate(option, x, y)

    st.metric(label="Result 👽", value=str(res))
