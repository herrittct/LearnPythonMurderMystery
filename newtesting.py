#New testing
#Murder Mystery Game
#Started 10/9/2018
#exercise 36
import random
import math
#This is a murder mystery text game created for the Learn Python the Hard Way Exercise 36
def error(function):
    print(f"There is an error in {function}.")
# Creates an empty dictionary to be filled with Victim information, will recieve arguments including gender, age, noteriety, status, and looks
victim_attributes = {}

# Function to determine the victim attributes to be used in the intro function
def victim():
    gender = ["man", "woman"]
    age = ["young", "old"]
    noteriety = ["well known", "little known"]
    status = ["bad", "good"]
    looks_female = ["beautiful", "normal"]
    looks_male = ["handsome", "normal"]
    if random.choice(gender) == "man":
        looks = random.choice(looks_male)
    else:
        looks = random.choice(looks_female)
    attributes = ["gender", "age", "noteriety", "status", "looks"]
    for i in attributes:
        victim_attributes["gender"] = random.choice(gender)
        victim_attributes["age"] = random.choice(age)
        victim_attributes["noteriety"] = random.choice(noteriety)
        victim_attributes["status"] = random.choice(status)
        victim_attributes["looks"] = looks

# calls the victim function to run
victim()
# prints the selected victim attributes, will need to be removed later
#print(victim_attributes)

# Creates an empty dictionary to be filled with suspect attributes, will recieve name, weapon, random number, clue1, clue 2, and final evidence
suspect_attributes = {}

#function to determine the suspect and their associated attributes
def suspect():
    attribute = ["Name", "Weapon", "Random Number", "Clue 1", "Clue 2", "Final Evidence"]
    bank_robber = ["Bank Robber","hand gun", random.randint(1,17), "shell casing", "holster", "pile of bank notes with blood"]
    bartender = ["Bartender","200 proof bottle of booze", random.randint(1,17), "shot glass", "lime wedges", "personalized flask"]
    mailperson = ["Mailperson", "letter opener", random.randint(1,17), "stamps", "post office missed you notice", " stack of bloody letters in a letterbag"]
    lover = ["Lover","necklace", random.randint(1,17), "locket", "jewlery store reciept", "photo and card"]
    boyfriend = ["Boyfriend","glass bottle", random.randint(1,17), "cork", "bottle opener", "wine soaked bloody shirt"]
    girlfriend = ["girlfriend","glass bottle", random.randint(1,17), "cork", "bottle opener", "wine soaked bloody shirt"]
    husband = ["husband","bottle of poison", random.randint(1,17), "pill bottle", "paper perscription", "google search for \' how to poison wife \'"]
    wife = ["wife","bottle of poison", random.randint(1,17), "pill bottle", "paper perscription", "google search for \'how to poison husband\'"]
    vagrant = ["vagrant","switch blade", random.randint(1,17), "brass knuckles", "soap in a sock", "stolen wallet with victims drivers license"]
    vagrantess = ["vagreantess","switch blade", random.randint(1,17), "brass knuckles", "soap in a sock", "stolen wallet with victims drivers license"]
    bear = ["bear","a set of teeth", random.randint(1,17), "tuft of fur", " set of tracks", "bloody leg"]
    mountain_lion = ["Mountain lion","a set of teeth", random.randint(1,17), "tuft of fur", "set of tracks", "bloody leg"]
    moose = ["Moose","broken horn tip", random.randint(1,17), "tuft of fur", "set of tracks", "bruised arm"]
    suspects = [bank_robber, bartender, mailperson, lover, boyfriend, girlfriend, husband, wife, vagrant, vagrantess, bear, mountain_lion, moose]
    suspect_chosen = random.choice(suspects)
    z = 0
    for i in attribute:
        x = i
        suspect_attributes[x] = suspect_chosen[z]
        z += 1

#Calls the function to determine the suspects attributes
suspect()
#prints the suspect attributes, will need to be removed later
#print(suspect_attributes)


def determine_items():
    items_needed = {}
    items = ["weapon", "Clue 1", "Clue 2", "Final Evidence"]
    possible_locations = [1.1,1.2,1.3,1.4,2.1,2.2,2.3,2.4,3.1,3.2,3.3,3.4,4.1,4.2,4.3,4.4]
    for i in items:
        exact = random.choice(possible_locations)
        possible_locations.remove(exact)
        items_needed[i] = exact
    return items_needed

items_needed = determine_items()
#print(items_needed)

river = ["river","Water", "Rocks", "Trees", "Waters Edge", "Small path to forest clearing", 1 ]
cabin = ["cabin","bed", "desk", "cupbord", "porch", "False floor to tunnel", 2]
hiking_path = ["hiking path", "Big Curve", "Picnic Table", "Parking Lot", "Summit", "Small cave enterance", 3]
campsite = ["campsite","Woodpile", "Rock ring", "In the ashes", "Stump Chairs", "Hole underneath the woodpile", 4]

place_choices = {"Cabin": cabin, "Hiking Path" : hiking_path, "Campsite": campsite,  "River": river}
#print(place_choices)

found_weapon = False
found_clue1 = False
found_clue2 = False
found_final_evidence = False

