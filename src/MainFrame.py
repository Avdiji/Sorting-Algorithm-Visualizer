import random
import tkinter
from tkinter import Tk, Frame, Button, ttk, StringVar, Canvas
import random
import time

# WIDTH and HEIGHT of the MainFrame
MF_WIDTH = 1300
MF_HEIGHT = 870

# Button WIDTH/HEIGHT for the Algorithm - Buttons
ALGORITHM_BUTTONS_WIDTH = 15
ALGORITHM_BUTTONS_HEIGHT = 3

# WIDTH and HEIGHT of the Canvas
HEIGHT_CANVAS = 700
WIDTH_CANVAS = 1000

mainFrame = Tk()
canvas = Canvas(mainFrame, width=WIDTH_CANVAS, height=HEIGHT_CANVAS, bg="#ABC")

bars = []


#################################################################
# Function renders the Canvas and draws all the bars
#################################################################
def render_bars():
    canvas.delete("all")
    bar_width = int(WIDTH_CANVAS / len(bars))

    for _ in range(0, len(bars)):
        canvas.create_rectangle(
            _ * bar_width, HEIGHT_CANVAS,
            (_ * bar_width) + bar_width,
            HEIGHT_CANVAS - bars[_],
            fill="red")


#################################################################
# Function generates the bar - values
#################################################################
def generate_bars(*args):
    maximum = int(float(args[0]))
    bars.clear()

    for _ in range(0, maximum):
        bars.append(random.randint(0, HEIGHT_CANVAS - 50))

    render_bars()


############################################################################################################
# SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS
# SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS
# SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS
############################################################################################################
def bubble_sort():
    n = len(bars)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if bars[j] > bars[j + 1]:
                bars[j], bars[j + 1] = bars[j + 1], bars[j]

    render_bars()

############################################################################################################
# SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS
# SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS
# SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS
############################################################################################################


#################################################################
# parameters
#   - parent: parent of the GUI objects in this Function
#
# Function creates the "control buttons" (faster, slower, sort...)
#################################################################
def init_button_controls(parent):
    ttk.Scale(parent, length=250, from_=10, to=100, orient="horizontal",
              command=generate_bars).grid(row=0, column=0, padx=5, pady=10)

    Button(parent, width=10, text="<<<").grid(row=0, column=1, padx=(10, 0), pady=10)
    Button(parent, width=10, text=">>>").grid(row=0, column=2, padx=(0, 10), pady=10)

    Button(parent, width=25, height=2, text="Sort!").grid(row=0, column=3, padx=(50, 0), pady=10)
    Button(parent, width=25, height=2, text="Reset!").grid(row=0, column=4, padx=0, pady=10)


#################################################################
# parameters
#   - parent: parent of the GUI objects in this Function
#
# Function creates the buttons, that enable the sorting algorithms
#################################################################
def init_button_sortingAlgorithms(parent):
    Button(parent, width=ALGORITHM_BUTTONS_WIDTH, height=ALGORITHM_BUTTONS_HEIGHT, text="Bubble Sort",
           command=bubble_sort) \
        .grid(row=0, column=0, padx=50)

    Button(parent, width=ALGORITHM_BUTTONS_WIDTH, height=ALGORITHM_BUTTONS_HEIGHT, text="Insertion Sort") \
        .grid(row=1, column=0, padx=50)

    Button(parent, width=ALGORITHM_BUTTONS_WIDTH, height=ALGORITHM_BUTTONS_HEIGHT, text="Selection Sort") \
        .grid(row=2, column=0, padx=50)


#################################################################
# Function initializes and runs the GUI
#################################################################
def initWindow():
    button_controls = Frame(mainFrame)
    button_controls.pack(side="bottom")

    algorithm_buttons = Frame(mainFrame)
    algorithm_buttons.pack(side="left")

    canvas.pack(pady=50)

    init_button_sortingAlgorithms(algorithm_buttons)
    init_button_controls(button_controls)

    mainFrame.geometry(f"{MF_WIDTH}x{MF_HEIGHT}")
    mainFrame.mainloop()


initWindow()
