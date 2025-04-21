import enum
from system import System
from empire import Empire
from build import Sandbox
from build import colonize_empires, create_galaxy, set_galaxy_size, set_num_empires
class uinp(enum):
    HELP = "h"
    Yes = "Y"
    No = "N"
class Start():
    def __init__(self):
        is_start = True


    def start_up(self):
        if self.is_start is not True:
            return
        
        print("Welcome to Basic Stellaris Sandbox Simulator!")
        inp = input("Would you like to access the tutorial? (Y/N): ")

        if inp.lower() == "n":
            print("let's get started!")
            new_game = Sandbox()
            new_game.build_sandbox()
        #elif inp == uinp.No:


        
         
    '''
    def set_num_AI_empires(num_empires):
        while True: 
            try:
                num = int(input("Number of AI empires: "))
                if num > 0 and num < num_empires // 3:
                    break
            except ValueError:
                print("Not a valid integer num of AI empires or too big. try again")
        make_empires_AI()
        






    '''