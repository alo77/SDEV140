"""
Program: Review Game
Author: Abigail Logan
Date: 02/28/2025
Short Description: This program is a review game that uses a JSON file to store the prompts and answers.
It uses science review prompts from sciencecourse2-3.json.
"""

import json
import tkinter as tk
from breezypythongui import EasyFrame

class ReviewGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Science Review Game", width=500, height=400)
        self.score = 0
        self.createWidgets()
    
    def createWidgets(self):
        # Create a score widget at the top-right
        self.score_label = tk.Label(self, text=f"Score: {self.score}")
        self.score_label.pack(side="top", anchor="ne", padx=10, pady=10)
        
        self.question_label = tk.Label(self, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.answer_frame = tk.Frame(self)
        self.answer_frame.pack(pady=20)

        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)
    
    def load_game_data(self):
        with open("sciencecourse2-3.json", "r") as f:
            return json.load(f)
    
    def display_question(self, question_data):
        # Clear any existing answer widgets
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
        
        self.question_label.config(text=question_data["question"])

        q_type = question_data.get("type", "").lower()
        if q_type == "selecting":
            self.selecting(question_data)
        elif q_type == "sequencing":
            self.sequencing(question_data)
        elif q_type == "true or false":
            self.true_or_false(question_data)
        else:
            raise ValueError(f"Unknown question type: {q_type}")

    def selecting(self, question_data):
        options = question_data.get("options", [])
        self.check_vars = []
        for i, option in enumerate(options):
            var = tk.IntVar()
            chk = tk.Checkbutton(self.answer_frame, text=option["text"], variable=var)
            chk.grid(row=i, column=0, sticky="w", padx=5, pady=2)
            self.check_vars.append(var)
        submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_answer)
        submit_button.grid(row=len(options), column=0, pady=10)

    def sequencing(self, question_data):
        # Display each option with an entry box for the user to input the order number.
        options = question_data.get("options", [])
        self.seq_entries = []
        for i, option in enumerate(options):
            label = tk.Label(self.answer_frame, text=option["text"])
            label.grid(row=i, column=0, padx=5, pady=2, sticky="w")
            entry = tk.Entry(self.answer_frame, width=5)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.seq_entries.append(entry)
        submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_answer)
        submit_button.grid(row=len(options), column=0, columnspan=2, pady=10)

    def true_or_false(self, question_data):
        options = question_data.get("options", [])
        self.tf_var = tk.StringVar()
        for i, option in enumerate(options):
            radio = tk.Radiobutton(self.answer_frame, text=option["text"],
                                   variable=self.tf_var, value=option["text"])
            radio.grid(row=0, column=i, padx=5)
        submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_answer)
        submit_button.grid(row=1, column=0, columnspan=len(options), pady=10)

    def submit_answer(self):
        # Placeholder for answer-checking logic.
        # For demonstration, we add 1 point for each submitted answer.
        self.update_score(1)
        print("Answer submitted. Current score:", self.score)

    def update_score(self, points):
        self.score += points
        self.score_label.config(text=f"Score: {self.score}")

    def start_game(self):
        self.game_data = self.load_game_data()
        self.score = 0  # Reset score at the start
        self.update_score(0)
        first_module = self.game_data[0]
        first_question_data = first_module["questions"][0]
        print("Loaded question:", first_question_data["question"])
        self.display_question(first_question_data)
        self.start_button.pack_forget()

        self.next_button = tk.Button(self, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=20)

    def next_question(self):
        # Placeholder for advancing to the next question.
        print("Next question button pressed.")

def main():
    ReviewGame().mainloop()

if __name__ == "__main__":
    main()
