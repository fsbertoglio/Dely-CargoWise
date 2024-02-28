from literals import TRUCK_DISTANCE_PRICE
from data_handler import DataHandler

class Gps():
    def __init__(self) -> None:
        self.dt = DataHandler()
        pass

    def get_distance(self, city1: str, city2: str) -> float:
        #print(self.cities)
        relative_distance = self.dt.get_data_frame().loc[self.dt.get_city_list().index(city2), city1]
        return relative_distance

    def get_travel_price(self, distance: float, truck_list: dict) -> float:
        total_cost = 0
        for truck_size in truck_list:
            total_cost += distance * truck_list[truck_size] * TRUCK_DISTANCE_PRICE[truck_size]
        return round(total_cost, 2)