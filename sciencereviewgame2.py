import tkinter as tk
import json

def load_game_data():
    with open("sciencecourse2-3.json", "r") as f:
      return json.load(f)
    
def display_question(question_data):
    # Clear any existing answer widgets
    for widget in answer_frame.winfo_children():
        widget.destroy()
    
    question_label.config(text=question_data["question"])

    type = question_data.get("type", "").lower()

    if type == "fill-in-the-blanks":
        fill_in_the_blanks(question_data)
    elif type == "ordering":
        ordering(question_data)
    elif type == "matching":
        matching(question_data)
    elif type == "grouping":
        grouping(question_data)
    elif type == "ordering":
        ordering(question_data)
    else:
        raise ValueError(f"Unknown question type: {type}")
    
    answer_frame.pack(pady=20)

def fill_in_the_blanks(question_data):
    sentence = question_data["sentence"]
    for i, word in enumerate(sentence):
        label = tk.Label(answer_frame, text=word)
        label.grid(row=0, column=i)

    entry = tk.Entry(answer_frame)
    entry.grid(row=1, columnspan=len(sentence))

    submit_button = tk.Button(answer_frame, text="Submit")
    submit_button.grid(row=2, columnspan=len(sentence))

def ordering(question_data):
    correct_order = question_data["correct_order"]
    for i, word in enumerate(correct_order):
        label = tk.Label(answer_frame, text=word)
        label.grid(row=0, column=i)

    submit_button = tk.Button(answer_frame, text="Submit")
    submit_button.grid(row=1, columnspan=len(correct_order))

def matching(question_data):
    correct_order = question_data["correct_order"]
    for i, word in enumerate(correct_order):
        label = tk.Label(answer_frame, text=word)
        label.grid(row=0, column=i)

    submit_button = tk.Button(answer_frame, text="Submit")
    submit_button.grid(row=1, columnspan=len(correct_order))

def grouping(question_data):
    correct_order = question_data["correct_order"]
    for i, word in enumerate(correct_order):
        label = tk.Label(answer_frame, text=word)
        label.grid(row=0, column=i)

    submit_button = tk.Button(answer_frame, text="Submit")
    submit_button.grid(row=1, columnspan=len(correct_order))

def ordering(question_data):
    correct_order = question_data["correct_order"]
    for i, word in enumerate(correct_order):
        label = tk.Label(answer_frame, text=word)
        label.grid(row=0, column=i)

    submit_button = tk.Button(answer_frame, text="Submit")
    submit_button.grid(row=1, columnspan=len(correct_order))

answer_frame = tk.Frame(root)

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

# This frame will contain the answer widgets (radio buttons, checkbuttons, listbox, etc.)
answer_frame = tk.Frame(root)
answer_frame.pack(pady=20)

root.mainloop()
