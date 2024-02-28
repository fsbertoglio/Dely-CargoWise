from data_handler import DataHandler
from shipment import Shipment
from manifest import Manifest
from gps import Gps
from item import Item

class Controller:
    global_shipment_history = []
    data_handler = DataHandler()

    def __init__(self) -> None:
        self.shipment = Shipment()
        self.manifest = Manifest()
        pass

    def get_city_list(self):
        return self.data_handler.get_city_list()
    
    def add_item(self, name, weight, quantity) -> None:
        new_item = self.__create_item(name=name, weight=weight, quantity=quantity)
        self.manifest.put_new_item(new_item= new_item)
        self.shipment.set_manifest(self.manifest)

    def __create_item(self, name, weight, quantity) -> Item:
        new_item = Item(new_name= name, new_weight= weight, new_quantity= quantity)
        return new_item
    
    def get_manifest(self) -> list:
        return self.manifest.get_manifest()
    
    def get_names_manifest(self) -> list:
        return self.manifest.get_names_manifest()
    
    def get_distance(self, city1, city2) -> int:
        gps = Gps()
        return gps.get_distance(city1=city1, city2=city2)
    
    def get_total_distance(self) -> int:
        return self.shipment.get_total_distance()
    
    def set_origin(self, city) -> None:
        self.shipment.set_origin(city)
        self.shipment.add_destination(city)

    def add_destination(self, city) -> None:
        self.shipment.add_destination(city)
    
    def get_best_transport(self) -> dict:
        return self.shipment.get_best_transport()
    
    def get_total_weight(self) -> float:
        return self.shipment.get_total_weight()
    
    def _get_total_price(self) -> float:
        return self.shipment.get_price()
    
    def get_total_price(self, distance, small_trucks, medium_trucks, large_trucks) -> float:
        truck_list = {"small": small_trucks, "medium": medium_trucks, "large": large_trucks}
        gps = Gps()
        return gps.get_travel_price(distance=distance, truck_list=truck_list)
    
    def get_price_per_item(self) -> float:
        return self.shipment.get_price_per_item()
    
    def save_shipment(self) -> None:
        self.global_shipment_history.append(self.shipment)
    
    def get_shipment_list(self) -> list:
        output_list = []
        for ship in self.global_shipment_history:
            shipment:Shipment = ship
            route = shipment.get_route()
            total_price = shipment.get_price()
            average_cost_km = (shipment.get_price()/shipment.get_total_distance())
            products = shipment.manifest.get_names_manifest()
            total_distance = shipment.get_total_distance()
            transport_distribution = shipment.get_best_transport()
            total_items = shipment.manifest.get_total_item_quantity()
            new_dict = {"route": route,"total_price": total_price,"average_price+km": average_cost_km ,"products": products , "transport_distribution": transport_distribution, "total_items": total_items, "total_distance" : total_distance}
            output_list.append(new_dict)
        return output_list    
    