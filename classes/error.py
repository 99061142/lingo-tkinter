from classes.window import Window
import tkinter as tk

class Error(Window):
    def __init__(self):
        super().__init__()

    def create_error_frame(self):
        # Delete the old error message if it exists 
        try:
            self._error_frame.destroy()
        except AttributeError:
            pass
        finally:
            error_frame = tk.Frame(
                self.board_frame,
                bg=self.light_gray,
                pady=5,
            )
            error_frame.grid(row=0)
            self._error_frame = error_frame
            error_frame.after(2000, lambda: error_frame.grid_forget()) # Remove the error message after x seconds

    def error_text(self, message:str):
        tk.Label(
            self._error_frame,
            text=message,
            font=("Helvetica 15"),
            background=self.light_gray,
            foreground=self.red,
        ).grid()

    def show_error(self, message:str):
        self.create_error_frame()
        self.error_text(message)