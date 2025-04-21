import random

class System():
    def __init__(self):
        size = random.randint(1, 3)
        econ_vaue = random.randint(1, 3) * size
        soverign = None
        has_border = False
        border_max = random.randint(2, 3)
        border_count = 0
        borders = []


    def add_border(self, border_sys):
        if not isinstance(border_sys, System):
            print(f"{border_sys} is not a vaid system")
            return
        self.has_border = True
        self.borders.append(border_sys)
        self.borer_count += 1
        border_sys.border_count += 1


    def add_system(self, galaxy):
        if not isinstance(galaxy, list):
            raise Exception("invalid galaxy parameter")
        galaxy.append(System())


    