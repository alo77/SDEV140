"""
Program: Review Game
Author: Abigail Logan
Date: 02/28/2025
Short Description: This program is a review game that uses a JSON file to store the prompts and answers. It uses science review prompts from sciencecourse2-3.json.
"""

import json
import tkinter as tk
from breezypythongui import EasyFrame
import tkinter.messagebox as messagebox
from scorekeeperpopup import (
    check_selecting_answer,
    check_sequencing_answer,
    check_true_or_false_answer,
    show_custom_popup
)

class ReviewGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Science Review Game", width=500, height=400)
        self.primary_color = "#4CAF50"    # Green
        self.secondary_color = "#FFFFFF"  # White
        self.configure(background=self.primary_color)

        self.score = 0
        self.game_data = None
        self.all_questions = []  # List to store all questions
        self.current_question_index = 0

        

        self.createWidgets()
    
    def createWidgets(self):
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
    
    def flatten_questions(self):
        # Extract all questions from all modules into one list.
        self.all_questions = []
        for module in self.game_data:
            for question in module["questions"]:
                self.all_questions.append(question)
    
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
        # Optionally, you can set a default value if needed:
        self.tf_var.set("")
        for i, option in enumerate(options):
            radio = tk.Radiobutton(self.answer_frame, text=option["text"],
                               variable=self.tf_var, value=option["text"])
            radio.grid(row=0, column=i, padx=5)
        submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_answer)
        submit_button.grid(row=1, column=0, columnspan=len(options), pady=10)

    def submit_answer(self):
        if self.current_question_index >= len(self.all_questions):
            print("No more questions.")
            return
        
        current_question = self.all_questions[self.current_question_index]
        q_type = current_question.get("type", "").lower().replace(" ", "")
        print("Processing question type:", q_type)

        if q_type == "selecting":
            user_answers = [var.get() for var in self.check_vars]
            if check_selecting_answer(current_question, user_answers)["options"]:
                self.update_score(1)
        elif q_type == "sequencing":
            user_answers = [entry.get() for entry in self.seq_entries]
            if check_sequencing_answer(current_question, user_answers)["options"]:
                self.update_score(1)
        elif q_type == "true or false":
            try:
                user_answer = self.tf_var.get()
            except AttributeError:
                print("Error: tf_var is not defined.")
                return
            
            correct_answer = next((option["text"] for option in current_question["options"] if option["correct"]), None)
            print("User answer:", user_answer, "Correct answer:", correct_answer)
            if correct_answer is not None and check_true_or_false_answer(user_answer, correct_answer):
                self.update_score(1)

            else:
                print(f"Incorrect. Correct answer: {correct_answer}")
                return
            
            print("Answer submitted. Current score:", self.score)

    def update_score(self, points):
        self.score += points
        self.score_label.config(text=f"Score: {self.score}")

    def start_game(self):
        self.game_data = self.load_game_data()
        self.flatten_questions()  # Flatten questions from all modules into one list.
        self.current_question_index = 0
        self.score = 0
        self.update_score(0)
        self.display_question(self.all_questions[self.current_question_index])
        self.start_button.pack_forget()
        self.create_next_button()

    def create_next_button(self):
        self.next_button = tk.Button(self, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=20)

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.all_questions):
            self.display_question(self.all_questions[self.current_question_index])
        else:
            # No more questions: end of game.
            self.question_label.config(text="Congratulations! You've completed the review game.")
            for widget in self.answer_frame.winfo_children():
                widget.destroy()
            self.next_button.config(state=tk.DISABLED)
            # Use the custom popup function from the helper module
            show_custom_popup(self, "Game Over", f"Final Score: {self.score}")
            print("Game over. Final Score:", self.score)
            # Alt display the final score in a popup message.
            # messagebox.showinfo("Game Over", f"Final Score: {self.score}")
            # print("Game over. Final Score:", self.score)

def main():
    ReviewGame().mainloop()

if __name__ == "__main__":
    main()