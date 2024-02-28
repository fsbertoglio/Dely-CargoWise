import pandas as pd
from literals import DATA_SOURCE

class DataHandler():
    def __init__(self) -> None:
        self.data_frame = pd.read_csv(DATA_SOURCE, sep= ";")
        self.cities = self.data_frame.columns.to_list()
    def get_data_frame(self):
        return self.data_frame
    def get_city_list(self):
        return self.cities
    

                

        
