if __name__ == "__main__":
    error_message = "Start this program with the \"start.py\" file"
    print(f"\033[1;31m{error_message}\033[0m")
    exit()
else:
    from lib.lib import *

class Board(Window):
    def __init__(self): 
        super().__init__()
        self.max_rounds = 5
        self.new_board()

    def new_board(self):
        self.round = 1
        self.word_guesses = []
        self.board_labels = [{} for i in range(self.max_rounds)]
        self.word = word.random_word()
        self.board_columns_chars = [[tk.StringVar() for i in range(self.get_word_length())] for i in range(self.max_rounds)]
        self.board()

    def board(self): 
        self.create_board_frame()   
        self.create_board_rows()

    def get_current_word_list(self) -> list:
        return [char.get() for char in self.board_columns_chars[self.round - 1]] # Current row word list in the board

    def get_current_word(self) -> str:
        return ''.join(self.get_current_word_list()) # Current row word in the board

    def get_word_length(self) -> int:
        return len(self.word)

    def word_guessed(self) -> bool:
        return self.get_current_word() == self.word

    def create_board_frame(self):
        # Delete the columns inside the board if the board already exitst, else create a new board
        try:
            for widget in self.board_frame.winfo_children():
                widget.destroy()
        except AttributeError:
            board_frame = tk.Frame(
                self, 
                bg=self.window_color, 
                pady=25
            )
            board_frame.grid(
                row=0
            )
            board_frame.place(
                relx=0.5, 
                rely=0.35, 
                anchor=tk.CENTER
            )
            self.board_frame = board_frame

    def create_board_rows(self): 
        # For every round
        for row in range(self.max_rounds):
            board_row = tk.Frame(
                self.board_frame,
                bg=self.window_color, 
                pady=3
            )
            board_row.grid()
            board_row.pack_propagate(0) # Set fixed size

            for col in range(self.get_word_length()):
                label_frame = tk.Frame(
                    board_row, 
                    width=50, 
                    height=50,
                    background=self.column_background
                )
                label_frame.pack_propagate(0) # Set fixed size
                
                label = ttk.Label(
                    label_frame,
                    textvariable=self.board_columns_chars[row][col],
                    font=("Helvetica 15"),  
                    background=self.column_background, 
                    foreground=self.white
                )
                label.pack(
                    expand=True
                )
    
                label_frame.grid(
                    row=row, 
                    column=col, 
                    padx=5
                )

                self.board_labels[row][col] = {
                    "frame": label_frame,
                    "label": label
                }

    def del_char_from_board(self, index:int):       
        self.board_columns_chars[self.round - 1][index - 1].set('')

    def add_char_to_board(self, index:int, char:str):
        self.board_columns_chars[self.round - 1][index].set(char)

    def get_first_empty_index(self):
        word_list = self.get_current_word_list()

        if '' in word_list:
            return word_list.index('') 

    def check_characters(self):
        correct_word = self.word

        # Change the styling of the keys / board columns based on the guessed character
        for index, (correct_char, char) in enumerate(zip(self.word, self.get_current_word())):            
            if char == correct_char:
                color = self.green
            elif char in correct_word:
                color = self.yellow
            else:
                color = self.incorrect
                
            self.button_config(char, color)
            self.label_config(index, color)

            if char in correct_word:
                correct_word = correct_word.replace(char, '')

    def label_config(self, index:int, color:str):
        for label_data in self.board_labels[self.round - 1][index].values():
            label_data.config(background=color)