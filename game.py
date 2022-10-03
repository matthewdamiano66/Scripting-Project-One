# rooms = 0            1           2           3         4           5           6           7
rooms = ['entrance', 'hallway', 'bedroom', 'basement', 'stairwell', 'Kitchen', 'trap room', 'exit']
# items =      0           1        2      3          4          5
items = ['flashlight', 'mirror', 'keys', 'camera', 'cellphone', 'net']
visited = []
inventory = []
villain = 'ghost'
line = "---------------------------------------------------------------------------------------------------------------"
# initial user data
name = input("Enter your name:")
data = input(name.lower().strip() + " " + "Do you want to play a game ? (Yes/No?)")
# ----------------------------------------------------------------------------------------------------------------------
# Game starts
if data.lower().strip() == "yes":
    visited.append(rooms[0])
    print("To play use input words that are surrounded by brackets like so: (answer)")
    print("Collect all 6 items  or make it to the exit to win  \n")
    print(line)
    print("For weeks you've heard stories of missing people entering the haunted Arley home.\n"
          "Following these stories you decide to investigate the home.\n")
    print(line)
    data = input("You enter a dark and dingy home standing in the " + " " + rooms[
        0] + " " + "you hear a strange noise do you head toward the (hallway) or (basement)?")
# ----------------------------------------------------------------------------------------------------------------------
elif data.lower().strip() == "no":
    print("Ok" + " " + name.lower().strip() + "," + " goodbye for now")
# ----------------------------------------------------------------------------------------------------------------------
else:
    data = input(name.lower().strip() + " " + "Do you want to play a game ? (Yes) or (No)?")
    print("Ok" + " " + name.lower().strip() + "," + " goodbye for now")
    # this is all working now
# ----------------------------------------------------------------------------------------------------------------------
if data.strip().lower() == "hallway":
    print(line)
    inventory.append(items[0])
    data = input(
        "Entering the hallway you find a " + " " + str(items[0]) + " " +
        "But hearing footsteps you must quickly decide where to go next ? the (Kitchen)? or the (stairwell)?\n")
    visited.append(rooms[1])
# ----------------------------------------------------------------------------------------------------------------------
# first possible game over not based on simply declining to play the game
if data.strip().lower() == "basement":
    print(line)
    print("You feel a presence fast approaching, the" + " " + villain + " " + "approaches too fast to react\n")
    print("Game Over," + " " + name + " " + "was never seen again!")
    visited.append(rooms[3])
# ----------------------------------------------------------------------------------------------------------------------
if data.strip().lower() == "kitchen":
    print(line)
    print("Entering the kitchen you use your flashlight to look around,you find a" + str(
        items[3]) + " " + "this may be helpful:")
    inventory.append(items[3])
    print("You have found " + str(len(inventory)) + " out of 6 items !")
    data = input("Hearing noises you rush out of the kitchen, where will you head next (Stairwell) or (basement) ?")
    visited.append(rooms[5])
# ----------------------------------------------------------------------------------------------------------------------
if data.strip().lower() == "stairwell":
    print(line)
    visited.append(rooms[4])
    print("You climb the stairs, noticing the state of the hallway you find yourself in you descend quickly back to "
          "whence you came.\n")
    inventory.append(items[4])
    print("You have found " + str(len(inventory)) + " out of 6 items !")
    print(line)
    data = input("Back where you started where will you head next ?\n to the (kitchen)? or downward to the (basement)?")
    if data == "basement":
        inventory.append(items[1])
        print("While is the basement using your flashlight you find a mirror, how could this be helpful you think?\n"
              "")
    # ----------------------------------------------------------------------------------------------------------------------
    if data.strip().lower() == "kitchen":
        print(line)
        print("Entering the kitchen you use your flashlight to look around,you find a" + str(
            items[3]) + " " + "this may be helpful:")
        inventory.append(items[3])
        print("You have found " + str(len(inventory)) + " out of 6 items !")
        print("Standing in the kitchen too long, you feel the floor creek beneath you\n")
        print("Catching your breath for too long you fall through the floor finding yourself in a trap room\n")
        visited.append(rooms[5])
        visited.append(rooms[6])
        print("In this room you find a net, seeing this you think you could use it to slow the " + villain)
        inventory.append(items[5])
        print("You have found " + str(len(inventory)) + " out of 6 items !")
        data = input("Using your flashlight to find the door, you have to decide to (stay) and wait, or (continue) "
                     "exploring, what will you do ?")
    # ----------------------------------------------------------------------------------------------------------------------
    if data.strip().lower() == "continue":
        inventory.append(items[2])
        print(line)
        visited.append(rooms[2])
        print("you continue forward until you find a bedroom\n")
        print("Entering the bedroom you use your flashlight to find clues\n")
        print("You find a set of keys on an antique spider web covered dresser\n")
        print("You have found " + str(len(inventory)) + " out of 6 items !")
        data = input("Shinning your light through the now open door, you believe you can see and exit do you ("
                     "stay) where you are or (explore)")
        if data.strip().lower() == "explore":
            print(line)
            data = input(
                "Making your way toward the exit you're suddenly stopped by the" + villain + " " + "Will you ("
                                                                                                   "attack) "
                                                                                                   "or (run)")
            print(line)
            if data.strip().lower() == "attack":
                print(line)
                visited.append(rooms[7])
                print("You throw your net over the ghost and taking your camera unmask the ghost while snapping a "
                      "photo")
                print("With all of the evidence you've found you make a break for the exit")
                print("you safely escape out the door and use your evidence to apprehend the" + " " + villain)
                print(line)
                print("Game over," + " " + name + " " + "you've won!")
# ----------------------------------------------------------------------------------------------------------------------
    if data.strip().lower() == "stay":
        print(line)
        print(
            "You decided to stay, you wait too long and are found by the " + villain + " and are never seen again")
        print("Game Over" + name + "Better luck nex time!")
# ----------------------------------------------------------------------------------------------------------------------
if len(inventory) == len(items):
    print(line)
    print("Congratulations" + " " + name + " " + "you found all the items" + "!")
# ----------------------------------------------------------------------------------------------------------------------
if len(visited) == 8:
    print(line)
    print("Congratulations" + " " + name + " " + "you visited all eight rooms" + "!")
