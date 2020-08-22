"""
Fun with dataclasses
--------------------
"""
from dataclasses import dataclass


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory.
    ---
    https://docs.python.org/3/library/dataclasses.html
    """

    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_value(self) -> float:
        """Calculate the total value of the inventory.
        ---
        """
        return self.unit_price * self.quantity_on_hand

    def show_dataclass_info(self) -> str:
        """Print info about the class to the terminal.
        ---
        """
        info = (
            f"Sample: {sample.name}\nPrice: {sample.unit_price}"
            f"\nInventory: {sample.quantity_on_hand}"
            f"\nTotal value of inventory: {sample.total_value()}"
        )
        return info


if __name__ == "__main__":
    sample = InventoryItem("Sling Shot", 50.99, 5000)
    print(sample.show_dataclass_info())
