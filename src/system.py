import random
import csv
class System():
    def __init__(self):
        self.name = ""
        self.size = random.randint(1, 3)
        self.econ_value = random.randint(1, 3) * self.size
        self.sovereign = None
        self.has_border = False
        self.border_max = random.randint(2, 3)
        self.border_count = 0
        self.borders = []


    def add_border(self, border_sys):
        if not isinstance(border_sys, System):
            print(f"{border_sys} is not a vaid system")
            return
        self.has_border = True
        border_sys.has_border = True
        self.borders.append(border_sys)
        border_sys.borders.append(self)
        self.border_count += 1
        border_sys.border_count += 1


    def add_system(self, galaxy):
        if not isinstance(galaxy, list):
            raise Exception("invalid galaxy parameter")
        galaxy.append(self)

    def add_name(self, s_names):
        if s_names:  # Ensure list isn't empty to prevent errors
            self.name = random.choice(s_names)  # Select a random name safely
            s_names.remove(self.name)  # Remove the chosen name
       



    