# Harsh Patel
import dearpygui.dearpygui as dpg
import tkinter as tk
from tkinter import filedialog

def load_project():
    pass


def save_project():
    pass

def choose_file(text_box):
    """Creates a pop up menu to choose a file.


    Args:
        text_box (Dpg widget): The widget where current chosen file path is shown.


    Returns:
        text_box (Dpg widget): The widget does not get returned but rather its value is set to the file path.
    """

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select a file")

    root.destroy()
    dpg.set_value(text_box, file_path)

