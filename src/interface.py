import streamlit as st
from analysis import *

'''
# 🔨 Auto Emoji 🔧
#### Automatic Emoji placement using sentiment analysis
---
'''

'''
**Input text**
'''
input_text = st.text_area("Input some text to have Emoji added")
if st.button("Add Emoji"):
    '''
    ---
    **Output text**
    '''
    sentiment_data, output_text = get_output_text(input_text)
    st.write(output_text)

    '''
    ---
    #### Analysis Data
    ##### Input section sentiments
    '''
    st.table(sentiment_data)

    '''
    ##### Emoji Sentiment Heatmap
    '''

    '''
    ##### Emoji Distribution
    '''

    '''
    ##### Polarity/Section
    '''

    '''
    ##### Subjectivity/Section
    '''
