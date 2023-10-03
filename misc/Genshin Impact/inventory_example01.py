class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_inventory(self):
        for item in self.items:
            print(item.name + ": " + item.description)

inventory = Inventory()
inventory.add_item(Item("Sword", "A sharp sword"))
inventory.add_item(Item("Shield", "A sturdy shield"))
inventory.print_inventory()