import streamlit as st
import json
import requests

st.title("Basic Calculator App")

# taking user inputs
option = st.selectbox("What operation You want to perform?", 
                     ('Addition', 'Subtraction', 'Multiplication', 'Division'))

st.write("")
st.write("Select the numbers from slider below")
x = st.slider("X", 0, 100, 20)
y = st.slider("Y", 0, 130, 10)

# converting the inputs into a json format
inputs = {"operation": option, "x": x, "y": y}

# when the user clicks on button it will fetch the API
if st.button('Calculate'):
    res = requests.post(url = "http://172.20.10.3:8000/calculate", data = json.dumps(inputs))

    st.subheader(f"Response from API = {res.text}")