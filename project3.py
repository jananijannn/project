import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    options = ["stone", "paper", "scissors"]
    player2_choice = random.choice(options)

    result = ""
    if player_choice == player2_choice:
        result = "It's a tie!"
    elif (
            (player_choice == "stone" and player2_choice == "scissors") or
            (player_choice == "paper" and  player2_choice== "stone") or
            (player_choice == "scissors" and player2_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"Your choice: {player_choice}\n player2 choice: {player2_choice}\n\n{result}")


def on_button_click(choice):
    play_game(choice)

root = tk.Tk()
root.title("Stone Paper Scissors")


stone_button = tk.Button(root, text="Stone", command=lambda: on_button_click("stone"))
stone_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click("paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click("scissors"))
scissors_button.pack(pady=10)


root.mainloop()
