"""
Program: Review Game
Author: Abigail Logan
Date: 02/28/2025
Short Description: This program is a review game that uses a json file to store the prompts and answers. This program is using science review promtps from sciencecourse2-3.json.
"""

import json
import tkinter as tk
from breezypythongui import EasyFrame

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
    
    def load_game_data():
        with open("sciencecourse2-3.json", "r") as f:
            return json.load(f)
        
    def display_question(self, question_data):
        # Clear any existing answer widgets
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
        
        self.question_label.config(text=question_data["question"])

        type = question_data.get("type", "").lower()

        if type == "selecting":
            self.selecting(question_data)
        elif type == "sequencing":
            self.sequencing(question_data)
        elif type == "true or false":
            self.true_or_false(question_data)
        else:
            raise ValueError(f"Unknown question type: {type}")
        
        def selecting(question_data):
            correct_order = question_data["correct_order"]
            for i, word in enumerate(correct_order):
                label = tk.Label(answer_frame, text=word)
                label.grid(row=0, column=i)

            submit_button = tk.Button(answer_frame, text="Submit")
            submit_button.grid(row=1, columnspan=len(correct_order))

            for i, word in enumerate(correct_order):
                var = tk.StringVar()
                radio_button = tk.Radiobutton(answer_frame, text=word, variable=var, value=word)
                radio_button.grid(row=1, column=i)

        def sequencing(question_data):
            correct_order = question_data["correct_order"]
            for i, word in enumerate(correct_order):
                label = tk.Label(answer_frame, text=word)
                label.grid(row=0, column=i)

            submit_button = tk.Button(answer_frame, text="Submit")
            submit_button.grid(row=1, columnspan=len(correct_order))

            for i, word in enumerate(correct_order):
                var = tk.StringVar()
                radio_button = tk.Radiobutton(answer_frame, text=word, variable=var, value=word)
                radio_button.grid(row=1, column=i)

        def true_or_false(question_data):
            correct_order = question_data["correct_order"]
            for i, word in enumerate(correct_order):
                label = tk.Label(answer_frame, text=word)
                label.grid(row=0, column=i)

            submit_button = tk.Button(answer_frame, text="Submit")
            submit_button.grid(row=1, columnspan=len(correct_order))

            for i, word in enumerate(correct_order):
                var = tk.StringVar()
                radio_button = tk.Radiobutton(answer_frame, text=word, variable=var, value=word)
                radio_button.grid(row=1, column=i)

        def start_game():
            self.game_data = load_game_data()
            first_module = self.game_data[0]
            first_question = first_module["questions"][0]["question"]
            print("Loaded question:", first_question)
            self.question_label.config(text=first_question)
            self.display_question(first_module["questions"][0])

            self.start_button.pack_forget()

            next_button = tk.Button(self, text="Next Question", command=self.next_question)
            next_button.pack(pady=20)

        def next_question(self):
            print("Next question")
            self.display_question(self.game_data[0]["questions"][0])

def main():
    ReviewGame().mainloop()

if __name__ == "__main__":
    main()
