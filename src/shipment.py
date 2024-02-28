from manifest import Manifest
from gps import Gps
from literals import TRUCK_WEIGTH_CAPACITY

class Shipment():
    def __init__(self) -> None:
        self.price:float
        self.manifest = Manifest
        self.list_of_trucks = {}
        self.total_weight:float
        self.origin: str
        self.route = {}
        self.total_distance = 0
        self.gps = Gps()
        self.price_per_item:float
    
    def get_best_transport(self) -> dict:
        weight = self.total_weight
        truck_distribution = {}
        for size in reversed(TRUCK_WEIGTH_CAPACITY):
            truck_distribution[size] = 0
            if weight >= TRUCK_WEIGTH_CAPACITY[size]:
                truck_distribution[size] += weight//TRUCK_WEIGTH_CAPACITY[size]
                weight -= truck_distribution[size] * TRUCK_WEIGTH_CAPACITY[size]
        if weight > 0:
            truck_distribution["small"] += 1
        self.list_of_trucks = truck_distribution
        return self.list_of_trucks
    
    def set_manifest(self, new_manifest: Manifest) -> None:
        self.manifest = new_manifest
        self.total_weight = new_manifest.get_weight()


    def add_destination(self, new_destination: str) -> None:
        if len(self.route) != 0:
            new_distance = self.gps.get_distance(self.__last_destination(), new_destination)
        else: 
            new_distance = 0
        self.route[new_destination] = new_distance
        self.total_distance += new_distance

        print(self.route) #####
    
    def set_origin(self, origin:str) -> None:
        if len(self.route) == 0:
            self.origin = origin
            self.route[origin] = 0
            
    def get_origin(self) -> str:
        return self.origin

    def __last_destination(self) -> str:
        return list(self.route)[-1]
    
    def get_total_distance(self) -> int:
        return int(self.total_distance)
    
    def get_price(self) -> float:
        self.price = self.gps.get_travel_price(distance= self.total_distance, truck_list= self.list_of_trucks)
        return self.price
    
    def get_price_per_item(self) -> float:
        return round(self.get_price() / self.manifest.get_total_item_quantity(), 2)
        
    def get_total_weight(self) -> float:
        return self.total_weight
    
    def get_route(self) -> dict:
        return self.route
    
