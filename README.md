# 😊 Auto Emoji 😁
Automatic Emoji placement using sentiment analysis. Auto Emoji accepts a block of text from the user and adds Emoji throughout, using sentiment analysis to determine what Emoji to insert. You can try Auto Emoji out [here](https://auto-emoji-demo.herokuapp.com/).

The text is split into sections delimited by various types of punctuations. The Emoji choice is based on both the polarity and subjectivity of a particular section. Below is a chart showing which Emoji choices correspond to which polarity and subjectivity scores:

![Emoji chart](https://raw.githubusercontent.com/JackCSheehan/auto-emoji/main/.github/chart.png?raw=true)

A more positive polarity corresponds to a more positive Emoji expression while a more negative polarity corresponds to a more negative Emoji expression. The intensity of the Emoji emotions increase as the subjectivity increases, representing the more opinionated nature of input with a higher subjectivity score. Emoji corresponding to higher subjectivity scores also tend to have more extreme neutral expressions.

The choice of the Emoji used to represent each polarity and subjectivity is a fairly subjective process. I simply did my best to find Emoji which I felt best fit in each category.

### Tech Stack
- [Python](https://www.python.org/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/) (for both polarity and subjectivity analysis)
- [Streamlit](https://streamlit.io/) (for the UI)
- [Altair](https://altair-viz.github.io/) (for all data visualizations)
- [Heroku](https://www.heroku.com/) (for web hosting)
