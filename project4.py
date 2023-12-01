import tkinter as tk
from tkinter import messagebox
import random
import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='canditates_detail',
            user='root',
            password=''
        )
        return connection

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                player_choice VARCHAR(255),
                player2_choice VARCHAR(255),
                result VARCHAR(255)
            )
        ''')
        connection.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")


def play_game_and_store_result(player_choice):
    options = ["stone", "paper", "scissors"]


    player2_choice = random.choice(options)

    result = ""


    if player_choice == player2_choice:
        result = "It's a tie!"
    elif (
            (player_choice == "stone" and player2_choice == "scissors") or
            (player_choice == "paper" and player2_choice == "stone") or
            (player_choice == "scissors" and player2_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    # Display the result
    messagebox.showinfo("Result", f"Your choice: {player_choice}\nplayer2_choice: {player2_choice}\n\n{result}")

    # Store the game data in the database
    try:
        cursor = connection.cursor()
        insert_query = '''
            INSERT INTO game_data (player_choice, player2_choice, result)
            VALUES (%s, %s, %s)
        '''
        data = (player_choice, player2_choice, result)
        cursor.execute(insert_query, data)
        connection.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")

root = tk.Tk()
root.title("Stone Paper Scissors")

connection = connect_to_database()
if connection:
    create_table(connection)


stone_button = tk.Button(root, text="Stone", command=lambda: play_game_and_store_result("stone"))
stone_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game_and_store_result("paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game_and_store_result("scissors"))
scissors_button.pack(pady=10)
root.mainloop()


if connection:
    connection.close()
    print("MySQL Database connection closed")
