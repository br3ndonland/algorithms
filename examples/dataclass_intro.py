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

    def print_info(self):
        """Print info about the class to the terminal.
        ---
        """
        print(
            f"Sample: {sample.name}\nPrice: {sample.unit_price}",
            f"\nInventory: {sample.quantity_on_hand}",
            f"\nTotal value of inventory: {sample.total_value()}",
        )


if __name__ == "__main__":
    sample = InventoryItem("Sling Shot", 50.99, 5000)
    sample.print_info()
