import random
import csv
from empire import Empire
from empiretype import EmpireType, create_new_empire
from system import System

'''
This class creates the enviornment that the simulation will take place in (the "sandbox").

It will create the galaxy, the empires, and set the game rules.

It will have a method to run the simulation, which will update the sandbox each iteration.
'''
class Sandbox():
    def __init__(self):
        self.end_year = 0                   # end year of the game
        self.contigency_start_year = 0      # contigency is like the final boss, a special empire type that the other empire will have to fight
        self.current_year = 0               # current year of the game
        self.galaxy = []                    # list of systems in the galaxy (galaxy is made up of system objects that the empires interat over)
        self.empires = []                   # list of empire objects    
        self.s_names = []                   # list of system names
        self.empire_names =[]               # list of empire names


    '''
    creates a sandbox object, which will be used to create the galaxy and empires

    functions used are "transition" function that check user input and pass vadid input to the "builder" functions
    '''
    def build_sandbox(self):
        self.create_system_names_list()         # create a list of system names from a csv file
        self.create_empire_names_list()     # create a list of empire names from a csv file
        #ask about default settings
        #set_num_AI_empires()
        #set_num_fallen_empires()
        self.set_galaxy_size()              # set the size of the galaxy
        self.set_num_empires()        # set the number of empires in the galaxy
        self.set_game_end_year()        # set the end year of the game
        self.set_contigency_start_year()            # set the year that the contigency will start
        #build_custom_empire()


    '''
    gets a list of system names from a csv file and sets self.s_names to that list
    '''
    def create_system_names_list(self):
        filepath = "/home/eman1/workspace/github.com/EmmanuelBaranyk7/Basic-Stellaris-Sandbox-Simulation/planet_names.csv"
        with open(filepath, newline='', encoding='utf-8') as csvf:
            reader = csv.reader(csvf)
            next(reader)  # Skip header
            self.s_names = [row[0] for row in reader]


    '''
    gets a list of empire names from a csv file and sets self.empire_names to that list
    '''
    def create_empire_names_list(self):
        filepath = "/home/eman1/workspace/github.com/EmmanuelBaranyk7/Basic-Stellaris-Sandbox-Simulation/empire_names.csv"
        with open(filepath, newline='', encoding='utf-8') as csvf:
            reader = csv.reader(csvf)
            next(reader)  # Skip header
            self.empire_names = [row[0] for row in reader]


    '''
    takes a size as user input, passes valid size to create_galaxy()
    '''
    def set_galaxy_size(self):
        size = int(input("what size would you like the galaxy? (num of systems): "))
        if not isinstance(size, int):
            raise Exception("not a valid size. Must be a positive int (1, 2, 3, etc)")
        
        self.create_galaxy(size)

    
    '''
    takes a number of empires as user input, passes valid number to colonize_empires()
    '''
    def set_num_empires(self):
        while True: 
            try:
                num = int(input("Number of empires: "))
                if num > 0 and num < len(self.galaxy) // 2:  # make sure there are enough systems for the empires (they need room to grow)
                    break
            except ValueError:
                print("Not a valid integer num of empires or too big. try again")
        self.colonize_empires(num)


    '''
    takes a year as user input, sets self.end_year to that year
    '''
    def set_game_end_year(self):
        while True:
            try:
                year = int(input("Set end year: "))
                if year > 0:
                    break
                print("Please input a positive year")
            except ValueError:
                print("Not a valid positive integer year. try again")
        self.end_year = year


    '''
    takes a year as user input, sets self.contigency_start_year to that year
    '''
    def set_contigency_start_year(self):   #later implement not having a contigency?
        while True:
            try:
                year = int(input("Set contigency start year: "))
                if year < self.end_year:                            # make sure contitgency happens during simulation (before end year)
                    break
                print("input is after end year, please try again")
            except ValueError:
                print("Not a valid integer year. try again")
        self.contigency_start_year = year


    def run_sandbox(self):
        for year in self.end_year:
            self.update_sandbox

    def create_galaxy(self, size):
        for i in range(size):
            System().add_system(self.galaxy)
            self.galaxy[-1].add_name(self.s_names)
            for sys in self.galaxy:
                if sys is not self.galaxy[i] and self.galaxy[i].border_count < self.galaxy[i].border_max and sys.border_count < sys.border_max:
                    self.galaxy[i].add_border(sys) 
        if not self.galaxy[-1].has_border:
            self.galaxy[-1].add_border(self.galaxy[-2]) # rare case there is a borderless system left over


    def colonize_empires(self, num):
        for i in range(num):
            while True:
                index = random.randint(0, len(self.galaxy)-1)
                if not self.galaxy[index].sovereign and self.galaxy[index].has_border:
                    e = create_new_empire()
                    e.add_name(self.empire_names)
                    e.add_system(self.galaxy[index])
                    print(f"{e.name} has been colonized in the {self.galaxy[index].name} system")
                    self.empires.append(e)
                    break

    def set_galaxy_size(self):
        size = int(input("what size would you like the galaxy? (num of systems): "))
        if not isinstance(size, int):
            raise Exception("not a valid size. Must be a positive int (1, 2, 3, etc)")
        
        self.create_galaxy(size)


    def set_num_empires(self):
        while True: 
            try:
                num = int(input("Number of empires: "))
                if num > 0 and num < len(self.galaxy) // 2:
                    break
            except ValueError:
                print("Not a valid integer num of empires or too big. try again")
        self.colonize_empires(num)


    def set_game_end_year(self):
        while True:
            try:
                year = int(input("Set end year: "))
                if year > 0:
                    break
                print("Please input a positive year")
            except ValueError:
                print("Not a valid positive integer year. try again")
        self.end_year = year

    def set_contigency_start_year(self):
        while True:
            try:
                year = int(input("Set contigency start year: "))
                if year < self.end_year:
                    break
                print("input is after end year, please try again")
            except ValueError:
                print("Not a valid integer year. try again")
        self.contigency_start_year = year

    def create_system_names_list(self):
        filepath = "/home/eman1/workspace/github.com/EmmanuelBaranyk7/Basic-Stellaris-Sandbox-Simulation/planet_names.csv"
        with open(filepath, newline='', encoding='utf-8') as csvf:
            reader = csv.reader(csvf)
            next(reader)  # Skip header
            self.s_names = [row[0] for row in reader]

    def create_empire_names_list(self):
        filepath = "/home/eman1/workspace/github.com/EmmanuelBaranyk7/Basic-Stellaris-Sandbox-Simulation/empire_names.csv"
        with open(filepath, newline='', encoding='utf-8') as csvf:
            reader = csv.reader(csvf)
            next(reader)  # Skip header
            self.empire_names = [row[0] for row in reader]

    def update_sandbox(self):
        for e in self.empires:
            e.perform_actions()
            #self.empires[i].display_actions()
        random.shuffle(self.empires) #scramble empires in empires list for "fairness"
        self.current_year += 1
            
    
'''
def make_empires_AI(num, galaxy):
    while True:
        index = random.randint(0, len(galaxy)-1)
        if not galaxy[index].is_ai:
            galaxy[index].is_ai = True
            while True:
                index2 = random.randint(0, len(galaxy[index].systems)-1)
                if galaxy[index].systems[index2].border_count < 3:
                    for bor in galaxy[index].systems[index2].borders:
                        if not bor.is_soverign:
'''        