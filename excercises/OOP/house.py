"""
    All MY houses have an address,
    A set amount of doors,
    a set amount of windows,
    either has a cellar or does not have a cellar.
    and either has a attic or does not have a attic.
    I will create a CLASS that holds this information.
    NO objects are created yet.
    The definition of a class is subjective. It's
    my program so I decide the definition of a house is.
    If you want more attributes to it, its fine, it's your class.
"""
class House(object):
    def __init__(self, address, nrOfDoors, nrOfWindows, hasCellar, hasAttic):
        self.address = address
        self.nrOfDoors = nrOfDoors
        self.nrOfWindows = nrOfWindows
        self.hasCellar = hasCellar
        self.hasCellar = hasAttic

"""
We will create ALL our objects by providing the same set of
ATTRIBUTES, but all of them have different VALUES for those attributes.
"""
# Create one fancy house OBJECT,
fancy_house = House("Fancy Address", 10, 10, True, True)
# Create one not so fancy house OBJECT
not_so_fancy_house = House("Not so fancy address", 1, 1, False, False)
# Create a really fancy house OBJECT
castle = House("Really fancy address", 100, 100, True, True)

"""
    Let's put all three OBJECTS in a list,
    so we don't need to keep track of all three
    house VARIABLES
"""
all_houses = []
all_houses.append(fancy_house)
all_houses.append(not_so_fancy_house)
all_houses.append(castle)

"""
    In the MY application,
    all houses with more than 50 windows is
    a CASTLE. Lets try to print it.
"""
for house in all_houses:
    if house.nrOfWindows > 50:
        """
            Ooooh, this house has more than 50 windows,
            its a real CASTLE. Lets store print some information
            and store this house in a list so we can use it later
        """
        print("I found a house with a lot of windows on address %s !" % house.address)
        print("It actually had %s !! This has to be a castle" % house.nrOfWindows)
