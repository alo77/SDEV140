import tkinter as tk
import json

def load_game_data():
    with open("sciencecourse2-2.json", "r") as f:
      return json.load(f)

def start_game():
    game_data = load_game_data()
    first_module = game_data[0]
    first_question = first_module["questions"][0]["question"]
    print("Loaded questiON:", first_question)
    question_label.config(text=first_question)

root = tk.Tk()
root.title("Science Review Game")

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=20)

question_label = tk.Label(root, text="", wraplength=400)
question_label.pack(pady=20)

root.mainloop()
