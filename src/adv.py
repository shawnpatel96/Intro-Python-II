from room import Room
from player import Player
from item import Item
# Declare all the rooms
item={
   '7.62': Item('7.62x51',"5.56×45mm NATO Ammo Box"),
   'SA-58':Item('SA-58',"DS Arms SA-58 7.62x51"),
   'Salewa':Item('Salewa',"Salewa FIRST AID KIT"),
   'AKM':Item('AKM',"Base Model AK, chambered in 7.62x39."),
   'SDN-6':Item('SDN-6',"AAC 762 SDN-6 7.62x51 Sound Suppressor"),
   'Propital': Item('Propital',"Military issued drug. It stimulates regeneration processes by increasing the biosynthesis of purine and pyrimidine bases. Increases metabolism, health and vitality.")
}
room = {    #<---Game Map 
      #Key      #Value(room)
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('SA-58','DS Arms SA-58 7.62x51')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                        passages run north and east.""", [Item('7.62',"5.56×45mm NATO Ammo Box")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                        into the darkness. Ahead to the north, a light flickers in
                        the distance, but there is no way across the chasm.""",[Item('Salewa',"Salewa FIRST AID KIT")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                        to north. The smell of gold permeates the air.""",[Item('SDN-6',"AAC 762 SDN-6 7.62x51 Sound Suppressor")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                        chamber! Sadly, it has already been completely emptied by
                        earlier adventurers. The only exit is to the south.""",[Item('Propital',"Military issued drug. It stimulates regeneration processes by increasing the biosynthesis of purine and pyrimidine bases. Increases metabolism, health and   vitality.")]),
}


# Link rooms together, making the game map

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

new_player = Player("PMC",room['outside'])   # <-- new player here

command = ""
current_terminal_room= new_player.current_room
print("\nMovement Keys: 'w', 's', 'a', 'd'\n>> Press 'q' to quit\n")

print(f"Hello {new_player.name}, your current position is: {new_player.current_room}")

while command !="q":
    command = str(input("\nType a command: "))

    if command == "w":
            new_player.current_room = new_player.current_room.n_to
            print(f"\nYou have entered the {new_player.current_room}")
        
    if command == "s":
            new_player.current_room = new_player.current_room.s_to
            print(f"\nYou have entered the {new_player.current_room}")
  
    if command == "d":
            if new_player.current_room.w_to:
                new_player.current_room = new_player.current_room.w_to
                print(f"\nYou have entered the {new_player.current_room}")
                
    if command == "a":
            new_player.current_room = new_player.current_room.e_to
            print(f"\nYou have entered the {new_player.current_room}")

    if command == 'search':
            new_player.current_room.search()

    if command == 'take':
        item_to_add = input('What Item would you like to take? Item: ')
        new_player.take_item(item_to_add)

    if command =='drop':
           new_player.check_inventory()
           item_remove = input('What would you like to drop? Item: ')
           new_player.drop_item(item_remove)

    if command == 'check inventory':
            new_player.check_inventory()   

    if command == 'Add Room Item':
            room_add = input('What item would you like to add to this room? Item:')
            current_terminal_room.add_item(room_add)


    if command == "q":
        print("Later Iroh")
        exit()

        