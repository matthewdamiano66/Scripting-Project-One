# rooms = 0            1           2           3         4           5           6           7
rooms = ['entrance', 'hallway', 'bedroom', 'basement', 'stairwell', 'Kitchen', 'trap room', 'exit']
# items =      0           1        2      3          4          5
items = ['flashlight', 'mirror', 'keys', 'camera', 'cellphone', 'net']
# I should use this method instead but who the fuck cares lmao
# directions = ['north','south','east','west']
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
    print("Collect all 6 items to win \n")
    print(line)
    print("For weeks you've heard stories of missing people entering the haunted Arley home.\n"
          "Following these stories you decide to investigate the home.\n")
    print(line)
    data = input("You enter a dark and dingy home standing in the " + " " + rooms[
        0] + " " + "you hear a strange noise do you head toward the hallway or basement?")
# ----------------------------------------------------------------------------------------------------------------------
elif data.lower().strip() == "no":
    print("Ok" + " " + name.lower().strip() + "," + " goodbye for now")
# ----------------------------------------------------------------------------------------------------------------------
else:
    data = input(name.lower().strip() + " " + "Do you want to play a game ? (Yes/No?)")
    print("Ok" + " " + name.lower().strip() + "," + " goodbye for now")
    # this is all working now
# ----------------------------------------------------------------------------------------------------------------------
if data.strip().lower() == "hallway":
    data = input(
        "you've entered the hallway but hear foot steps you find a " + " " + items[
            0] + " " + "where do you go next ? the Kitchen? or the stairwell?\n")
    inventory.append(items[0])
    visited.append(rooms[1])
# ----------------------------------------------------------------------------------------------------------------------
# first possible game over not based on simply declining to play the game
if data.strip().lower() == "basement":
    print("You feel a presence fast approaching, the" + " " + villain + " " + "approaches too fast to react\n")
    print(line)
    print("Game Over," + " " + name + " " + "was never seen again!")
    visited.append(rooms[3])
    print("You visited:" + str(visited))
    # ----------------------------------------------------------------------------------------------------------------------
    if data.strip().lower() == "kitchen":
        print("Entering the kitchen you use your flashlight to look around,you find a" + str(
            items[3]) + " " + "this may be helpful:")
        inventory.append(items[3])
        print("You have found "+str(len(inventory))+" out of 6 items !")
        data = input("Hearing noises you rush out of the kitchen, where will you head next?")
        visited.append(rooms[5])
# ----------------------------------------------------------------------------------------------------------------------
if data.strip().lower() == "stairwell":
    visited.append(rooms[4])
    print("You climb the stairs, noticing the state of the hallway you find yourself in you descend quickly back to "
          "whence you came.\n")
    print("Looking around quickly you find a set of keys along the stairs where could they lead ?\n")
    inventory.append(items[2])
    print("You have found " + str(len(inventory)) + " out of 6 items !")
    print(line)
    data = input("Back where you started where will you head next ?\n to the kitchen? or downward to the basement?")
    if data == "basement":
        inventory.append(items[1])
        print("While is the basement using your flashlight you find a mirror, how could this be helpful you think?\n"
              "")
    if data.strip().lower() == "kitchen":
        print("Entering the kitchen you use your flashlight to look around,you find a" + str(
            items[3]) + " " + "this may be helpful:")
        inventory.append(items[3])
        print("You have found " + str(len(inventory)) + " out of 6 items !")
        data = input("idk man plot is hard")
        visited.append(rooms[5])
# ----------------------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------------------
