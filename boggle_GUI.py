import tkinter as tk
import time
from fun_facts import JOKES_AND_FUN_FACTS
import random
import pygame

# initialize pygame mixer, enables to combine music
pygame.mixer.init()

BUTTON_STYLE = {
    'font': ('Arial', 18),
    'bg': 'white',
    'fg': 'black',
    'width': 5,
    'height': 2,
    'activebackground': '#ADD8E6',
    'activeforeground': 'black'
}


class BoggleUI:
    """this class manages the ui part of the game"""
    def __init__(self, add_chars_callback, check_word_callback,
                 delete_word_callback, start_game_callback, end_game_callback):
        """ initialize the GUI object"""
        # Create the root
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.configure(bg='#ADD8E6')#set the background color to light blue

        # Create word label
        self.word_label = tk.Label(self.root, text="", font=("Arial", 20),
                                   bg='#ADD8E6')
        self.word_label.pack()
        self.found_words_label = tk.Label(self.root, text="Words found: ",
                                          font=("Arial", 20), bg='#ADD8E6')
        self.fun_fact_label = tk.Label(self.root, text=random.choice(JOKES_AND_FUN_FACTS),
                                       font=("Ariel", 20), bg='#ADD8E6',pady=100)
        self.secred_sound_buttom = tk.Button(self.root, text='Secret Button',
        command=lambda: [self.secred_sound_buttom.forget(),self.play_sound()])

        # Create a frame for letter buttons
        self.frame = tk.Frame(self.root)
        self.letter_buttons = []

        self.board = None  # will be updated when game starts

        # Connection to the control class
        self.add_chars_callback = add_chars_callback
        self.check_word_callback = check_word_callback
        self.start_game_callback = start_game_callback
        self.delete_word_callback = delete_word_callback
        self.end_game_callback=end_game_callback

        # Button creation
        self.timer_label = tk.Label(self.root, text="", font=("Arial", 20),
                                    bg='#ADD8E6',pady=25)
        self.timer_label.pack_forget()
        self.ready_button = tk.Button(self.root, text="I AM READY", padx=50,
                                      command=self.start_game,**BUTTON_STYLE)
        self.end_game_label = tk.Label(self.root, text="Nicely done!",
                                       font=("Arial", 20), bg='#ADD8E6')
        self.end_game_button = tk.Button(self.root, text="GO AGAIN!",
                                      command=self.end_game)
        self.new_game_button = tk.Button(self.root, text="Restart",**BUTTON_STYLE,
                command=lambda : [self.new_game_button.forget(), self.start_game()])
        self.ready_button.pack()
        self.fun_fact_label.pack()
        self.utility_buttons_and_info()
        try:  # try to add music
            self.sound = pygame.mixer.Sound(r"C:\Users\Meshi Nosrati\Downloads"
                                            r"\Mission-Impossible.mp3")
        except FileNotFoundError:
            self.sound = None
        self.sounds = False


    def main_loop(self):
        """"the main loop that manage the game in GUI"""
        self.root.mainloop()

    def start_game(self):
        """initialize akk the parts we need to start a game"""
        self.fun_fact_label.destroy()
        self.board = self.start_game_callback()
        self.frame.pack()
        self.word_label.pack()
        self.found_words_label.pack()
        self.timer_label.pack()
        self.ready_button.destroy()
        self.create_board_buttons()
        self.start_timer()
        self.found_words_label["text"] = "Words Found: "
        self.score_counter["text"] = "0"
        self.word_label["text"] = ""
        self.sounds = False

    def create_board_buttons(self):
        """
        creates all the letter buttons, and places the buttons in a grid.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                button = tk.Button(self.frame, text=self.board[i][j],**BUTTON_STYLE,
                                   command=lambda letter=(i,j): self.update_word(letter))
                button.grid(row=i, column=j)
                self.letter_buttons.append(button)

    def utility_buttons_and_info(self):
        """ creats "clear", "check" buttons and the score label"""
        self.clear_button = tk.Button(self.frame, text="Del", **BUTTON_STYLE,
                                 command=lambda: self.clear_word())
        self.clear_button.grid(row=5, column=0)
        self.check_button = tk.Button(self.frame, text="Check", **BUTTON_STYLE,
                                 command=self.check_word)
        self.check_button.grid(row=5, column=3)
        self.score_label = tk.Label(self.frame, text="Score:",
                                   font=("Arial", 15), bg='white')
        self.score_label.grid(row=5, column=1)
        self.score_counter = tk.Label(self.frame, text="0",
                               font=("Arial", 17), bg='white')
        self.score_counter.grid(row=5, column=2)

    def check_word(self):
        """
         checks if the player found a valid word if so - update the score
         and clear the word
        """
        found_words,score = self.check_word_callback()  # callback
        if found_words:
            self.found_words_label.config(text=f"Words Found :\n {found_words}")
        self.score_counter.config(text=score)
        self.clear_word()

    def update_word(self, letter):
        """adds new letter that player chose and update it on the board"""
        cur_word = self.add_chars_callback(letter)  # callback
        self.word_label.config(text=cur_word)

    def clear_word(self):
        """delete word from the board"""
        cur_word = self.delete_word_callback() # callback
        self.word_label.config(text=cur_word)

    def start_timer(self):
        """starts counting the time in the beginning of the game. the game ends
        when time arrive to zero"""
        self.end_time = time.time() + 180
        self.countdown()

    def countdown(self):
        """this function checks if the time is over, if yes - shows relevant
        massage and end the game. else - shows how much time is left"""
        remaining = int(self.end_time - time.time())
        if remaining <= 0:
            for button in self.letter_buttons:
                button["state"] = "disabled"
            self.timer_label.config(text="Time's up!")
            self.end_game()
            return
        elif remaining < 171 and not self.sounds:
            self.secred_sound_buttom.pack(side=tk.LEFT)
            self.sounds = True
        self.timer_label.config(text=str(remaining) + " seconds remaining.")
        self.timer_label.after(100, self.countdown)

    def play_sound(self):
        """plays sounds during the game"""
        try:
            self.sound.play()
        except Exception:
            "cant load file."

    def end_game(self):
        """manage the end of the game"""
        self.end_game_callback()  # callback
        self.new_game_button.pack()
        if self.sounds:
            self.sound.stop()




