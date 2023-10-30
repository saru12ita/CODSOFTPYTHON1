import tkinter as tk
import random

# Function to determine the winner based on user and computer choices
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Scissors" and computer_choice == "Paper")
        or (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def make_choice(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer's choice: {computer_choice}\n{result}")
    update_score(result)

# Function to update the score
def update_score(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    score_label.config(text=f"Your Score: {user_score}\nComputer Score: {computer_score}")

# Function to play again
def play_again():
    result_label.config(text="")
    user_choice.set("Choose")
    computer_choice.set("Computer's Choice")
    play_button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")
window.configure(bg="purple")

# User and computer choices
user_choice = tk.StringVar()
user_choice.set("Choose")
computer_choice = tk.StringVar()
computer_choice.set("Computer's Choice")

# Labels
title_label = tk.Label(window, text="Rock-Paper-Scissors Game", font=("Arial", 18, "bold"), bg="purple", fg="blue")
title_label.pack(pady=10)

user_label = tk.Label(window, text="Your Choice:", font=("Arial", 14, "bold"), bg="purple", fg="blue")
user_label.pack()
user_option_menu = tk.OptionMenu(window, user_choice, "Rock", "Paper", "Scissors")
user_option_menu.pack()

computer_label = tk.Label(window, textvariable=computer_choice, font=("Arial", 14, "bold"), bg="purple", fg="blue")
computer_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="purple", fg="blue")
result_label.pack(pady=20)

score_label = tk.Label(window, text="Your Score: 0\nComputer Score: 0", font=("Arial", 14, "bold"), bg="purple", fg="blue")
score_label.pack()

play_button = tk.Button(window, text="Play", font=("Arial", 14, "bold"), command=lambda: make_choice(user_choice.get()), bg="blue", fg="white")
play_button.pack()

play_again_button = tk.Button(window, text="Play Again", font=("Arial", 14, "bold"), command=play_again, state=tk.DISABLED, bg="blue", fg="white")
play_again_button.pack()

user_score, computer_score = 0, 0

# Run the application
window.mainloop()
