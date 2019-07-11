play_name = raw_input("What will your username be? : ")

p = "welcome to Maze of doors will you mange to get to the end?..... " +play_name
print p


l = raw_input(" Lets start the game " + play_name)
print l

print ( "You must choose between 5 doors, Your choices are red, green, blue and purple as well as orange...choose in the right order inorder to gain access to the next!!")


inventory = []

while True:
    t = raw_input(" Choose a door color : ")
    answer = t
    if answer == "red" or answer == "r":
        print play_name + " has chosen the red door"
        answer1 = raw_input(" Do you want to open the door : ")
        if answer1 == "yes" or answer1 == "y":
            print (play_name + " have entered the Red door")
            reddoor_item = "purple key"
            answer1 = raw_input("Would you like to recieve the key ?")
            if answer1 == "yes" or answer1 == "y":
                print (play_name + " have recieved  " + reddoor_item)
                inventory.append(reddoor_item)
            elif answer1 == "no" or answer1 == "n":
                print " you may regret this....."
                continue



    elif answer == "blue" or answer == "b":
        print play_name + " has chosen the blue door"
        answer1 = raw_input("Do you want to open the door?:  ")
        if answer1 == "yes" or answer1 == "y":
            if "purple key" in inventory:
                print (play_name + " have entered the Blue door")
                reddoor_item = "Golden Key "
                answer1 = raw_input("Would you like to recieve the key ?")
                if answer1 == "yes" or answer1 == "y":
                    print (play_name + " Has recieved " + reddoor_item)
                    inventory.append(reddoor_item)
            elif answer1 == "no" or answer1 == "n":
                print " you will regret your decision"
                continue
            else:
                print " Sorry you do not have access"
                continue

    elif answer == "purple" or answer == "p":
        print play_name + " has chosen the purple door"
        answer1 = raw_input("Do you want to open the door?:  ")
        if answer1 == "yes" or answer1 == "y":
                if "purple key" in inventory:
                    print (play_name + " have entered the purple door")
                    reddoor_item = "rainbow Key "
                    answer1 = raw_input("Would you like to recieve the key ?")
                    if answer1 == "yes" or answer1 == "y":
                        print (play_name + " Has recieved " + reddoor_item)
                    inventory.append(reddoor_item)
                elif answer1 == "no" or answer1 == "n":
                    print " you will regret your decision"
                    continue
                else:
                    print " Sorry you do not have access"
                    continue


    elif answer == "orange" or answer == "o":
        print play_name + " has chosen the orange door"
        answer1 = raw_input("Do you want to open the door?:  ")
        if answer1 == "yes" or answer1 == "y":
                if "purple key" in inventory:
                    print (play_name + " have entered the purple door")
                    reddoor_item = "crystal Key "
                    answer1 = raw_input("Would you like to recieve the key ?")
                    if answer1 == "yes" or answer1 == "y":
                        print (play_name + " Has recieved " + reddoor_item)
                    inventory.append(reddoor_item)
                elif answer1 == "no" or answer1 == "n":
                    print " you will regret your decision"
                    continue
                else:
                    print " Sorry you do not have access"
                    continue

    elif answer == "green" or answer == "g":
        print play_name + " has chosen the Green door"
        answer1 = raw_input(" Do you want to enter the door?:  ")
        if answer1 == "yes" or answer1 == "y":
            print (play_name + " has entered the Green door")
            answer1 = raw_input("do you have all the keys thus far?: ")
            if answer1 == "yes" or answer1 =="y":
                print(" You have successfully reached the end of the MAze, you are now FREE!!!!!! ")
                break



































