"""
Program: Review Game ScorekeeperSupport Module
Author: Abigail Logan
Date: 03/04/2025
Short Description: This program assists the review game as a scorekeeper module and popup.
"""

import json
import tkinter as tk
from breezypythongui import EasyFrame

def show_custom_popup(parent, title, message):
    popup = tk.Toplevel(parent)
    popup.title(title)
    popup.geometry("300x200")
    
    title_label = tk.Label(popup, text=title, font=("Helvetica", 14, "bold"))
    title_label.pack(pady=(10, 5))

    confetti_image = tk.PhotoImage(file="confetti.png")
    image_label = tk.Label(popup, image=confetti_image)
    image_label.image = confetti_image
    image_label.pack(pady=10)

    message_label = tk.Label(popup, text=message, wraplength=250)
    message_label.pack(pady=(5,10), padx=20)

    self.score_label = tk.Label(popup, text=f"Score: {self.score}")
    self.score_label.pack(side="top", anchor="ne", padx=10, pady=10)

    ok_button = tk.Button(popup, text="OK", command=popup.destroy)
    ok_button.pack(pady=10)

    popup.transient(parent)
    popup.grab_set()
    popup.wait_window(popup)