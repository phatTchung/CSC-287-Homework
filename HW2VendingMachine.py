from abc import ABC, abstractmethod

class Product(ABC):
    """
    This is the main product class.
    Every product has a name and a way to be used (consume).
    """
    def __init__(self, product_name):
        """
        Set the name of the product.
        """
        self.product_name = product_name

    @abstractmethod
    def consume(self):
        """
        Show what happens when someone uses the product.
        (Must be written in the child class.)
        """
        pass


class Drink(Product):
    """
    A drink product.
    """
    def consume(self):
        """
        Print a message when you drink this item.
        """
        print(f"Yum, you drink the {self.product_name}.")


class Snack(Product):
    """
    A snack product.
    """
    def consume(self):
        """
        Print a message when you eat this item.
        """
        print(f"Yum, you eat the {self.product_name}.")


class EmptyProduct(Product):
    """
    This means the product is not available.
    """
    def __init__(self):
        """
        Give the empty product a name.
        """
        super().__init__("Empty")

    def consume(self):
        """
        Print a message when no product is found.
        """
        print("Sorry, this product is empty.")


class Slot:
    """
    One slot in the vending machine.
    It has a location, products, and a price.
    """
    def __init__(self, location, product_list, unit_price):
        """
        Make a slot with location, list of products, and price.
        """
        self.location = location
        self.products = product_list
        self.unit_price = unit_price

    def is_empty(self):
        """
        Check if the slot has no products.
        """
        return len(self.products) == 0

    def remove_product(self):
        """
        Take out one product from the slot.
        If no products, return an EmptyProduct.
        """
        if not self.is_empty():
            return self.products.pop(0)
        return EmptyProduct()


class VendingMachine:
    """
    The main vending machine that holds all slots.
    """
    def __init__(self):
        """
        Start with an empty vending machine.
        """
        self.slots = {}

    def stock_item(self, location, product_list, unit_price):
        """
        Add products to a slot in the machine.
        """
        self.slots[location] = Slot(location, product_list, unit_price)

    def print_inventory(self):
        """
        Show all slots, how many products, and their prices.
        """
        for loc, slot in self.slots.items():
            if slot.is_empty():
                print(f"Slot {loc}: Empty")
            else:
                product_name = slot.products[0].product_name
                print(f"Slot {loc}: {len(slot.products)} items of {product_name} at ${slot.unit_price} each")

    def purchase(self, location, money):
        """
        Buy a product from the machine.
        If not enough money or no product, return EmptyProduct.
        Otherwise, give the product and the change.
        """
        if location not in self.slots:
            return (EmptyProduct(), money)
        
        slot = self.slots[location]
        if slot.is_empty() or money < slot.unit_price:
            return (EmptyProduct(), money)
        
        product = slot.remove_product()
        change = round(money - slot.unit_price, 2)
        return (product, change)


if __name__ == "__main__":
    machine = VendingMachine()

    # Add products
    machine.stock_item("A1", [Drink("Coke"), Drink("Coke")], 1.50)
    machine.stock_item("B1", [Snack("Chips"), Snack("Chips")], 2.00)

    # Show what is inside
    machine.print_inventory()

    # Buy one drink
    product, change = machine.purchase("A1", 2.00)
    print(f"\nGot {product.product_name}, change: ${change}")
    product.consume()

    # Try to buy from empty slot
    product, change = machine.purchase("C1", 5.00)
    product.consume()
