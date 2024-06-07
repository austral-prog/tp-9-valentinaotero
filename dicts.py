def create_inventory(items):
    
    inventory = dict ()
    value = 1
    for item in items:
        if item in inventory:
            inventory[item] += value
        else:
            inventory [item] = value
    return inventory


def add_items(inventory, items):
    value=1
    for item in items:
        if item in inventory: 
            inventory[item]= value + 1
        else:
            inventory[item]=value
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item]>0: 
            inventory[item]= inventory[item]-1
        elif item in inventory and inventory[item] <=0:
            inventory[item]=0

    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    else:
        inventory=inventory
    return inventory


def list_inventory(inventory):
   list = []
   for key, value in inventory.items()
        if value > 0:
            list.append((key,value))
    return list


