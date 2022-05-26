import random
import tkinter
from tkinter import Tk, Frame, Button, ttk, StringVar, Canvas
import random
import time
import threading

# WIDTH and HEIGHT of the MainFrame
MF_WIDTH = 1300
MF_HEIGHT = 810

# Button WIDTH/HEIGHT for the Algorithm - Buttons
ALGORITHM_BUTTONS_WIDTH = 15
ALGORITHM_BUTTONS_HEIGHT = 3

# WIDTH and HEIGHT of the Canvas
HEIGHT_CANVAS = 700
WIDTH_CANVAS = 1000

SLEEP = 0.01

mainFrame = Tk()
canvas = Canvas(mainFrame, width=WIDTH_CANVAS, height=HEIGHT_CANVAS, bg="#ABC")

bars = []


# #################################################################
# # Function renders the Canvas and draws all the bars
# #################################################################
def render_bars():
    canvas.delete("all")
    bar_width = int(WIDTH_CANVAS / len(bars))

    try:
        for _ in range(0, len(bars)):
            canvas.create_rectangle(
                _ * bar_width, HEIGHT_CANVAS,
                (_ * bar_width) + bar_width,
                HEIGHT_CANVAS - bars[_],
                fill="red")
    except IndexError:
        print()


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
class SortingAlgorithm(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self._func = func

    def run(self):
        self._func()


def bubble_sort():
    n = len(bars)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if bars[j] > bars[j + 1]:
                bars[j], bars[j + 1] = bars[j + 1], bars[j]
                render_bars()
                time.sleep(SLEEP)


def insertion_sort():
    for step in range(1, len(bars)):
        key = bars[step]
        j = step - 1
        while j >= 0 and key < bars[j]:
            bars[j + 1] = bars[j]
            j = j - 1
            render_bars()
            time.sleep(SLEEP)
        bars[j + 1] = key


def selection_sort():
    for step in range(len(bars)):
        min_idx = step

        for i in range(step + 1, len(bars)):
            if bars[i] < bars[min_idx]:
                min_idx = i
                render_bars()
                time.sleep(SLEEP)
        (bars[step], bars[min_idx]) = (bars[min_idx], bars[step])
        render_bars()

def start_thread(sortingAlgorithm):
    if sortingAlgorithm == "bubble_sort":
        SortingAlgorithm(bubble_sort).start()
    elif sortingAlgorithm == "insertion_sort":
        SortingAlgorithm(insertion_sort).start()
    elif sortingAlgorithm == "selection_sort":
        SortingAlgorithm(selection_sort).start()
############################################################################################################
# SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS
# SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS
# SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS    SORTING ALGORITHMS
############################################################################################################


#################################################################
# parameters
#   - parent: parent of the GUI objects in this Function
#
# Function creates the buttons, that enable the sorting algorithms
#################################################################
def init_button_sortingAlgorithms(parent):
    Button(parent, width=ALGORITHM_BUTTONS_WIDTH, height=ALGORITHM_BUTTONS_HEIGHT, text="Bubble Sort",
           command=lambda: start_thread("bubble_sort")).grid(row=0, column=0, padx=50)

    Button(parent, width=ALGORITHM_BUTTONS_WIDTH, height=ALGORITHM_BUTTONS_HEIGHT, text="Insertion Sort",
           command=lambda: start_thread("insertion_sort")).grid(row=1, column=0, padx=50)

    Button(parent, width=ALGORITHM_BUTTONS_WIDTH, height=ALGORITHM_BUTTONS_HEIGHT, text="Selection Sort",
           command=lambda: start_thread("selection_sort")).grid(row=2, column=0, padx=50)

    ttk.Scale(parent, length=150, from_=10, to=100, orient="horizontal",
              command=generate_bars).grid(row=3, column=0, padx=5, pady=20)


#################################################################
# Function initializes and runs the GUI
#################################################################
def initWindow():
    algorithm_buttons = Frame(mainFrame)
    algorithm_buttons.pack(side="left")

    canvas.pack(pady=50)

    init_button_sortingAlgorithms(algorithm_buttons)

    mainFrame.geometry(f"{MF_WIDTH}x{MF_HEIGHT}")
    mainFrame.mainloop()


initWindow()
