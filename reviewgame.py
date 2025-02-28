"""
Program: Review Game
Author: Abigail Logan
Date: 02/28/2025
Short Description: This program is a review game that uses a json file to store the prompts and answers. This program is using science review promtps from sciencecourse2-3.json.
"""

from breezypythongui import EasyFrame
import json

def load_game_data():
    with open("sciencecourse2-3.json", "r") as f:
      return json.load(f)
    
def start_game():
    game_data = load_game_data()
    print(game_data)
    first_module = game_data[0]
    first_question = first_module["questions"][0]["question"]
    print("Loaded question:", first_question)
    question_label.config(text=first_question)
    display_question(first_module["questions"][0])

class ReviewGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Science Review Game", width=500, height=300)
        self.createWidgets()

    def createWidgets(self):
        self.question_label = tk.Label(self, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.answer_frame = tk.Frame(self)
        self.answer_frame.pack(pady=20)

        self.start_button = tk.Button(self, text="Start Game", command=start_game)
        self.start_button.pack(pady=20)