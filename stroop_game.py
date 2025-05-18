import tkinter as tk
import random
import time
import pandas as pd

# Setup
COLORS = ['red', 'green', 'blue', 'yellow']
NUM_TRIALS = 20
TRIAL = 0
DATA = []
current_font_color = None
start_time = 0

# Functions
def next_trial():
    global TRIAL, current_font_color, start_time

    if TRIAL >= NUM_TRIALS:
        label.config(text="Done!", fg="black")
        save_results()
        return

    word = random.choice(COLORS)
    font_color = random.choice(COLORS)
    current_font_color = font_color
    label.config(text=word, fg=font_color)
    start_time = time.time()
    TRIAL += 1

def key_pressed(event):
    global start_time

    rt = time.time() - start_time
    pressed = event.char.lower()
    correct = (pressed == current_font_color[0])
    DATA.append({
        "trial": TRIAL,
        "word_shown": label.cget("text"),
        "font_color": current_font_color,
        "key_pressed": pressed,
        "reaction_time": round(rt, 3),
        "correct": correct
    })

    next_trial()

def save_results():
    df = pd.DataFrame(DATA)
    df.to_csv("stroop_results.csv", index=False)
    print("Results saved to stroop_results.csv")

# GUI setup
root = tk.Tk()
root.title("Stroop Task")

label = tk.Label(root, text="", font=("Helvetica", 48))
label.pack(pady=50)

instructions = tk.Label(root, text="Press the first letter of the FONT COLOR (r/g/b/y)", font=("Helvetica", 14))
instructions.pack()

root.bind("<Key>", key_pressed)
next_trial()

root.mainloop()
