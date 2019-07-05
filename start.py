def main():
    house_map()

def gameMenu():
    print('''
Text Game Main Menu
==========
It's 11 PM at night. Your house has been haunted with a Ghost. 
You are alive as of this time. 
If you encounter the Ghost, you are dead. Game over!
To come out alive you need to:
Find 3 items which will unlock the final item and proceed to the garage.
==========
Use "go" to navigate to the desired direction.
Use "get" to acquire the items
''')

def status(): #displays the status: Position & items acquired
    print('--->Current Status<---')
    print('You are in the ' + currentRoom)
    print('Items you have: ' + str(itemsAcquired))
    if "item" in rooms[currentRoom]:
        print('Viola there is your ' + rooms[currentRoom]['item'])
    print("*****************")
itemsAcquired = [] #To store the items found & acquired

rooms = {
            'Hall' : {
                'north' : 'Guest Room',
                'south' : 'Kitchen',
                'east'  : 'Dining Room',
                'west'  : 'Bedroom'
            },
            'Bedroom' : {
                'east' : 'Hall',
                'west' : 'Bathroom',
                'north' : 'Closet',
                'item' : 'keys'
            },
            'Closet' : {
                'south' : 'Bedroom'
            },
             'Bathroom' : {
                'east' : 'Hall'
                
            },
            'Guest Room' : {
                'south' : 'Hall'
            },
            'Kitchen' : {
                'north' : 'Hall',
                'east'  : 'Living Room',
                'south'  : 'Backyard',
                'item'  : 'phone'

            },
            'Backyard' : {
                'north' : 'Kitchen'

            },
            'Living Room' : {
                'west' : 'Kitchen',
                'north'  : 'Dining Room',
                'item'  : 'wallet'

            },
            'Dining Room' : {
                'west'  : 'Hall',
                'south' : 'Living Room',
                'east'  : 'Garage',
                'item'  : 'ghost'

            },
           'Garage' : {
                'west' : 'Dining Room'
            },

}
def house_map():
    try:
        north = rooms[currentRoom]['north']
    except:
        north = ""
    try:
        south = rooms[currentRoom]['south']
    except:
        south = ""
    try:
        east = rooms[currentRoom]['east']
    except:
        east = ""
    try:
        west = rooms[currentRoom]['west']
    except:
        west = ""
    n = "N"
    s = "S"
    vert_line = "|"
    hzt_line = "- W -- X -- E -"
    print(north.center(30))
    print("")
    print(vert_line.center(30))
    print(n.center(30))
    print(vert_line.center(30))
    print(west + hzt_line.center(30 - len(west) * 2) + east)
    print(vert_line.center(30))
    print(s.center(30))
    print(vert_line.center(30))
    print("")
    print(south.center(30))
    print("")
currentRoom = 'Hall' #Game starts in the Hall
gameMenu()

while True:
    
    house_map() #Display map 
    status()    #Display status
    move = ''
    while move == '':  
        move = input('>')

    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
    #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            itemsAcquired.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
            #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
            # Game Over if enter a room with Ghost
    if 'item' in rooms[currentRoom] and 'ghost' in rooms[currentRoom]['item']:
        print('OOPs the Ghost catches you and you are dead. GAME OVER!')
        break
  
    if currentRoom == 'Living Room' and 'keys' in itemsAcquired and 'phone' in itemsAcquired and 'wallet' in itemsAcquired:
        print('You have UNLOCKED a magical wand in one of the rooms. Proceed with caution but once you get the wand, the ghost cant eat you.')
        rooms['Guest Room'].update(item='wand') #Unlock wand in a mystery spot when all other items found
    if currentRoom == 'Hall' and 'keys' in itemsAcquired and 'phone' in itemsAcquired and 'wallet' in itemsAcquired and 'wand' in itemsAcquired:
        del rooms['Dining Room']['item']
    # The winning move. If you get the unlocked magical wand, and all 3 items (keys, phone and wallet) and enter Garage.
    if currentRoom == 'Garage' and 'keys' in itemsAcquired and 'phone' in itemsAcquired and 'wallet' in itemsAcquired and 'wand' in itemsAcquired:
        print('Wow! You win ! The Ghost was hiding in the Garage but since you unlocked and got the wand, the Ghost had no choice but to vanish ..!')
        break
if __name__ == "__main__":
    main()