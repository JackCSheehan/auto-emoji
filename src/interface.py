import streamlit as st
from analysis import *
from visualizer import SentimentVisualizer

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
    analyzer = Analyzer()


    output_text = analyzer.get_output_text(input_text)
    visualizer = SentimentVisualizer(analyzer.get_sentiment_data())
    st.write(output_text)

    '''
    ---
    #### Analysis Data
    ##### Input section sentiments
    '''
    st.table(visualizer.get_sentiment_dataframe())

    '''
    ##### Subjectivity v. Polarity
    '''
    st.altair_chart(visualizer.create_sentiment_scatter_plot(), use_container_width = True)

    '''
    ##### Emoji Distribution
    '''
    st.altair_chart(visualizer.create_emoji_distribution(), use_container_width = True)

    '''
    ##### Polarity v. Section
    '''
    st.altair_chart(visualizer.create_polarity_over_section_chart(), use_container_width = True)

    '''
    ##### Subjectivity v. Section
    '''
    st.altair_chart(visualizer.create_subjectivity_over_section_chart(), use_container_width = True)

    '''
    ##### Polarity and Subjectivity v. Section
    '''
    st.altair_chart(visualizer.create_subjectivity_and_polarity_over_section_chart(), use_container_width = True)