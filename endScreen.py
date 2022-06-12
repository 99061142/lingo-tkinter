from window import Window
import tkinter as tk

class endScreen(Window):
    def __init__(self):
        super().__init__()
        self._end_frame = None

    def end_frame(self):
        reset_frame = tk.Frame(
            self._board_frame,
            bg=self._light_gray,
            padx=50,
            pady=25,
        )
        reset_frame.grid(row=0)
        reset_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Reset frame centered above board frame

        self._end_frame = reset_frame

    def end_label(self):
        tk.Label(
            self._end_frame,
            text="Game over",
            font=("Helvetica 15"),
            background=self._light_gray,
            foreground=self._red,
        ).grid(pady=25)

    def reset_button(self):
        tk.Button(
            self._end_frame,
            text="Play again",
            font=("Helvetica 15"),
            background=self._incorrect,
            foreground=self._green,
            command=lambda: self.restart(),
        ).grid()

    def end_screen(self):
        self.end_frame()
        self.end_label()
        self.reset_button()