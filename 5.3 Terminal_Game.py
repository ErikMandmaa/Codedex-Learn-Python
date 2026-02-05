import random # importing random module for generating random events
import time # importing time module for adding delays
import sys # importing sys module for system-specific parameters and functions

class SpaceAdventure: # main game class
    def __init__(self): # initializing game variables
        self.ship_health = 100 # ship's health percentage 
        self.crew_morale = 80 # crew's morale perecentage
        self.fuel = 100 # fuel percentage
        self.supplies = 50 # amount of supplies
        self.discoveries = 0 # number of discoveries made 
        self.credits = 100 # amount of credits player has
        
    def clear_screen(self): # function to clear the terminal screen
        print("\n" * 2) # printing new lines to simulate clearing the screen
    
    def slow_print(self, text, delay=0.03): # function to print text slowly for dramatic effect
        for char in text: # iterating through each character in the text
            sys.stdout.write(char) # writing character to standard output
            sys.stdout.flush() # flushing the output buffer
            time.sleep(delay) # adding delay between characters
        print() # printing a new line after the text is printed
    
    def display_status(self): # function to display current status of the ship and crew
        print("\n" + "="*50) # printing separator line
        print(f" SHIP STATUS") # title
        print("="*50) # printing separator line
        print(f"Hull Integrity: {self.ship_health}%") # displaying ship health
        print(f"Crew Morale: {self.crew_morale}%") # displaying crew morale
        print(f"Fuel: {self.fuel}%") # displaying fuel level
        print(f"Supplies: {self.supplies} units") # displaying supplies
        print(f"Credits: {self.credits}") # displaying credits
        print(f"Discoveries: {self.discoveries}") # displaying number of discoveries
        print("="*50 + "\n") # printing separator line
    
    def get_choice(self, num_options): # function to get player's choice from given options
        while True: # loop until valid input is received
            try: # try block to catch invalid inputs
                choice = int(input("\nEnter your choice (number): ")) # getting input from player
                if 1 <= choice <= num_options: # checking if input is within valid range
                    return choice # returning valid choice
                else: # otherwise
                    print(f"Please enter a number between 1 and {num_options}") # prompting for valid input
            except ValueError: # catching value error for non-integer inputs
                print("Please enter a valid number")
    
    def intro(self): # function to display game introduction
        self.clear_screen() # clearing the screen
        self.slow_print("    THE VOID BETWEEN STARS: A SPACE ODYSSEY    ") # game title
        time.sleep(1) # adding delay
        self.slow_print("\nYear 2347. You are Captain of the deep-space vessel 'Horizon's Edge'.") # intro text
        self.slow_print("Your mission: explore the uncharted Nebula Sector and return with valuable data.") # mission briefing
        self.slow_print("\nBut space is unforgiving, and every decision matters...") # warning text
        time.sleep(1.5) # adding delay
        input("\nPress Enter to begin your journey...") # waiting for player to start the game
    
    def game_over(self, reason): # function to handle game over scenario
        self.clear_screen() # clearing the screen
        self.slow_print("\n  MISSION FAILED! \n") # game over title
        self.slow_print(reason) # displaying reason for game over
        self.slow_print(f"\nFinal Discoveries: {self.discoveries}") # displaying final discoveries
        self.slow_print("\nThe void claims another ship...") # dramatic ending text
        sys.exit() # exiting the game
    
    def victory(self): # function to handle victory scenario
        self.clear_screen() # clearing the screen
        self.slow_print("\n  MISSION SUCCESS!  \n") # victory title
        self.slow_print("You've navigated the treacherous Nebula Sector and returned home safely!") # victory message
        self.slow_print(f"\nTotal Discoveries: {self.discoveries}") # displaying total discoveries
        self.slow_print(f"Final Credits: {self.credits}") # displaying final credits
        self.slow_print("\nYour name will be remembered in the annals of space exploration!") # celebratory message
        sys.exit() # exiting the game
    
    def check_game_over(self): # function to check if game over conditions are met
        if self.ship_health <= 0: # checking ship health
            self.game_over("Your ship has been destroyed. The crew perished in the cold void.") # game over message
        if self.crew_morale <= 0: # checking crew morale
            self.game_over("The crew has mutinied! You've been cast out into space.") # game over message
        if self.fuel <= 0: # checking fuel level
            self.game_over("You've run out of fuel. The ship drifts endlessly through space...") # game over message
    
    def event_mysterious_signal(self): # function for mysterious signal event
        self.clear_screen() # clearing the screen
        self.display_status() # displaying current status
        self.slow_print(" MYSTERIOUS SIGNAL DETECTED! \n") # event title
        self.slow_print("Your comms officer reports an unknown transmission from a nearby asteroid field.") # event description
        self.slow_print("It could be a distress signal... or a trap.") # event description
        
        print("\nWhat do you do?") # prompting player for choice 
        print("1. Investigate the signal") # option 1
        print("2. Ignore it and continue on your course") # option 2
        print("3. Send a probe to investigate first") # option 3
        
        choice = self.get_choice(3) # getting player's choice
        
        if choice == 1: # if player chooses to investigate
            self.slow_print("\nYou navigate into the asteroid field...") # event narrative
            outcome = random.randint(1, 3) # random outcome generator
            if outcome == 1: # positive outcome
                self.slow_print("You find a derelict ship with valuable salvage!") # event narrative
                self.credits += 50 # adding credits
                self.supplies += 20 # adding supplies
                self.discoveries += 1 # adding discovery
                self.slow_print("+ 50 Credits, + 20 Supplies, + 1 Discovery!") # event rewards
            elif outcome == 2: # negative outcome
                self.slow_print("It's a trap! Pirates ambush your ship!") # event narrative
                self.ship_health -= 25 # reducing ship health
                self.crew_morale -= 15 # reducing crew morale
                self.slow_print("- 25 Hull Integrity, - 15 Morale") # event penalties
            else: # neutral outcome
                self.slow_print("You find stranded colonists! They're grateful for rescue.") # event narrative
                self.crew_morale += 20 # increasing crew morale
                self.discoveries += 1 # adding discovery
                self.slow_print("+ 20 Morale, + 1 Discovery!") # event rewards
        elif choice == 2: # if player chooses to ignore
            self.slow_print("\nYou decide to play it safe and continue on...") # event narrative
            self.fuel -= 5 # reducing fuel
            self.slow_print("- 5 Fuel") # event penalty
        else: # if player chooses to send a probe
            self.slow_print("\nYour probe reveals it's just spatial interference. Smart move!") # event narrative
            self.fuel -= 10 # reducing fuel
            self.slow_print("- 10 Fuel") # event penalty 
        
        self.fuel -= 10 # reducing fuel for the event
    
    def event_alien_encounter(self): # function for alien encounter event
        self.clear_screen() # clearing the screen
        self.display_status() # displaying current status
        self.slow_print(" ALIEN VESSEL DETECTED! \n") # event title
        self.slow_print("A sleek, bio-organic ship emerges from quantum space.") # event description
        self.slow_print("The aliens are attempting to communicate...") # event description
        
        print("\nHow do you respond?") # prompting player for choice
        print("1. Attempt peaceful communication") # option 1
        print("2. Raise shields and prepare weapons") # option 2
        print("3. Offer a gift (costs 30 credits)") # option 3 
        print("4. Retreat immediately") # option 4
        
        choice = self.get_choice(4) # getting player's choice
        
        if choice == 1: # if player chooses peaceful communication
            outcome = random.randint(1, 2) # random outcome generator
            if outcome == 1: # positive outcome
                self.slow_print("\nThe aliens share advanced star charts with you!") # event narrative
                self.discoveries += 2 # adding discoveries
                self.fuel += 20 # adding fuel
                self.slow_print("+ 2 Discoveries, + 20 Fuel!") # event rewards
            else: # neutral outcome
                self.slow_print("\nCommunication fails. The aliens seem confused and depart.") # event narrative
                self.slow_print("No changes.") # event narrative
        elif choice == 2: # if player chooses to prepare for combat
            self.slow_print("\nThe aliens interpret this as hostility and attack!") # event narrative
            self.ship_health -= 30 # reducing ship health
            self.crew_morale -= 10 # reducing crew morale
            self.slow_print("- 30 Hull Integrity, - 10 Morale") # event penalties
        elif choice == 3: # if player chooses to offer a gift
            if self.credits >= 30: # checking if player has enough credits
                self.slow_print("\nThe aliens are pleased! They grant you safe passage and rare materials.") # event narrative
                self.credits -= 30 # reducing credits
                self.credits += 80 # adding credits
                self.discoveries += 1 # adding discovery
                self.slow_print("- 30 Credits, + 80 Credits, + 1 Discovery!") # event rewards
            else: # if not enough credits
                self.slow_print("\nYou don't have enough credits!") # event narrative
                self.crew_morale -= 5 # reducing crew morale
                self.slow_print("- 5 Morale") # event penalty
        else: # if player chooses to retreat
            self.slow_print("\nYou retreat safely, but the crew questions your courage.") # event narrative
            self.fuel -= 20 # reducing fuel
            self.crew_morale -= 10 # reducing crew morale
            self.slow_print("- 20 Fuel, - 10 Morale") # event penalties
        
        self.fuel -= 10 # reducing fuel for the event
     
    def event_space_station(self): # function for space station event
        self.clear_screen() # clearing the screen
        self.display_status() # displaying current status
        self.slow_print(" SPACE STATION AHEAD! \n") # event title
        self.slow_print("You've reached 'Haven Station', a trading outpost on the edge of civilized space.") # event description
        
        print("\nWhat would you like to do?") # prompting player for choice
        print("1. Trade credits for supplies (50 credits = 30 supplies)") # option 1
        print("2. Repair your ship (50 credits = 40 hull integrity)") # option 2
        print("3. Give the crew shore leave (30 credits, +25 morale)") # option 3
        print("4. Refuel (40 credits = 50 fuel)") # option 4
        print("5. Leave the station") # option 5
        
        choice = self.get_choice(5) # getting player's choice
        
        if choice == 1: # if player chooses to trade for supplies
            if self.credits >= 50: # checking if player has enough credits
                self.credits -= 50 # reducing credits
                self.supplies += 30 # adding supplies
                self.slow_print("\nSupplies loaded! - 50 Credits, + 30 Supplies") # event rewards
            else: # if not enough credits
                self.slow_print("\nInsufficient credits!") # event narrative
        elif choice == 2: # if player chooses to repair ship
            if self.credits >= 50: # checking if player has enough credits
                self.credits -= 50 # reducing credits
                self.ship_health = min(100, self.ship_health + 40) # repairing ship health
                self.slow_print("\nRepairs complete! - 50 Credits, + 40 Hull Integrity") # event rewards
            else: # if not enough credits
                self.slow_print("\nInsufficient credits!") # event narrative
        elif choice == 3: # if player chooses shore leave
            if self.credits >= 30: # checking if player has enough credits
                self.credits -= 30 # reducing credits
                self.crew_morale = min(100, self.crew_morale + 25) # increasing crew morale
                self.slow_print("\nThe crew returns refreshed! - 30 Credits, + 25 Morale") # event rewards
            else: # if not enough credits
                self.slow_print("\nInsufficient credits!") # event narrative
        elif choice == 4: # if player chooses to refuel
            if self.credits >= 40: # checking if player has enough credits
                self.credits -= 40 # reducing credits
                self.fuel = min(100, self.fuel + 50) # refueling
                self.slow_print("\nFuel tanks full! - 40 Credits, + 50 Fuel") # event rewards
            else: # if not enough credits
                self.slow_print("\nInsufficient credits!") # event narrative
        else: # if player chooses to leave
            self.slow_print("\nYou depart the station.") # event narrative
        
        self.fuel -= 5 # reducing fuel for the event
    
    def event_nebula_anomaly(self): # function for nebula anomaly event
        self.clear_screen() # clearing the screen
        self.display_status() # displaying current status
        self.slow_print(" QUANTUM ANOMALY DETECTED! \n") # event title
        self.slow_print("Your sensors have picked up a swirling quantum anomaly in a nearby nebula.") # event description
        self.slow_print("It's incredibly dangerous but could hold unprecedented scientific value.") # event description
        
        print("\nWhat's your decision?") # prompting player for choice
        print("1. Navigate directly through it (high risk, high reward)") # option 1
        print("2. Collect data from a safe distance") # option 2
        print("3. Avoid it entirely") # option 3
        
        choice = self.get_choice(3) # getting player's choice
        
        if choice == 1: # if player chooses to navigate through
            self.slow_print("\nYou enter the anomaly. Space-time warps around you...") # event narrative
            outcome = random.randint(1, 4) # random outcome generator
            if outcome == 1: # positive outcome
                self.slow_print("Critical success! You've discovered a new form of matter!") # event narrative
                self.discoveries += 3 # adding discoveries
                self.credits += 100 # adding credits
                self.slow_print("+ 3 Discoveries, + 100 Credits!") # event rewards
            elif outcome == 4: # negative outcome
                self.slow_print("Catastrophic failure! The anomaly tears into your hull!") # event narrative
                self.ship_health -= 40 # reducin ship health
                self.crew_morale -= 20 # reducing crew morale
                self.slow_print("- 40 Hull Integrity, - 20 Morale") # event penalties
            else: # neutral outcome
                self.slow_print("You collect valuable data but take some damage.") # event narrative
                self.discoveries += 1 # adding discovery
                self.ship_health -= 15 # reducing ship health
                self.slow_print("+ 1 Discovery, - 15 Hull Integrity") # event rewards and penalties
        elif choice == 2: # if player chooses to collect data from distance
            self.slow_print("\nYou carefully gather data from the periphery.") # event narrative
            self.discoveries += 1 # adding discovery 
            self.fuel -= 15 # reducing fuel
            self.slow_print("+ 1 Discovery, - 15 Fuel") # event rewards and penalties
        else: # if player chooses to avoid
            self.slow_print("\nYou take the long route around. Safety first.") # event narrative
            self.fuel -= 20 # reducing fuel
            self.crew_morale -= 5 # reducing crew morale
            self.slow_print("- 20 Fuel, - 5 Morale") # event penalties
        
        self.fuel -= 10 # reducing fuel for the event
    
    def event_crew_crisis(self): # function for crew crisis event
        self.clear_screen() # clearing the screen
        self.display_status() # displaying current status
        self.slow_print(" CREW SITUATION! \n") # event title
        
        crisis_type = random.randint(1, 3) # random crisis type generator
        
        if crisis_type == 1: # supply shortage crisis
            self.slow_print("Your engineer reports critical supply shortages.") # event description
            self.slow_print("Morale is dropping fast!") # event descriptiom
            print("\nWhat do you do?") # prompting player for choice
            print("1. Use emergency rations (costs 20 supplies)") # option 1
            print("2. Boost morale with a stirring speech") # option 2
            print("3. Implement strict rationing (crew won't like it)") # option 3
            
            choice = self.get_choice(3) # getting player's choice
            if choice == 1: # if player chooses emergency rations
                if self.supplies >= 20: # checking if enough supplies
                    self.supplies -= 20 # reducing supplies
                    self.crew_morale += 15 # increasing crew morale
                    self.slow_print("\n+ 15 Morale, - 20 Supplies") # event rewards and penalties
                else: # if not enough supplies
                    self.slow_print("\nNot enough supplies!") # event narrative
                    self.crew_morale -= 10 # reducing crew morale
                    self.slow_print("- 10 Morale") # event penalty
            elif choice == 2: # if player chooses to boost morale
                outcome = random.randint(1, 2) # random outcome generator
                if outcome == 1: # positive outcome
                    self.slow_print("\nYour words inspire the crew!") # event narrative
                    self.crew_morale += 20 # increasing crew morale
                    self.slow_print("+ 20 Morale") # event reward
                else: # negative outcome
                    self.slow_print("\nThe crew sees through your empty words.") # event narrative
                    self.crew_morale -= 5 # reducing crew morale
                    self.slow_print("- 5 Morale") # event penalty
            else: # if player chooses rationing
                self.slow_print("\nThe crew grudgingly accepts rationing.") # event narrative
                self.crew_morale -= 15 # reducing crew morale
                self.supplies += 10 # increasing supplies
                self.slow_print("- 15 Morale, + 10 Supplies") # event penalties and rewards
        
        elif crisis_type == 2: # crew conflict crisis
            self.slow_print("Two crew members are fighting over navigation decisions!") # event description
            print("\nHow do you handle it?") # prompting player for choice
            print("1. Side with the first officer") # option 1
            print("2. Side with the navigator") # option 2
            print("3. Confine both to quarters until they cool down") # option 3
            
            choice = self.get_choice(3) # getting player's choice
            if choice == 3: # if player chooses to confine both
                self.slow_print("\nA fair decision. The crew respects your judgment.") # event narrative
                self.crew_morale += 10 # increasing crew morale
                self.slow_print("+ 10 Morale") # event reward
            else: # if player chooses to side with one
                self.slow_print("\nYour favoritism causes division among the crew.") # event narrative
                self.crew_morale -= 10 # reducing crew morale
                self.slow_print("- 10 Morale") # event penalty
        
        else: # fatigue crsis
            self.slow_print("The crew is exhausted from the long journey.") # event description
            self.slow_print("They're requesting a rest period.") # event description
            print("\nYour response?") # prompting player for choice
            print("1. Grant them rest (costs time/fuel)") # option 1
            print("2. Push forward (crew won't be happy)") # option 2
            
            choice = self.get_choice(2) # getting player's choice
            if choice == 1: # if player chooses to grant rest
                self.slow_print("\nThe crew returns rested and grateful.") # event narrative
                self.fuel -= 15 # reducing fuel
                self.crew_morale += 20 # increasing crew morale
                self.slow_print("+ 20 Morale, - 15 Fuel") # event rewards and penalties
            else: # if player chooses to push forward
                self.slow_print("\nThe crew reluctantly continues, but resentment builds.") # event narrative
                self.crew_morale -= 15 # reducing crew morale
                self.slow_print("- 15 Morale") # event penalty
    
    def final_choice(self): # function for final mission choice
        self.clear_screen() # clearing the screen
        self.display_status() # displaying current status
        self.slow_print(" MISSION CRITICAL DECISION! \n") # event title
        self.slow_print("You've reached the heart of the Nebula Sector.") # event description
        self.slow_print("Before you lies an ancient alien structure - a gateway to unknown space.") # event description
        self.slow_print("\nThis is what you came for, but entering could be fatal...") # event description
        
        print("\nWhat is your final decision?") # prompting player for choice
        print("1. Enter the gateway (ultimate risk for ultimate discovery)") # option 1
        print("2. Collect data and return home safely") # option 2
        
        choice = self.get_choice(2) # getting player's choice
        
        if choice == 1: # if player chooses to enter the gateway
            self.slow_print("\nYou enter the gateway...") # event narrative
            time.sleep(2) # adding delay
            self.slow_print("Reality bends around you...") # event narrative
            time.sleep(2) # adding delay
            
            if self.ship_health > 40 and self.crew_morale > 40: # checking if ship and crew are in good condition
                self.slow_print("\nYour well-prepared ship emerges in a realm of infinite possibilities!") # event narrative
                self.slow_print("You've discovered the key to faster-than-light travel!") # event narrative
                self.discoveries += 5 # adding discoveries
                self.credits += 500 # adding credits
                self.victory() # calling victory function
            else: # if ship or crew are in poor condition
                self.slow_print("\nYour damaged ship can't withstand the forces...") # event narrative
                self.game_over("The gateway consumed your vessel. A brave but fatal choice.") # game over message
        else: # if player chooses to return home
            self.slow_print("\nWisdom is knowing when to return.") # event narrative
            time.sleep(1) # adding delay
            if self.discoveries >= 5: # checking if enough discoveries were made
                self.slow_print("Your wealth of discoveries makes this mission a triumph!") # event narrative
                self.victory() # calling victory function
            else: # if not enough discoveries
                self.slow_print("You return safely, but with fewer discoveries than hoped.")
                self.slow_print("The mission is deemed a partial success.") # event narrative
                self.slow_print(f"\nFinal Discoveries: {self.discoveries}") # displaying final discoveries
                sys.exit() # exiting the game
    
    def play(self): # main game loop
        self.intro() # calling intro function
        
        events = [ # list of possible events
            self.event_mysterious_signal, # function for mysterious signal event
            self.event_alien_encounter, # function for alien encounter event
            self.event_space_station, # function for space station event
            self.event_nebula_anomaly, # function for nebula anomaly event
            self.event_crew_crisis # function for crew crisis event
        ] # end of events list
        
        for i in range(6): # looping through 6 events
            self.check_game_over() # checking for game over conditions
            event = random.choice(events) # randomly selecting an event
            event() # calling the selected event function
            time.sleep(1.5) # adding delay
            input("\n[Press Enter to continue...]") # waiting for player to continue
        
        self.final_choice() # calling final choice function

if __name__ == "__main__": # main entry point
    game = SpaceAdventure() # creating game instance
    game.play() # starting the game