classes, counter = "", 0
path = "/Users/jgarcia/PycharmProjects/pythonProject/src/core/movements/"

with open(f'{path}Gen2.csv') as f:
    for line in f:
        counter += 1
        if counter > 1:
            number, name, type, cat, pp, power, acu, gen = line.strip().split(",")
            print(f"Name: {name} Type: {type}")
            if cat == "Physical":
                category = "MOVEMENT_BASE_PHYSICAL"
            elif cat == "Special":
                category = "MOVEMENT_BASE_SPECIAL"
            else:
                category = "MOVEMENT_BASE_STATUS"

            classes += F"""
class {name}:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = {type.upper()}
        self.category = {category}
        self.damage = {str(power)}
        self.accuracy = {acu}
        self.power_points = {str(pp)}

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


        """

# open text file
text_file = open(f'{path}Gen2.txt', "w")

# write string to file
text_file.write(classes)

# close file
text_file.close()
