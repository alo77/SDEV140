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
    popup.geometry("300x100")
    label = tk.Label(popup, text=message)
    label.pack(pady=20)
    ok_button = tk.Button(popup, text="OK", command=popup.destroy)
    ok_button.pack()

    placeholder_image = tk.PhotoImage(width=50, height=50)
    placeholder_image.put("lightgray", to=(0, 0, 50, 50))
                          
    image_label = tk.Label(popup, image=placeholder_image)
    image_label.pack()

    message_label = tk.Label(popup, text=message, wraplength=250)
    message_label.pack(pady=(20, 10), padx=20)

    self.score_label = tk.Label(popup, text=f"Score: {self.score}")
    self.score_label.pack(side="top", anchor="ne", padx=10, pady=10)

    ok_button = tk.Button(popup, text="OK", command=popup.destroy)
    ok_button.pack()

    popup.transient(parent)
    popup.grab_set()
    parent.wait_window(popup)