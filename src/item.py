class Item():
    def __init__(self, new_name: str, new_weight: float, new_quantity: int) -> None:
        self.name = new_name
        self.weight = new_weight
        self.quantity = new_quantity

    def get_item_weight(self) -> float:
        return self.weight
    
    def get_item_name(self) -> str:
        return self.name
    
    def get_item_quantity(self) -> int:
        return self.quantity

