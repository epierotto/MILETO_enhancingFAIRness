import sys

import customtkinter as ctk

from src.gui.controller import Controller
from src.gui.model import Model
from src.gui.view import View
from src.utils.utils import resource_path
from src.utils.utils_gui import get_zoomed_geometry


def main_gui():
    model = Model()
    ctk.set_appearance_mode("dark")
    if sys.platform.startswith("linux"):
        geometry = get_zoomed_geometry()
        view = View()
        view.geometry(geometry)
    else:
        view = View()
        view._state_before_windows_set_titlebar_color = "zoomed"

    view.after(201, lambda: view.iconbitmap(resource_path("assets/logo.ico")))
    controller = Controller(model, view)
    view.set_controller(controller)
    view.mainloop()


if __name__ == "__main__":
    main_gui()
