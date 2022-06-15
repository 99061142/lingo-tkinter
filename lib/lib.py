if __name__ == "__main__":
    error_message = "Start this program with the \"start.py\" file"
    print(f"\033[1;31m{error_message}\033[0m")
    exit()

try:
    # Standard libraries
    import sys
    import os
    import json
    import tkinter as tk
    from tkinter import ttk
    from random import choice 
    
    # Set every folder to the path of main file
    folders = ["classes", "modules", "storage" ]

    for folder in folders:
        sys.path.append(os.path.abspath(os.path.join('..', folder)))

    # MODULES
    import modules.word as word

    # CLASSES
    # NOTE: The imports must be in the same order as the hierachy 
    from classes.topHierachy import Type
    
    from classes.scores import Scores
    
    from classes.window import Window
    
    from classes.endScreen import EndScreen
    from classes.error import Error
    from classes.board import Board
    from classes.keyboard import Keyboard

    from classes.app import App
except ModuleNotFoundError as e:
    error_message = str(e) + ", or the module is not installed"
    print("\033[1;31m" + error_message + "\033[0m")
    exit()