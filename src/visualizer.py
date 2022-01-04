from altair.vegalite.v4.schema.channels import Tooltip
import pandas as pd
import altair as alt

# Class responsible for generating visualizations and organizations of sentiment data
class SentimentVisualizer:
    def __init__(self, sentiment_data):
        self.sentiment_dataframe = pd.DataFrame(sentiment_data, columns = ["Text", "Chosen Emoji", "Polarity", "Subjectivity"])

    def get_sentiment_dataframe(self):
        return self.sentiment_dataframe

    # Generates an Altair heatmap plot visualizing the polarity and subjectivity map
    def create_sentiment_scatter_plot(self):
        return alt.Chart(self.sentiment_dataframe).mark_circle(color = "orange", size = 100).encode(
            x = alt.X("Polarity", scale = alt.Scale(domain = (-1, 1)), axis = alt.Axis(tickMinStep = .33)),
            y = alt.Y("Subjectivity", scale = alt.Scale(domain = (0, 1)), axis = alt.Axis(tickMinStep = .33)),
            tooltip = ["Subjectivity", "Polarity", "Chosen Emoji"],
        ).configure_view(
            strokeOpacity = 0
        )

    # Generates Altair pie chart showing distribution of Emoji choices
    def create_emoji_distribution(self):
        return alt.Chart(self.sentiment_dataframe).mark_arc().encode(
            theta = "count(Chosen Emoji)",
            color = alt.Color("Chosen Emoji"),
            tooltip = ["Chosen Emoji", "count(Chosen Emoji)"]
        ).configure_view(
            strokeOpacity = 0
        )

    # Generates Altair line graph which shows how the polarity changes throughout the given text.
    # setStrokeOpacity is used to determine whether or not to remove the border
    def create_polarity_over_section_chart(self, setStrokeOpacity = True):
        chart = alt.Chart(self.sentiment_dataframe.reset_index()).mark_line().encode(
            x = alt.X("index", axis = alt.Axis(title = "Section", tickMinStep = 1)),
            y = "Polarity",
            tooltip = ["Text", "Polarity"],
        ).interactive()

        if setStrokeOpacity:
            chart = chart.configure_view(strokeOpacity = 0)

        return chart

    # Generates Altair line graph which shows how the subjectivity changes throughout the given text
    # setStrokeOpacity is used to determine whether or not to remove the border
    def create_subjectivity_over_section_chart(self, setStrokeOpacity = True):
        chart =  alt.Chart(self.sentiment_dataframe.reset_index()).mark_line(color = "orange").encode(
            x = alt.X("index", axis = alt.Axis(title = "Section", tickMinStep = 1)),
            y = "Subjectivity",
            tooltip = ["Text", "Subjectivity"],
        ).interactive()

        if setStrokeOpacity:
            chart = chart.configure_view(strokeOpacity = 0)

        return chart
    
    # Layers both of the data over section graphs into one
    def create_subjectivity_and_polarity_over_section_chart(self):
        return alt.layer(
            self.create_polarity_over_section_chart(False),
            self.create_subjectivity_over_section_chart(False)
        ).configure_view(
            strokeOpacity = 0
        )