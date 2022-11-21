import pandas as pd
import plotly.express as px
from Load_data import Load_data as ld

class Finland:
    
    olympic_data_finland = None
    olympic_data_finland_with_medals = None
    olympic_data_finland_unique_players = None
    
    @classmethod
    def initialize(cls):
        cls.olympic_data_finland = ld.olympic_data.loc[ld.olympic_data['NOC'] == 'FIN']
        cls.olympic_data_finland_with_medals = cls.olympic_data_finland[cls.olympic_data_finland['Medal'].notna()]
        
        # Remove duplicate players (by looking at name hash)
        cls.olympic_data_finland_unique_players = cls.olympic_data_finland.drop_duplicates('Name')
    
    @staticmethod
    def medal_distribution_sports_finland():

        # Filter the rows into groups of sports, than sum the "Medals" column for each given sport
        medals_per_finland_sport = Finland.olympic_data_finland_with_medals.groupby('Sport')['Medal'].count()

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
    
    
    @staticmethod
    def medal_distribution_olympics_finland():
        # Filter the rows into groups of games, than sum the "Medals" column for each given game
        medals_per_os = Finland.olympic_data_finland_with_medals.groupby('Games')['Medal'].count()

        medals_per_os.index = medals_per_os.index.sort_values()

        fig = px.bar(
            x=medals_per_os.index,
            y=medals_per_os,
            title="Medal distribution across the olympic games in finland",
            labels={
                'x': '',
                'y': 'Medals'
            }
        )

        return fig
    
    
    @staticmethod
    def age_distribution_olympics_finland():
        fig = px.histogram(
            data_frame=Finland.olympic_data_finland,
            x="Age",
            title="Age distribution across the OS contenders"
        )

        return fig
    
    @staticmethod
    def height_distribution_olympics_finland():
        fig = px.histogram(
            data_frame=Finland.olympic_data_finland_unique_players,
            x="Height",
            title="height distribution"
        )

        return fig
    
    @staticmethod
    def weight_distribution_olympics_finland():
        # Get a series of the value counts of the ages
        olympic_data_finland_weights = Finland.olympic_data_finland_unique_players['Weight'].value_counts()

        olympic_data_finland_weights = olympic_data_finland_weights.sort_values(ascending=False)


        fig = px.histogram(
            x=olympic_data_finland_weights.index,
            y=olympic_data_finland_weights,
            title="Weight distribution",
            
            labels={
                'x': 'Kg',
                'y': 'Number of people'
            }
        )

        fig.update_layout(yaxis_title="Number of people")
        return fig
    
    
class General:
    pass