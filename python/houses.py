#houses.py

level = 0

#-- House upgrade needs ---
#house level names
name = ["Empty plot", "Tent","Shack", "Hovel","Hut", "Sturdy hut", \
        "Cottage", "Farmhouse",\
        "Small residence", "Residence","Townhouse", "Boarding house",  \
         "Flophouse", "Tenement", "Apartments",\
          "Slum","Crowded apartments", "Fancy apartments"]

#resident needs
needs = {"Tent":"a heat source.",\
         "Shack":"food.", "Hovel":"clean water.",\
         "Sturdy hut":"household goods.",\
         "Cottage":"something to do.",\
         "Small residence":"household goods from a bazaar."}

for key in ["Empty plot", "Hut", "Farmhouse", "Townhouse","Apartments",\
            "Fancy apartments"]:
    needs[key] = "nothing for now."

for key in ["Residence", "Boarding house","Flophouse"]:
    needs[key] = "a more varied diet."
for key in ["Tenement","Slum"]:
    needs[key] = "skilled jobs."
for key in ["Crowded apartments"]:
    needs[key] = "luxury goods from an \n\temporium."

from random import randint
#landlord needs
upgrades = {}

for key in name:
    upgrades[key] = "needs building materials"

for key in ["Farmhouse", "Townhouse", "Apartments", "Fancy apartments"]:
    upgrades[key] = "is done upgrading for now"

upgrades["Hovel"] = "needs access to sanitation"
upgrades["Empty plot"] = "is waiting for someone to move in"

#--Population--
sizes = {}
pop = 0
for key in name:
    sizes[key] = pop
    if pop == 0:
        pop = 4
    elif key == "Crowded apartments" or key == "Slum":
        pop += 6
    elif key != "Hovel":
        #pop += randint(2,4)
        #pop += 3
        pop = pop * 1.25

#--Printing the house info table--
while level < len(name):
    print(name[level],end=": The residents of this house need ")
    #needs
    try :
        print(needs[name[level]])
    except KeyError:
        print("::NEEDS::")
    #upgrades 
    try:
        print("\tThis property %s."\
              %upgrades[name[level]])
    except KeyError:
        print("::UPGRADES::")

    print("\t%d people live here."%sizes[name[level]])
        
    level += 1
    print()

input()
    
