from classes.window import Window
import tkinter as tk

class endScreen(Window):
    def __init__(self):
        super().__init__()

    def end_message(self):
        message = "YOU WON!" if self.word_guessed() else "YOU LOST! \n The word was: " + self.word
        color = self.green if self.word_guessed() else self.red

        end_message = {
            "message": message,
            "color": color,
        }
        return end_message

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
        end_message = self.end_message()
        
        tk.Label(
            end_frame,
            text=end_message['message'],
            font=("Helvetica 15"),
            background=self.light_gray,
            foreground=end_message['color'],
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