def intro():
    city = ["Chicago", "New York", "Ottawa", "London", "Fort Collins"]
    #For the game it will request the participants name
    detective_name = input("What is your name?  ")
    #detective_name = "Cameron"
    print("""\n The victim was an {0} {1}, but {2} and regarded as a {3} person, while looking extremely {4} for these parts.""".format(victim_attributes['age'],victim_attributes['gender'],victim_attributes['noteriety'],victim_attributes['status'],victim_attributes['looks']))
    print(f"""\n The detective arrived by train from {random.choice(city)} and was well known for solving murders within a day.
    Detective {detective_name} was here to solve the latest of the towns {random.randint(2,17)} murders in the last two months.""")
    headed()
    return detective_name

def headed():
    print(f"""

    Now that you are here you have some choices, where would you like to go?
    Head to the river
    Head to the cabin
    Head to the hiking path
    Head to the campsite

    """)
    choosen_destination = str(input(">>>   "))
    if choosen_destination == "river":
        #print(place_choices["River"])
        locations(place_choices["River"])
    elif choosen_destination == "cabin":
        #print(place_choices["Cabin"])
        locations(place_choices["Cabin"])
    elif choosen_destination == "hiking path":
        #print(place_choices["Hiking Path"])
        locations(place_choices["Hiking Path"])
    elif choosen_destination == "campsite":
        #print(place_choices["Campsite"])
        locations(place_choices["Campsite"])
    else:
        print("Sorry I am kinda broken")
        headed()

def keep_searching(upper_location,previous_location, location_selected):
    #remove previous location from options to travel to and send player back to the upper location to keep searching if they want to
    #print("Keep Searching")
    locations(location_selected)

def locations(location_selected):
    print(f"""

Current status:
Weapon          {found_weapon}
Clue 1          {found_clue1}
Clue 2          {found_clue2}
Final Evidence  {found_final_evidence}
""")
    found_all = found_weapon and found_clue1 and found_clue2 and found_final_evidence
    if found_all == True:
        endgame()
    else:
        #print(location_selected)
        print("You arrive at the {0} and look around.  There seem to be a couple main options to look for clues.".format(location_selected[0]))
        location_count = 4
        y = 1
        while y <= location_count:
            print(f"You can search the {location_selected[y]}")
            y += 1
        print("Or go back")
        sub_location = str(input("Where do you want to search?   "))

        if str.lower(sub_location) == str.lower(location_selected[1]):
            print(f"You search the {location_selected[1]}\n")
            print("Do you find something interesting?")
            find_something(0.1, location_selected)

        elif str.lower(sub_location) == str.lower(location_selected[2]):
            print(f"You search the {location_selected[2]}\n")
            print("Do you find something interesting?\n")
            find_something(0.2, location_selected)

        elif str.lower(sub_location) == str.lower(location_selected[3]):
            print(f"You search the {location_selected[3]}\n")
            print("Do you find something interesting?\n")
            find_something(0.3, location_selected)

        elif str.lower(sub_location) == str.lower(location_selected[4]):
            print(f"You search the {location_selected[4]}\n")
            print("Do you find something interesting?\n")
            find_something(0.4, location_selected)
        elif str.lower(sub_location) == "back":
            headed()
        else:
            print(" locations else statement")


def find_something(lower_location, location_selected):
    global found_weapon, found_clue1, found_clue2, found_final_evidence
    #print(lower_location)
    #print("Find Something location selected",location_selected)
    #print(location_selected[6])
    upper_location = location_selected[6]
    current_location = lower_location + upper_location

    if current_location == items_needed["weapon"]:
        print("You found a {0}!".format(suspect_attributes["Weapon"]))
        found_weapon = True
        print("-------------------------------------------------------------------------------")
        keep_searching(upper_location, current_location, location_selected)

    elif current_location == items_needed["Clue 1"]:
        print("You found a {0}".format(suspect_attributes["Clue 1"]))
        found_clue1 = True
        print("-------------------------------------------------------------------------------")
        keep_searching(upper_location, current_location, location_selected)

    elif current_location == items_needed["Clue 2"]:
        print("You found a {0}".format(suspect_attributes["Clue 2"]))
        found_clue2 = True
        print("-------------------------------------------------------------------------------")
        keep_searching(upper_location, current_location, location_selected)

    elif current_location == items_needed["Final Evidence"]:
        print("You found a {0}".format(suspect_attributes["Final Evidence"]))
        found_final_evidence = True
        print("-------------------------------------------------------------------------------")
        keep_searching(upper_location, current_location, location_selected)

    else:
        print("You don't find anything")
        print("-------------------------------------------------------------------------------")
        keep_searching(upper_location, current_location, location_selected)

def endgame():
    print("Congradulations You Won the Game!!!!!")

    print(f" {your_name} found out that the suspect was the {0}, they were killed using {1}. ".format(suspect_attributes["Name"],suspect_attributes["Weapon"]))
    print(" The other evidence you found was the {0}, as well as {1}.  However, the most damning evidence was the {2}.".format(suspect_attributes["Clue 1"],suspect_attributes["Clue 2"],suspect_attributes["Final Evidence"]))

your_name = intro()
