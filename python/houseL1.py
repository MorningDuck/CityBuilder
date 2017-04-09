#HouseL1

from houseObject import House

class HouseL1(House):

    def __init__(self, neighbours, plots):

        self.level = 1
        self.families = 1
        self.neighbours = neighbours
        self.plots      = plots
        self.overcrowds = 0
        self.name       = "Tent"


    def upgrade(self):

        print('no -_-')
        #create HouseL2 object
        #for split branch upgrades, check crowding level

    



hh = House(0,0)

print(hh)

h2 = hh.upgrade()

print(h2)

    
