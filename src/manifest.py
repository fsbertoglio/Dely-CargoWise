from item import Item

class Manifest():
    def __init__(self) -> None:
        self.item_list = []
        self.item_names_list = []
        self.total_weight = 0
        self.total_item_quantity = 0

    def put_new_item(self, new_item: Item) -> None:
        self.item_list.append(new_item)
        self.item_names_list.append(new_item.get_item_name())
        self.total_weight += new_item.get_item_weight() * new_item.get_item_quantity()
        self.total_item_quantity += new_item.get_item_quantity()

    def get_manifest(self) -> list:
        return self.item_list
    
    def get_names_manifest(self) -> list:
        return self.item_names_list
    
    def get_weight(self) -> float:
        return self.total_weight
    
    def get_total_item_quantity(self) -> int:
        return self.total_item_quantity