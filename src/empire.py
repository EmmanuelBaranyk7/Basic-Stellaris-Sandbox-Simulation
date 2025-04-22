import random
from enum import Enum
from system import System

class EmpireType(Enum):
    PACIFIST = "pasifist"
    MILITARIST = "militarist"
    EGALITERIAN = "egalterian"
    MATERIALIST = "materialist"
    TECHNOCRATIC = "technocratic"


class Empire():
    def __init__(self):
        self.empire_type = None
        self.is_ai = False #not implemented yet
        self.is_at_war = False
        self.is_vassal = False #will take this out
        self.overlord = None
        self.is_alive = True #maybe just implement a "when systems = 0, remove from empires list"
        self.system_count = 0
        self.economy = 0
        self.military_power = 0
        self.tech_level = 0
        self.fleet_cap = 0
        self.fleet_power = 0
        self.score = 0
        self.systems = [] 
        self.neighbors = []
        self.rivals = []
        self.vassals = []
        self.name = "" #to be implemented (.csv?)
            
    def add_system(self, sys):
        sys.sovereign = self
        self.systems.append(sys)
        self.system_count += 1
        self.economy += sys.econ_value
        self.fleet_cap += 2
        self.military_power -= 1
        #self.score += sys.econ_value

    def lose_system(self, sys):
        sys.sovereign = None
        self.systems.remove(sys)
        self.system_count -= 1
        self.economy -= sys.econ_value
        self.fleet_cap -= 2
        self.military_power += 1
        #self.score -= sys.econ_value
        if self.overlord != None:
            self.overlord.systems.remove(sys)
            self.overlord.system_count -= 1
            self.overlord.economy -= sys.econ_value
            self.overlord.fleet_cap -= 2
            self.overlord.military_power += 1
            #self.overlord.score -= sys.econ_value
            

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
                        if neighbor.soveregin.fleet_power <= 0:
                            neighbor.sovereign.lose_system(neighbor)
                            self.add_system(neighbor)
                        else:
                            victory_num = random.randint(0, 1)
                            if victory_num == 1:
                                neighbor.sovereign.fleet_power -= 5
                                neighbor.sovereign.lose_system(neighbor)
                                self.add_system(neighbor)
                                self.fleet_power -= 3
                            else:
                                neighbor.sovereign.fleet_power -= 3
                                self.fleet_power -= 3
        if self.is_overlord:
            for vassel in self.vassals:
                bonus += vassel.fleet_power // vassel.system_count
        self.military_power = (self.fleet_power // self.system_count) + bonus
        self.rescore()

    def attempt_vassalization(self, neighbor):
        if neighbor.score < self.score // 2:
            chance = random.randint(1, 100)
            if neighbor.score < self.score // 4:
                if chance <= 75:
                    self.vassalize(neighbor)
            elif neighbor.score < self.score // 3:
                if chance <= 50:
                    self.vassalize(neighbor)
            else:
                if chance <= 25:
                    self.vassalize(neighbor)
        self.rescore()

    def vassalize(self, neighbor): # note: vassals systems no longer count toward system_count, just score
        neighbor.overlord = self 
        self.fleet_cap += neighbor.fleet_cap
        self.fleet_power += neighbor.fleet_power
        self.systems.extend(neighbor.systems)
        neighbor.neighbors.remove(self)
        self.neighbors.remove(neighbor)
        self.neighbors.extend(neighbor.neighbors)
        self.vassals.append(neighbor)

    def inc_tech_level(self):
        self.tech_level += 1
        self.rescore()

    def rescore(self):
        bonus = 0
        if self.overlord is None and self.vassals:
            for vassal in self.vassals:  
                vassal.rescore()
                bonus += abs(vassal.tech_level - self.tech_level) 
                vassal.military_power = vassal.fleet_power // vassal.system_count
                bonus += vassal.system_count + vassal.economy + vassal.military_power 
        self.military_power = self.fleet_power // self.system_count
        self.score = self.system_count + self.economy + (self.tech_level * 5) + self.military_power + bonus

    def rebuild_fleet(self):
        if self.fleet_power < self.fleet_cap:
            self.fleet_power += self.economy
            if self.fleet_power > self.fleet_cap:
                self.fleet_power == self.fleet_cap
        self.rescore()

    def add_name(self, empire_names):
        if empire_names:  
            self.name = random.choice(empire_names)  
            empire_names.remove(self.name)  



    def update_military_power(self): #update score?
        #self.military_power
        pass
        
        
