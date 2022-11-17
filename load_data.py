import pandas as pd

class Load_data:
    @classmethod
    def load(cls):
        os_data = pd.read_csv("../Data/athlete_events.csv")
        return os_data