import tkinter as tk
import json

def load_game_data():
    with open("sciencecourse2-2.json", "r") as f:
      return json.load(f)

def start_game():
    game_data = load_game_data()
    first_module = game_data[0]
    first_question = first_module["questions"][0]["question"]
