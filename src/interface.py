import streamlit as st
from analysis import *
from visualizer import SentimentVisualizer

st.set_page_config(
    page_title = "😊 Auto Emoji 😁"
)

'''
# 😊 Auto Emoji 😁
#### Automatic Emoji placement using sentiment analysis
##### What is it?
Auto Emoji automatically supplements a given block of text with Emoji by inserting them in
various parts of the text. The choice of Emoji is based on the connotation of the proceeding
portion of the text. Auto Emoji is intended to be a demonstration project showing off the
basics of sentiment analysis on arbitrary text. Additional data visualizations are included
to demonstrate how a change in the input text affects the sentiment analysis algorithm's results.

##### How it Works
Auto Emoji accepts a block of input text from the user and splits up into "sections." Sections are
important substrings from the input text delimited by major punctuations such as periods, commas,
semicolons, etc. Each section is run through a sentiment analysis algorithm in order
to determine the section's polarity and subjectivity. Emoji are chosen based on both of these
parameters.

Negative sections are given sad or angry Emoji while positive sections are given happy or laughing
Emoji. The subjectivity is used to determine the intensity of the Emoji; the more subjective, the
more intense the Emoji. The rule-based sentiment analysis used by TextBlob is not perfect, and
sometimes Emoji choices may not accurately reflect the actual sentiment of a sentence section.
Nonetheless, Auto Emoji stands as an interesting interactive demonstration of sentiment analysis.

Auto Emoji is written in **Python** using **TextBlob**'s sentiment analysis algorithm. The interface
is written in Python using the **Streamlit** library.

##### Source Code and Contributing
Auto Emoji's open source code is hosted on GitHub. Feel free to fork and make a pull request if you
see something that can be approved.

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