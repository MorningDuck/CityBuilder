#houseObject
from houseL1 import HouseL1

class House:

    def __init__(self,neighbours,plots):

        self.level      = 0
        self.families   = 0
        self.residents  = 0
        self.neighbours = neighbours
        self.plots      = plots
        self.goods      = 0
        self.overcrowds = 0

        self.name = "Empty plot"

        
    def upgrade(self):

        new = HouseL1(self.neighbours, self.plots)
        return new

    def overcrowd(self):
        self.overcrowds += 1
        

    def __str__(self):

        return(self.name)

