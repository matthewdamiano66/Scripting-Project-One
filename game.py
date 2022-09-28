rooms = ['entrance', 'hallway', 'bedroom', 'basement', 'stairwell', 'Kitchen', 'trap room', 'exit']
items = ['flashlight', 'mirror', 'key', 'camera', 'cellphone', 'net']
# I should use this method instead but who the fuck cares lmao
# directions = ['north','south','east','west']
visited = []
inventory = []
villain = 'ghost'
line = "---------------------------------------------------------------------------------------------------------------"
name = input("Enter your name:")
data = input(name.lower().strip() + " " + "Do you want to play a game ? (Yes/No?)")
# ----------------------------------------------------------------------------------------------------------------------
# print(visited)
# Game starts
if data.lower().strip() == "yes":
    visited.append(rooms[0])
    print("Collect all 6 items to win \n")
    print(line)
    print("For weeks you've heard stories of miissing people entering the haunted Arley home.\n"
          "Following these stories you decide to investigae the home.\n")
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
        print(visited)
        print(inventory)
# ----------------------------------------------------------------------------------------------------------------------
        if data.strip().lower() == "kitchen":
            print("Entering the kitchen you use your flashlight to look around,you find a" + str(
                items[3]) + " " + "this may be helpful:")
            print("You have found 2 out of 6 items !")
            input("Hearing noises you rush out of the kitchen, where will you head next?")
        inventory.append(items[3])
        visited.append(rooms[5])
        print(inventory)
# ----------------------------------------------------------------------------------------------------------------------
if data.strip().lower() == "stairwell":
    print("Ascending the stairs with your flashlight, peering around for clues you suddenly rush back into the hallway")
# ----------------------------------------------------------------------------------------------------------------------
elif data.strip().lower() == "basement":
    print("You feel a presence fast approaching, the" + " " + villain + " " + "approaches too fast to react\n")
    print(line)
    print("Game Over," + " " + name + " " + "was never seen again!")
    visited.append(rooms[3])
    print("You visited:" + str(visited))
