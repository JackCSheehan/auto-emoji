# 😊 Auto Emoji 😁
Automatic Emoji placement using sentiment analysis. Auto Emoji accepts a block of text from the user and adds Emoji throughout, using sentiment analysis to determine what Emoji to insert. You can try Auto Emoji out [here](https://github.com/JackCSheehan/auto-emoji).

The text is split into sections delimitated by a various types of punctuations. The Emoji choice is based on both the polarity and subjectivity of a particular section. Below is a chart showing which Emoji choices correspond to which polarity and subjectivity scores:

#### Tech Stack
- Python
- TextBlob (for both polarity and subjectivity)
- Streamlit (for the UI)
- Heroku (for web hosting)