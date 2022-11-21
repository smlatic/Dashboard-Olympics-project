import pandas as pd

class load_data:
    
    olympic_data = None
    
    
    ###
    
    @classmethod
    def load(cls):
        cls.olympic_data = pd.read_csv("Data/athlete_events.csv")