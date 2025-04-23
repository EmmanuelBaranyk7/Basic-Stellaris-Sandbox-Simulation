from empire import Empire, EmpireType
from build import Sandbox
from system import System

def main():
    sandbox = Sandbox()
    sandbox.build_sandbox()

    for border in sandbox.galaxy[2].borders:
        print(f"border check: {border.name}")

    while sandbox.current_year <= sandbox.end_year:
        #print(f"current year {sandbox.current_year}")
        sandbox.update_sandbox()

main()