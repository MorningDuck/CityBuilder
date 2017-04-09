#houseObject
#16 Jan 2017 made base house class and inherited upgrade classes

MAX = "~~Maximum housing level reached~~"

class House:

    def __init__(self):

        self.level      = 0
        self.families   = 0
        self.residents  = 0
        self.plots      = 0
        self.goods      = 0
        self.overcrowds = 0

        self.name = "Empty plot"

        
    def upgrade(self):

        new = HouseL1()
        return new

    def overcrowd(self):
        self.overcrowds += 1
        

    def __str__(self):

        return(self.name)

class HouseL1(House):

    def __init__(self):

        self.level      = 1
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 3
        self.overcrowds = 0

        self.name = "Tent"


    def upgrade(self):

        new = HouseL2()
        return new

class HouseL2(House):

    def __init__(self):

        self.level      = 2
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 3
        self.overcrowds = 0
        
        self.name       = "Lean-to"


    def upgrade(self):

        new = HouseL3()
        return new

class HouseL3(House):

    def __init__(self):

        self.level      = 3
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 3
        self.overcrowds = 0
        
        self.name       = "Hut"
    def upgrade(self):

        if self.overcrowds > 0:

            new = HouseL4()

        else:
            new = HouseL5()
        return new

class HouseL4(House):

    def __init__(self):

        self.level      = 3
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 3
        self.overcrowds = 1
        
        self.name       = "Hovel"


    def upgrade(self):

        new = HouseL5()
        return new

class HouseL5(House):

    def __init__(self):

        self.level      = 4
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 2
        self.overcrowds = 0
        
        self.name       = "Shack"


    def upgrade(self):

        new = HouseL6()
        return new

class HouseL6(House):

    def __init__(self):

        self.level      = 5
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 3
        self.overcrowds = 1
        
        self.name       = "Sturdy hut"


    def upgrade(self):

        new = HouseL7()
        return new

class HouseL7(House):

    def __init__(self):

        self.level      = 6
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 5
        self.overcrowds = 1
        
        self.name       = "Cottage"


    def upgrade(self):

        #if plots, turn into lodge (farm building object)
        if self.overcrowds > 1:
            new = HouseL8()
        else:
            new = MAX
        return new


#forgot to add small lodge

class HouseL8(House):

    def __init__(self):

        self.level      = 8
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 5
        self.overcrowds = 2
        
        self.name       = "Residence"


    def upgrade(self):

        if self.overcrowds > 2:
            new = HouseL10()
        else:
            new = HouseL9()
        return new

class HouseL9(House):

    def __init__(self):

        self.level      = 9
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 5
        self.overcrowds = 2
        
        self.name       = "Townhouse"


    def upgrade(self):

        if self.overcrowds > 2:
            new = HouseL10()
        else:
            new = MAX
        return new

class HouseL10(House):

    def __init__(self):

        self.level      = 9
        self.families   = 1
        self.residents  = 0
        self.plots      = 0
        self.goods      = 5
        self.overcrowds = 3
        
        self.name       = "Boarding house"


    def upgrade(self):

        return 'no -_-'
        
        #for split branch upgrades, check crowding level


    



hq = HouseL7()
print(hq)
hq.overcrowd()
hq = hq.upgrade()
print(hq)

hh = HouseL5()
i = 10
while i > 0:
    print("\nUpdate:")
    try:
        hh.overcrowds = 3
        hh = hh.upgrade()
    except AttributeError:
        print("oopsie")
        break
    print(hh,"\n-----------------------")
    i -= 1

    
