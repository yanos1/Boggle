import tkinter as tk
import time
from word_list import JOKES_AND_FUN_FACTS
import random
import pygame

# initialize pygame mixer
pygame.mixer.init()

# load a sound file


# function to play the sound


# create a button to play the sound


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
    def __init__(self,add_chars_callback, check_word_callback,delete_word_callback,start_game_callback,end_game_callback):
        self.root = tk.Tk()
        self.root.geometry("700x600")
        self.root.configure(bg='#ADD8E6') # set the background color to light blue

        # Create word label
        self.word_label = tk.Label(self.root, text="", font=("Arial", 20), bg='#ADD8E6')
        self.word_label.pack()
        self.found_words_label = tk.Label(self.root, text="Words found: ", font=("Arial", 20), bg='#ADD8E6')
        self.fun_fact_label = tk.Label(self.root, text=random.choice(JOKES_AND_FUN_FACTS), font=("Ariel", 20), bg='#ADD8E6',pady=100)
        self.secred_sound_buttom = tk.Button(self.root, text='Secret Button', command= lambda : [self.secred_sound_buttom.forget(),self.play_sound()])


        # Create a frame for letter buttons
        self.frame = tk.Frame(self.root)

        self.letter_buttons = []

        self.board = None
        self.add_chars_callback = add_chars_callback
        self.check_word_callback = check_word_callback
        self.start_game_callback = start_game_callback
        self.delete_word_callback = delete_word_callback
        self.end_game_callback=end_game_callback

        # Create check button


        # Create timer label
        self.timer_label = tk.Label(self.root, text="", font=("Arial", 20), bg='#ADD8E6',pady=25)
        self.timer_label.pack_forget()
        self.ready_button = tk.Button(self.root, text="I AM READY", padx=50,
                                      command=self.start_game,**BUTTON_STYLE)
        self.end_game_label = tk.Label(self.root, text="Nicely done!",font=("Arial", 20), bg='#ADD8E6')
        self.end_game_button = tk.Button(self.root, text="GO AGAIN!",
                                      command=self.end_game)
        self.new_game_button = tk.Button(self.root, text="Restart",**BUTTON_STYLE,
                                      command=lambda : [self.new_game_button.forget(),self.start_game()])
        self.ready_button.pack()
        self.fun_fact_label.pack()
        self.utility_buttons_and_info()
        self.sound = pygame.mixer.Sound(r"C:\Users\Yan Nosrati\Downloads\Mission-Impossible.mp3")

        self.sounds = False


    def main_loop(self):
        self.root.mainloop()

    def start_game(self):
        self.fun_fact_label.destroy()
        self.board = self.start_game_callback()
        self.frame.pack()
        self.word_label.pack()
        self.found_words_label.pack()
        self.timer_label.pack()
        self.ready_button.destroy()
        self.create_board()
        self.start_timer()
        self.found_words_label["text"] = "Words Found: "
        self.score_counter["text"] = "0"
        self.sounds = False

    def create_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                button = tk.Button(self.frame, text=self.board[i][j],**BUTTON_STYLE,
                                   command=lambda letter=(i,j): self.update_word(letter))
                button.grid(row=i, column=j)
                # button.pack_forget()
                self.letter_buttons.append(button)

    def utility_buttons_and_info(self):
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
        found_words,score = self.check_word_callback()
        if found_words:
            self.found_words_label.config(text=f"Words Found :\n {found_words}")
        self.score_counter.config(text=score)
        self.clear_word()

    def update_word(self, letter):
        cur_word = self.add_chars_callback(letter)
        self.word_label.config(text=cur_word)


    def clear_word(self):
        cur_word = self.delete_word_callback()
        self.word_label.config(text=cur_word)



    def start_timer(self):
        self.end_time = time.time() +10
        self.countdown()

    def countdown(self):
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
        self.sound.play()
    def end_game(self):
        self.end_game_callback()
        self.new_game_button.pack()
        self.sound.stop()




