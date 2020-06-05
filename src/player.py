# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room , inventory=[]):
        self.name= name
        self.current_room = current_room
        self.inventory = inventory 
        
    def __str__(self):
        return(f"{self.name}: {self.current_room}")
    
    def check_inventory(self):
            for item in self.inventory:
                output = f"\nInventory:\n{item.name}\n"
            print(output)
            
    def take_item(self, item):
        i = None
        for ite in self.current_room.items:
            if ite.name == item:
                i = ite
        self.inventory.append(i)
        self.current_room.items.remove(i)
        print(f'\nYou have picked up: {item} from {self.current_room}\n')
   
    def drop_item(self,item):
       i = None 
       for ite in self.inventory:
           if ite.name==item:
               i = ite
       self.inventory.remove(i)
       self.current_room.items.append(i)
       print(f'\n You have dropped {item}.') 

