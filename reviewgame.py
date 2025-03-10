"""
Program: Review Game
Author: Abigail Logan
Date: 02/28/2025
Short Description: This program is a review game that uses a JSON file to store the prompts and answers. It uses science review prompts from sciencecourse2-3.json.
"""

import json
import tkinter as tk
from breezypythongui import EasyFrame

# ----------------------------
# ReviewGame class
# ----------------------------
class ReviewGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Science Review Game", width=1200, height=1200)
        self.primary_color = "#4CAF50"    # Green
        self.secondary_color = "#FFFFFF"  # White
        self.configure(background=self.primary_color)
        self.score = 0
        self.game_data = None
        self.all_questions = []  # List to store all questions
        self.current_question_index = 0
        self.createWidgets()
    
    def createWidgets(self):
        self.score_label = tk.Label(self, text=f"Score: {self.score}", bg=self.primary_color, fg=self.secondary_color)
        self.score_label.pack(side="top", anchor="ne", padx=10, pady=10)
        
        self.question_label = tk.Label(self, text="", wraplength=400, bg=self.primary_color, fg=self.secondary_color)
        self.question_label.pack(pady=20)

        self.answer_frame = tk.Frame(self, background=self.primary_color)
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
        # Save current question data for use in submit_answer()
        self.current_question = question_data

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
            chk = tk.Checkbutton(self.answer_frame, text=option["text"], variable=var, bg=self.primary_color, fg=self.secondary_color)
            chk.grid(row=i, column=0, sticky="w", padx=5, pady=2)
            self.check_vars.append(var)
        submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_answer)
        submit_button.grid(row=len(options), column=0, pady=10)

    def sequencing(self, question_data):
        options = question_data.get("options", [])
        self.seq_entries = []
        for i, option in enumerate(options):
            label = tk.Label(self.answer_frame, text=option["text"], bg=self.primary_color, fg=self.secondary_color)
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
                                   variable=self.tf_var, value=option["text"], bg=self.primary_color, fg=self.secondary_color)
            radio.grid(row=0, column=i, padx=5)
        submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_answer)
        submit_button.grid(row=1, column=0, columnspan=len(options), pady=10)

    def submit_answer(self):
        q_type = self.current_question.get("type", "").lower()
        is_correct = False
    
        if q_type == "selecting":
            # Handles json "correct" key true/false
            is_correct = True
            for var, option in zip(self.check_vars, self.current_question["options"]):
                if bool(var.get()) != option.get("correct", False):
                    is_correct = False
                    break
        elif q_type == "sequencing":
            try:
                user_order = [int(entry.get()) for entry in self.seq_entries]
                correct_order = [option.get("order") for option in self.current_question["options"]]
                is_correct = (user_order == correct_order)
            except ValueError:
                is_correct = False  # Non-numeric = incorrect
        elif q_type == "true or false":
            user_answer = self.tf_var.get()
            correct_answer = None
            for option in self.current_question["options"]:
                if option.get("correct", False):
                    correct_answer = option["text"]
                    break
            is_correct = (user_answer == correct_answer)
    
        if is_correct:
            self.update_score(1)
            print("Correct answer submitted. Current score:", self.score)
        else:
            print("Incorrect answer submitted. Score remains:", self.score)


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
            self.question_label.config(text="Congratulations! You've completed the review game.")
            for widget in self.answer_frame.winfo_children():
                widget.destroy()
            self.next_button.config(state=tk.DISABLED)
            show_custom_popup(self, "Game Over", f"Final Score: {self.score}")
            print("Game over. Final Score:", self.score)

# ----------------------------
# Launcher class
# ----------------------------
class Launcher:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Launcher")
        self.master.geometry("600x400")

        try:
            self.photo = tk.PhotoImage(file="rocket2.png")
            self.image_label = tk.Label(master, image=self.photo)
            self.image_label.pack(pady=20)
        except Exception as e:
            print("Error loading image:", e)
            self.image_label = tk.Label(master, text="Launcher Image Not Found")
            self.image_label.pack(pady=20)

# Insert a spacer widget to add 50 pixels of vertical space below the image.
        spacer = tk.Frame(master, height=100)
        spacer.pack()
        
        # Launch Game button
        self.launch_button = tk.Button(master, text="Launch Game", command=self.launch_game, width=20, height=2)
        self.launch_button.pack(pady=20)
    
    def launch_game(self):
        # Close the launcher window and start the game
        self.master.destroy()  # Close launcher
        # Start the game by creating a new instance of ReviewGame.
        game_app = ReviewGame()
        game_app.mainloop()

# ----------------------------
# Main function to run the launcher
# ----------------------------
def main():
    root = tk.Tk()
    launcher = Launcher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
