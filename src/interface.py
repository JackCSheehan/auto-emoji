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
Auto Emoji automatically supplements a given input string with Emoji by inserting them throughout
various parts of the text. The choice of Emoji is based on the connotation of the proceeding
portion of the text. Auto Emoji is intended to be a demonstration project showing off the
basics of sentiment analysis on an arbitrary input. Additional data visualizations are included
to demonstrate how a change in the input text affects the sentiment analysis algorithm's results.

##### How it Works
Auto Emoji accepts a block of input text from the user and splits it up into "sections." Sections are
important substrings from the input text delimited by major punctuations such as periods, commas,
semicolons, etc. Each section is run through a sentiment analysis algorithm in order
to determine the section's polarity and subjectivity.

Emoji are chosen based on both the polarity and subjectivity of a section and replace the delimiting puncations.
Polarity is measured on scale from -1 to 1 and subjectivity is measured from 0 to 1. Negative sections
are given sad or angry Emoji while positive sections are given happy or laughing Emoji.
The subjectivity is used to determine the intensity of the Emoji; the more subjective, the more intense
and expressive the Emoji. The rule-based sentiment analysis used by TextBlob is not perfect, and
sometimes Emoji choices may not accurately reflect the actual sentiment of a sentence section.
Nonetheless, Auto Emoji stands as a minimal and interactive demonstration of sentiment analysis.

Auto Emoji is written in Python using [TextBlob](https://github.com/sloria/TextBlob)'s sentiment analysis algorithm. The interface
is written in Python using the [Streamlit](https://github.com/streamlit/streamlit) library.

##### Source Code and Contributing
Auto Emoji's open source code is hosted on [GitHub](https://github.com/JackCSheehan/auto-emoji). Feel free to fork and make a pull request if you
see something that can be improved.

---
'''

'''
**Input text**
'''
input_text = st.text_area("Input some text to have Emoji added")
if st.button("Add Emoji") and len(input_text.strip()) > 0:
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
    ##### Input Section Sentiments
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

    # Only plot if there is sufficient data points
    if len(visualizer.get_sentiment_dataframe()) > 1:
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

    else:
        '''
        *Add more sentences to your input for even more visualizations!*
        '''