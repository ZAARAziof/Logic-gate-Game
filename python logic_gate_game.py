import tkinter as tk
from tkinter import messagebox
import random

# Logic gate questions and answers
gate_data = [
    {"question": "Which logic gate outputs 1 only when BOTH inputs are 1?", "answer": "AND"},
    {"question": "Which gate outputs 1 if AT LEAST one input is 1?", "answer": "OR"},
    {"question": "Which gate outputs 1 only when inputs are DIFFERENT?", "answer": "XOR"},
    {"question": "Which gate outputs 1 when BOTH inputs are NOT 1?", "answer": "NAND"},
    {"question": "Which gate inverts the input?", "answer": "NOT"},
]

# Shuffle for randomness
random.shuffle(gate_data)

# Game Variables
current_q = 0
score = 0

# GUI setup
root = tk.Tk()
root.title("🧠 Logic Gate Puzzle Game")
root.geometry("600x350")
root.configure(bg="#0d0d0d")

# Title
title = tk.Label(root, text="🟢 Logic Gate Puzzle - Hacker Style", font=("Courier", 18, "bold"), fg="lime", bg="#0d0d0d")
title.pack(pady=15)

# Question Label
question_label = tk.Label(root, text="", font=("Courier", 14), fg="white", bg="#0d0d0d", wraplength=500)
question_label.pack(pady=10)

# Answer Entry
answer_entry = tk.Entry(root, font=("Courier", 14), fg="lime", bg="#1a1a1a", justify="center")
answer_entry.pack(pady=10)

# Feedback
feedback = tk.Label(root, text="", font=("Courier", 12), fg="cyan", bg="#0d0d0d")
feedback.pack()

# Functions
def load_question():
    if current_q < len(gate_data):
        q = gate_data[current_q]["question"]
        question_label.config(text=f"Q{current_q+1}: {q}")
        answer_entry.delete(0, tk.END)
        feedback.config(text="")
    else:
        show_result()

def check_answer():
    global current_q, score
    user_input = answer_entry.get().strip().upper()
    correct = gate_data[current_q]["answer"]

    if user_input == correct:
        score += 1
        feedback.config(text="✅ That's right, queen!", fg="lime")
    else:
        feedback.config(text=f"❌ Nope! The correct answer was: {correct}", fg="red")

    current_q += 1
    root.after(1500, load_question)

def show_result():
    messagebox.showinfo("👑 GAME OVER", f"Your final score: {score}/{len(gate_data)}")
    root.destroy()

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=check_answer, font=("Courier", 12), fg="white", bg="#333")
submit_btn.pack(pady=10)

# Start the game
load_question()
root.mainloop()
