# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player
from item import Item
class Room: 
    def __init__(self, name, description, items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.items=items
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        
    def __str__(self):
        return f"{self.name}, {self.description}"

    def search(self):
        if len(self.items) == 0:
             print("\nYou've looted everything, move on before a 5 man PMC group comes and rolls you.\n")  
        else:
            output = f"You look inside the wooden box, inside you find: "
            for i in self.items:
                output += f"\n{i.name} - {i.description}"
            print(output)

    def add_item(self, item):
        self.items.append(item)
           
