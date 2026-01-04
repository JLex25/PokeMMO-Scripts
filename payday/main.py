from pynput.keyboard import Controller
import time
import keys as key
import screen
import sound
import re
import random as rnd
import sys


# Constants
PP = 32
TIMES_FISHING_LOOP = 1

POS_FICHING_DIALOG_X1 = 219
POS_FICHING_DIALOG_Y1 = 138
POS_FICHING_DIALOG_X2 = 526
POS_FICHING_DIALOG_Y2 = 40
FISH_APEARED_TEXT = r'(ha picado un pok)'

POS_POKEMON_NAME_X1 = 139
POS_POKEMON_NAME_Y1 = 162
POS_POKEMON_NAME_X2 = 500
POS_POKEMON_NAME_Y2 = 25 
SHINY_APEARED_TEXT_1 = r'(variocolor)'
SHINY_APEARED_TEXT_2 = r'(shiny)'


# Instances
keyboard = Controller()


# Functions
def start():
    # Countdown before starting
    print("Looping", TIMES_FISHING_LOOP, "times, fishing with", PP, "PP of Pay Day")
    print("--------------")
    count = 5
    for i in range(count):
        print("Starting in", count - i)
        time.sleep(0.8)
    print("--------------")
    

def press_key(key):
    keyboard.press(key) # Press the key
    time.sleep(rnd.uniform(0.08, 0.11)) # Time the key is held down
    keyboard.release(key) # Release the key
    time.sleep(rnd.uniform(0.08, 0.1)) # Time between presses
    
    
def hold_key(key, hold_time):
    keyboard.press(key) # Start holding the key
    time.sleep(hold_time) # Time the key is held down
    keyboard.release(key) # Release the key
    time.sleep(rnd.uniform(0.08, 0.1)) # Time between presses


def heal_pokemon_center_unova():
    hold_key(key.UP, rnd.uniform(1.3, 1.8)) # Up  
    for _ in range(4): # Talking to nurse
        press_key(key.A) # Confirm dialog
        time.sleep(rnd.uniform(0.8, 1.2)) # Wait for dialog
    time.sleep(rnd.uniform(5, 6)) # Wait for healing animation
    for _ in range(3): # End dialog
        press_key(key.B) # Confirm dialog
        time.sleep(rnd.uniform(0.5, 0.8)) # Wait for dialog
       
    
def exit_pokemon_center_unova():
    hold_key(key.DOWN, rnd.uniform(1.5, 1.8)) # Down
    time.sleep(rnd.uniform(1.8, 2.2)) # Wait to exit


def go_to_fishing_spot_undella_town():
    route = rnd.choice([1, 2]) # Randomly choose between two routes
    print(f"\tUsing route {route}") 
    if route == 1: # Route 1
        go_to_fishing_spot_undella_town_1()
    elif route == 2: # Route 2
        go_to_fishing_spot_undella_town_2()
    return route
    
    
def go_to_fishing_spot_undella_town_1():
    hold_key(key.DOWN, rnd.uniform(0.4, 0.6)) # Down    
    hold_key(key.LEFT, rnd.uniform(0.85, 0.9)) # Left      
    hold_key(key.DOWN, rnd.uniform(1, 1.2)) # Down
    

def go_to_fishing_spot_undella_town_2():
    hold_key(key.DOWN, rnd.uniform(0.4, 0.6)) # Down    
    hold_key(key.LEFT, rnd.uniform(0.8, 0.9)) # Left      
    hold_key(key.DOWN, rnd.uniform(0.25, 0.35)) # Down
    hold_key(key.RIGHT, rnd.uniform(0.45, 0.55)) # Right  
    hold_key(key.DOWN, rnd.uniform(0.2, 0.3)) # Down


def fish():
    count = 0
    while True:
        count += 1
        press_key(key.SUPER_ROD) # Throw the rod
        time.sleep(rnd.uniform(4, 4.5)) # Wait for the dialog to appear
        text = screen.get_text(POS_FICHING_DIALOG_X1, POS_FICHING_DIALOG_Y1,
                               POS_FICHING_DIALOG_X2, POS_FICHING_DIALOG_Y2) # Read the dialog in the screen
        press_key(key.A) # Confirm dialog
        if re.search(FISH_APEARED_TEXT, text) or count >= 20: # Check if fish appeared or its an infinite loop
            break # Exit the loop      
    time.sleep(rnd.uniform(12, 13)) # Wait for the fish to appear


def fight():
    check_shiny() # Check if shiny appeared
    press_key(key.A) # Select fight
    time.sleep(rnd.uniform(0.5, 1)) # Small wait
    press_key(key.A) # Selct Pay day
    time.sleep(rnd.uniform(12, 13)) # Wait for the fight to end
    
    
def check_shiny():
    text = screen.get_text(POS_POKEMON_NAME_X1, POS_POKEMON_NAME_Y1,
                           POS_POKEMON_NAME_X2, POS_POKEMON_NAME_Y2) # Read the Pokemon name in the screen
    if text: 
        '''re.search(SHINY_APEARED_TEXT_1, text) or re.search(SHINY_APEARED_TEXT_2, text): # Check if shiny appeared'''
        print("-----------------------")
        print("Shiny Pokemon appeared!")
        print("-----------------------")
        sound.alarm() # Play alarm sound
        input("Press Enter to exit...")
        sys.exit(0) # Exit the script
    
def go_back_to_pokemon_center_undella_town(route):
    if route == 1:
        go_back_to_pokemon_center_undella_town_1()
    elif route == 2:
        go_back_to_pokemon_center_undella_town_2()


def go_back_to_pokemon_center_undella_town_1():
    hold_key(key.UP, rnd.uniform(1.1, 1.2)) # Up 
    hold_key(key.RIGHT, rnd.uniform(0.9, 0.95)) # Right 
    hold_key(key.UP, rnd.uniform(0.6, 0.8)) # UP   
    

def go_back_to_pokemon_center_undella_town_2():
    hold_key(key.UP, rnd.uniform(0.4, 0.6)) # Up    
    hold_key(key.LEFT, rnd.uniform(0.45, 0.5)) # Left      
    hold_key(key.UP, rnd.uniform(0.4, 0.5)) # Up
    hold_key(key.RIGHT, rnd.uniform(0.8, 0.9)) # Right  
    hold_key(key.UP, rnd.uniform(0.4, 0.6)) # Up 


# Main
start()
loopCount = 0
while loopCount < TIMES_FISHING_LOOP:
    loopCount += 1
    print(f"Loop [{loopCount}]:")
    heal_pokemon_center_unova() # Heal Pokemons
    exit_pokemon_center_unova() # Exit Pokemon center
    route = go_to_fishing_spot_undella_town() # Go to fishing spot
    for i in range(PP): # Farm until PP run out
        print(f"\tFishing [{i + 1}]")
        fish() # Fish until a Pokemon appears
        fight() # Fight the Pokemon
    go_back_to_pokemon_center_undella_town(route) # Go to Pokemon center
    print("--------------")
input("Script finished. Press Enter to exit...")
