import tkinter
from tkinter import Tk, Frame, Button, ttk, StringVar

MF_WIDTH = 1000
MF_HEIGHT = 700

ALGORITHM_BUTTONS_WIDTH = 15
ALGORITHM_BUTTONS_HEIGHT = 2

mainFrame = Tk()


def get_elements_to_sort(*args):
    print(int(float(args[0])))
    return int(float(args[0]))


def init_button_controls(parent):
    ttk.Scale(parent, length=250, from_=10, to=100, orient="horizontal",
              command=get_elements_to_sort).grid(row=0, column=0, padx=5, pady=10)

    Button(parent, width=10, text="<<<").grid(row=0, column=1, padx=(10, 0), pady=10)
    Button(parent, width=10, text=">>>").grid(row=0, column=2, padx=(0, 10), pady=10)

    Button(parent, width=25, height=2, text="Sort!").grid(row=0, column=3, padx=(50, 0), pady=10)
    Button(parent, width=25, height=2, text="Reset!").grid(row=0, column=4, padx=0, pady=10)


def init_button_sortingAlgorithms(parent):
    Button(parent, width=ALGORITHM_BUTTONS_WIDTH, height=ALGORITHM_BUTTONS_HEIGHT, text="Bubble Sort").grid(row=0,
                                                                                                            column=0)
    Button(parent, width=ALGORITHM_BUTTONS_WIDTH, height=ALGORITHM_BUTTONS_HEIGHT, text="Insertion Sort").grid(row=1,
                                                                                                               column=0)
    Button(parent, width=ALGORITHM_BUTTONS_WIDTH, height=ALGORITHM_BUTTONS_HEIGHT, text="Selection Sort").grid(row=2,
                                                                                                               column=0)


def initWindow():
    button_controls = Frame(mainFrame)
    button_controls.pack(side="bottom")

    algorithm_buttons = Frame(mainFrame)
    algorithm_buttons.pack(side="left")

    init_button_controls(button_controls)
    init_button_sortingAlgorithms(algorithm_buttons)

    mainFrame.geometry(f"{MF_WIDTH}x{MF_HEIGHT}")
    mainFrame.mainloop()


initWindow()
