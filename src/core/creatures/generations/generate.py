classes, counter = "", 0
path = "/Users/jgarcia/PycharmProjects/pythonProject/src/core/creatures/generations/"


with open(f'{path}Gen1.csv') as f:
    for line in f:
        counter += 1
        if counter > 1:
            name, ps, pa, pd, sa, sd, speed = line.strip().split(",")
            print(f"Name: {name}")

            classes += F"""
class {name}(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.ps = {ps}
        self.physical_attack = {pa}
        self.physical_defense = {pd}
        self.special_attack = {sa}
        self.special_defense = {sd}
        self.speed = {speed}


        """

# open text file
text_file = open(f'{path}Gen1.txt', "w")

# write string to file
text_file.write(classes)

# close file
text_file.close()
