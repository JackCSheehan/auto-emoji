import streamlit as st
from analysis import *

'''
# 🔨 Auto Emoji 🔧
#### Automatic Emoji placement using sentiment analysis
---
'''

input_text = st.text_area("Input text")
if st.button("Add Emoji"):
    output_text = get_output_text(input_text)
    st.write(output_text)
