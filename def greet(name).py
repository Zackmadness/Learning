import _random
import random
import keyboard

def greet(name):
    print(name)

names = ["Loser!", "Gibby is Gay!", "Mr. Wire Tripper!", "Gibby!"]

def on_space_press(event):
    greet(random.choice(names))

keyboard.on_press_key("space", on_space_press)

print("Press the spacebar to get a greeting. Press Ctrl+C to exit.")
keyboard.wait("esc")

