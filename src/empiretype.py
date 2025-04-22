import random
from empire import Empire, EmpireType

class Pacifist(Empire):
    def __init__(self):
        super().__init__()
        self.empire_type = EmpireType.PACIFIST

class Militarist(Empire):
    def __init__(self):
        super().__init__()
        self.empire_type = EmpireType.MILITARIST

class Egalitarian(Empire):
    def __init__(self):
        super().__init__()
        self.empire_type = EmpireType.EGALITERIAN

class Materialist(Empire):
    def __init__(self):
        super().__init__()
        self.empire_type = EmpireType.MATERIALIST

class Technocratic(Empire):
    def __init__(self):
        super().__init__()
        self.empire_type = EmpireType.TECHNOCRATIC

def create_new_empire():
        em_type = random.randint(1, 5)
        match em_type:
            case 1:
                return Pacifist()
            case 2:
                return Militarist()
            case 3:
                return Egalitarian()
            case 4:
                return Materialist()
            case 5:
                return Technocratic()

    
    