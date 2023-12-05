import tkinter as tk
import random
from tkinter import messagebox

class WordGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")

        #Variables which I am going to use here.
        self.words = ["python", "programming", "tkinter", "developer", "keyboard", "mouse", "computer", "coding"]
        self.score = 0
        self.timer_seconds = 30

        #Gui Components I am going to use below.
        self.label_title = tk.Label(root, text="Word Guessing Game", font=("Helvetica", 16))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_score = tk.Label(root, text="Score: 0")
        self.label_score.grid(row=1, column=0, columnspan=2)

        self.label_timer = tk.Label(root, text=f"Time Remaining: {self.timer_seconds}s")
        self.label_timer.grid(row=2, column=0, columnspan=2)

        self.label_word = tk.Label(root, text="")
        self.label_word.grid(row=3, column=0, columnspan=2, pady=20)

        self.entry_guess = tk.Entry(root)
        self.entry_guess.grid(row=4, column=0, columnspan=2, pady=10)

        self.button_guess = tk.Button(root, text="Guess", command=self.check_guess)
        self.button_guess.grid(row=5, column=0, columnspan=2, pady=10)

        # Now we have to start the game.
        self.start_game()

    def start_game(self):
        self.root.after(1000, self.update_timer)
        self.next_word()

    def next_word(self):
        # Now we have to pick a random word from the list
        word_to_guess = random
        # Now we have to shuffle the word.
        shuffled_word = ''.join(random.sample(word_to_guess, len(word_to_guess)))

        # Now we have to display the shuffled word.
        self.label_word.config(text=shuffled_word)

        # Now we have to reset the entry field.
        self.entry_guess.delete(0, tk.END)

        # Now we have to focus on the entry field.
        self.entry_guess.focus()

        # Now we have to update
        self.label_score.config(text=f"Score: {self.score}")

        # Now we have to schedule the next word after 5000 miliseconds (5 seconds)
        self.root.after(5000, self.next_word)

    def update_timer(self):
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.label_timer.config(text=f"Time Remaining: {self.timer_seconds}")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def check_guess(self):
        guessed_word = self.entry_guess.get().lower()
        current_word = self.label_word.cget("text")

        if guessed_word == current_word:
            self.score += 1
            messagebox.showinfo("Correct!", "Good Job ! You gussed it right.")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct word was {current_word}'.")
    
    def end_game(self):
        messagebox.showinfo("Game Over", f"Game Over! Your final score is {self.score}.")
        self.root.destroyed()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordGuessingGame(root)
    root.mainloop()

    