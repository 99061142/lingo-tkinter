from window import Window
import tkinter as tk

class endScreen(Window):
    def __init__(self):
        super().__init__()

    def end_frame(self):
        end_frame = tk.Frame(
            self.board_frame,
            bg=self.light_gray,
            padx=50,
            pady=25,
        )
        end_frame.grid(row=0)
        end_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Frame centered above board frame
        return end_frame

    def end_label(self, end_frame):
        tk.Label(
            end_frame,
            text="Game over",
            font=("Helvetica 15"),
            background=self.light_gray,
            foreground=self.red,
        ).grid(pady=25)

    def end_button(self, end_frame):
        tk.Button(
            end_frame,
            text="Play again",
            font=("Helvetica 15"),
            background=self.incorrect,
            foreground=self.green,
            command=lambda: self.restart(),
        ).grid()

    def end_screen(self):
        end_frame = self.end_frame()
        self.end_label(end_frame)
        self.end_button(end_frame)