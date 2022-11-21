import pandas as pd
import plotly.express as px
from load_data import load_data

class plotly_graphs:
    @staticmethod
    def graphfig():
        
        olympic_data = load_data.olympic_data
        
        # Get data for finland only
        olympic_data_finland = olympic_data.loc[olympic_data['NOC'] == 'FIN']



        # Get all rows where a player managed to score a medal
        olympic_data_finland_with_medals = olympic_data_finland[olympic_data_finland['Medal'].notna()]


        # Filter the rows into groups of sports, than sum the "Medals" column for each given sport
        medals_per_finland_sport = olympic_data_finland_with_medals.groupby('Sport')['Medal'].count()

        medals_per_finland_sport = medals_per_finland_sport.sort_values(ascending=False)

        # Take the top 5 sports with most medals scored
        medals_per_sport_top5_finland = medals_per_finland_sport[:5]

        fig = px.bar(
            x=medals_per_sport_top5_finland.index,
            y=medals_per_sport_top5_finland,
            title="Medal distribution across the olympic sports in finland",
            labels={
                'x': '',
                'y': 'Medals'
            }
        )
        
        return fig

