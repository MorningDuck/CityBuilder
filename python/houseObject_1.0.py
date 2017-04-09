#houseObject

NORMAL = 0
RURAL = 1
CROWDED = 2
WEALTHY = 3

class House:

    def __init__(self,neighbours):

        self.level      = 0
        self.families   = 0
        self.residents  = 0
        self.neighbours = neighbours
        self.overcrowds = 0

        self.names = ["Empty plot", "Tent","Shack", "Hut","Hovel",\
                      "Barracks","Sturdy hut", "Cottage", "Farmhouse",\
        "Small residence", "Residence","Townhouse", "Boarding house",  \
         "Flophouse", "Tenement", "Apartments",\
          "Slum","Crowded apartments", "Fancy apartments"]

    def upgrade(self, conditions = NORMAL):

        if conditions == NORMAL:
            #residence or boarding house
            if self.level == 9 or self.level == 11:
                self.level += 2
            #tenement
            elif self.level == 13:
                self.level += 1
                
        elif conditions == CROWDED:
            #residence or flophouse
            if self.level == 9 or self.level == 12:
                self.level += 3
            #slum, crowded apartments
            elif self.level == 15 or self.level == 16:
                self.level += 1
                
        elif conditions == WEALTHY:
            #residence
            if self.level == 9:
                self.level += 1

        if self.level == 8:
            self.level += 1

        if conditions != RURAL:
            #cottage
            if self.level == 6:
                self.level += 2

        if self.level < 7:
            self.level += 1

    def __str__(self):

        return(self.names[self.level])


    
