import random
import enum
from system import System
from empiretype import Pacifist, Materialist, Militarist, Egaltarian, Technocratic

class EmpireType(enum):
    PACIFIST = "pasifist"
    MILITARIST = "militarist"
    EGALTERIAN = "egalterian"
    MATERIALIST = "materialist"
    TECHNOCRATIC = "technocratic"


class Empire():
    def __init__(self):
        empire_type = None
        is_ai = False #not implemented yet
        is_at_war = False
        is_vassel = False
        is_alive = True #maybe just implement a "when systems = 0, remove from empires list"
        system_count = 0
        economy = 0
        military_power = 0
        tech_level = 0
        fleet_cap = 0
        fleet_power = 0
        score = 0
        systems = [] 
        neighbors = []
        rivals = []
        name = "" #to be implemented (.csv?)

    def create_new_empire():
        em_type = random.randint(1, 5)
        match em_type:
            case 1:
                return Pacifist()
            case 2:
                return Militarist()
            case 3:
                return Egaltarian()
            case 4:
                return Materialist()
            case 5:
                return Technocratic()
            
    def add_system(self, sys):
        sys.soverign = self
        self.systems.append(sys)
        self.system_count += 1
        self.economy += sys.econ_value
        self.fleet_cap += 2
        self.military_power -= 1
        self.score += sys.econ_value + 4

    def lose_system(self, sys):
        sys.soverign = None
        self.systems.remove(sys)
        self.system_count -= 1
        self.economy -= sys.econ_value
        self.fleet_cap -= 2
        self.military_power += 1
        self.score += sys.econ_value - 4

    def preform_actions(self):
        if self.is_at_war and self.fleet_power > 0:
            self.preform_war()
        self.inc_tech_level()
        self.rebuild_fleet()
        if not self.is_vassel:
            for neighbor in self.neighbors:
                self.attempt_vassalization(neighbor)
                                

    def preform_war(self):
        offensive_battle_cap = random.randint(1, 3)
        off_battles_fought = 0
        for sys in self.systems:
            for neighbor in sys.borders:
                if off_battles_fought < offensive_battle_cap and neighbor.soverign in self.rivals and self.fleet_power > 0:
                        if neighbor.sovergin.fleet_power <= 0:
                            neighbor.soverign.lose_system(neighbor)
                            self.add_system(neighbor)
                        else:
                            victory_num = random.randint(0, 1)
                            if victory_num == 1:
                                neighbor.soverign.fleet_power -= 5
                                neighbor.soverign.lose_system(neighbor)
                                self.add_system(neighbor)
                                self.fleet_power -= 3
                            else:
                                neighbor.soverign.fleet_power -= 3
                                self.fleet_power -= 3
        self.military_power = self.fleet_power // self.system_count
        self.rescore()

    def attempt_vassalization(self, neighbor):
        if neighbor.score < self.score // 2:
            chance = random.randint(1, 100)
            if neighbor.score < self.score // 4:
                if chance <= 75:
                    self.vasselize(neighbor)
            elif neighbor.score < self.score // 3:
                if chance <= 50:
                    self.vasselize(neighbor)
            else:
                if chance <= 25:
                    self.vasselize(neighbor)
        self.rescore()

    def vasselize(self, neighbor):
        neighbor.overlord = self
        self.fleet_cap += neighbor.fleet_cap
        self.fleet_power += neighbor.fleet_power
        self.systems.extend(neighbor.systems)
        neighbor.neighbors.remove(self)
        self.neighbors.extend(neighbor.neighbors)

    def inc_tech_level(self):
        self.tech_level += 1
        self.rescore()

    def rescore(self):
        new_score = self.system_count + self.economy + (self.tech_level * 5) + self.military_power
        self.score = new_score

    def rebuild_fleet(self):
        if self.fleet_power < self.fleet_cap:
            self.fleet_power += self.economy
            if self.fleet_power > self.fleet_cap:
                self.fleet_power == self.fleet_cap
        self.rescore()



    def update_military_power(self): #update score?
        #self.military_power
        pass
        
        
