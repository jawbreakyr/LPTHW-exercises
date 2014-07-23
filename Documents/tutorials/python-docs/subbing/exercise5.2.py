# Problem 1
players_inventory = {"apples": 2, "sleeping bag": 1, "torch": 5}
print players_inventory
# Problem 2
players_inventory["apples"]=5
print players_inventory
# Problem 3
del players_inventory["sleeping bag"]
print players_inventory
# Problem 4
def delete_item_from_inventory(inventory_dict, item_key):
	del inventory_dict[item_key]

delete_item_from_inventory(players_inventory, "apples")
print players_inventory