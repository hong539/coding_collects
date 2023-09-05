#good docs for dictionary in Python
#src01: https://docs.python.org/3.8/library/stdtypes.html#dict.update
#src02: https://www.w3schools.com/python/python_ref_dictionary.asp
#game inventory
#雷電將軍 角色突破素材
#Target
#破舊的刀鐔 36
#影打刀鐔 96
#名刀鐔 66
#Currnet
#202
#64
#9
#convertions
#影打刀鐔 = 破舊的刀鐔*3
#名刀鐔 = 影打刀鐔*3 = (破舊的刀鐔*3)*3 = 破舊的刀鐔*9

class Item:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
        # self.dict = {}
        # self.dict[self.name] = self.value        

class Inventory:
    def __init__(self) -> None:
        self.items = {}        
        
    def add_item(self, item):
        self.items.update({item.name: item.value})
        
    def remove_item(self, item):
        self.items.pop(item)

    def list_item_values(self):
        print(self.items.values())

    def count_items_all_values(self):
        pass

    def display_inventory(self):
        for item in self.items.items():
            print(item)
        

player_inventory01 = Inventory()
# print(type(Item("破舊的刀鐔", 202)))
player_inventory01.add_item(Item("破舊的刀鐔", 202))
player_inventory01.add_item(Item("影打刀鐔", 64))
player_inventory01.add_item(Item("名刀鐔", 9))
player_inventory01.display_inventory()
player_inventory01.remove_item("名刀鐔")
player_inventory01.display_inventory()
player_inventory01.list_item_values()