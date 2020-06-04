from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

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
# Welcome Message
# Make a new player object that is currently in the 'outside' room.
print("Welcome to The Adventure Game!")
print("Please create a player to continue")
startPosition = room['outside']

username = input("Player Name: ")
user = Player(str(username), startPosition)
print(f"Welcome {user.name}")

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
playGame = input("Please press yes (y) to continue or (q) to quit:")

if playGame.lower().strip() == "y":
        print("Welcome to the Adventure Game! Move foward to begin the treasure hunt!")

userInput = input(f"You're currently {user.current_room} press (n) to move foward:")

if userInput.lower().strip() == "n":
    user.current_room = user.current_room.n_to
    print(user)

elif playGame.lower().strip() == "q":
        print("Game exiting")
        exit(0)
