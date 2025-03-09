"""
Program: Review Game ScorekeeperSupport Module
Author: Abigail Logan
Date: 03/04/2025
Short Description: This program assists the review game as a scorekeeper module and popup.
"""

import json
import tkinter as tk
from breezypythongui import EasyFrame
from reviewgame import (
    update_score
)

class ScorekeeperPopup(EasyFrame):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)
        self.geometry("300x200")
        
        title_label = tk.Label(self, text=title, font=("Helvetica", 14, "bold"))
        title_label.pack(pady=(10, 5))

        confetti_image = tk.PhotoImage(file="confetti.png", width=50, height=50)
        image_label = tk.Label(self, image=confetti_image)
        image_label.image = confetti_image
        image_label.put("image", to="center")
        image_label.pack(pady=10)

        message_label = tk.Label(self, text=message, wraplength=250)
        message_label.pack(pady=(5,10), padx=20)

        score_label = tk.Label(self, text=f"Final Score: {update_score}")
        score_label.pack(pady=10)

        ok_button = tk.Button(self, text="OK", command=self.destroy)
        ok_button.pack(pady=10)

        self.transient(parent)
        self.grab_set()
        self.wait_window(self)