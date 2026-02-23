# Harsh Patel

import dearpygui.dearpygui as dpg
import tkinter as tk
from tkinter import filedialog

def import_static_image(file_path):
    w, h, channels, data = dpg.load_image(file_path)

    with dpg.texture_registry():
        texture = dpg.add_static_texture(w, h, data)
    return (texture)
