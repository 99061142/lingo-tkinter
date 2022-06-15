if __name__ == "__main__":
    error_message = "Start this program with the \"start.py\" file"
    print(f"\033[1;31m{error_message}\033[0m")
    exit()
else:
    from lib.lib import *

class EndScreen(Window):
    def __init__(self):
        super().__init__()

    def end_message(self) -> dict:
        if(self.word_guessed()):
            return {
                'message': "You won!",
                'color': self.green
            }
        else:
            return {
                'message': f"YOU LOST! \n The word was: {self.word}",
                'color': self.red
            }

    def end_frame(self):
        end_frame = tk.Frame(
            self.board_frame,
            bg=self.light_gray,
            padx=50,
            pady=25
        )

        # Frame centered above board frame
        end_frame.grid(
            row=0
        )
        end_frame.place(
            relx=0.5,
            rely=0.5, 
            anchor=tk.CENTER
        )

        return end_frame

    def end_label(self, end_frame):
        end_message = self.end_message()
        
        tk.Label(
            end_frame,
            text=end_message['message'],
            font=("Helvetica 15"),
            background=self.light_gray,
            foreground=end_message['color']
        ).grid(
            pady=25
        )

    def end_button(self, end_frame):
        tk.Button(
            end_frame,
            text="Play again",
            font=("Helvetica 15"),
            background=self.incorrect,
            foreground=self.green,
            command=lambda: self.restart()
        ).grid()

    def end_screen(self):
        end_frame = self.end_frame()
        self.end_label(end_frame)
        self.end_button(end_frame)