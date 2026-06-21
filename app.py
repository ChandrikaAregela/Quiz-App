import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "Which keyword is used to create a function?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["int", "bool", "str", "float"],
        "answer": "bool"
    },
    {
        "question": "Which loop is used to iterate through a list?",
        "options": ["while", "for", "repeat", "loop"],
        "answer": "for"
    }
]

current_question = 0
score = 0

# Main Window
root = tk.Tk()
root.title("Python Quiz Application")
root.geometry("700x500")
root.config(bg="#1E1E2F")

# Title
title = tk.Label(
    root,
    text="🐍 Python Quiz Challenge",
    font=("Arial", 24, "bold"),
    bg="#1E1E2F",
    fg="#FFD700"
)
title.pack(pady=20)

# Question Frame
frame = tk.Frame(root, bg="#2D2D44", padx=20, pady=20)
frame.pack(pady=20, fill="both", expand=True, padx=30)

# Question Label
question_label = tk.Label(
    frame,
    text="",
    font=("Arial", 16, "bold"),
    bg="#2D2D44",
    fg="white",
    wraplength=600
)
question_label.pack(pady=15)

selected_option = tk.StringVar()

radio_buttons = []

for i in range(4):
    rb = tk.Radiobutton(
        frame,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 13),
        bg="#2D2D44",
        fg="white",
        activebackground="#2D2D44",
        activeforeground="#00FFCC",
        selectcolor="#444466"
    )
    rb.pack(anchor="w", pady=5)

    radio_buttons.append(rb)

# Progress Label
progress_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#1E1E2F",
    fg="#00FFCC"
)
progress_label.pack()

def load_question():
    q = questions[current_question]

    progress_label.config(
        text=f"Question {current_question + 1} of {len(questions)}"
    )

    question_label.config(text=q["question"])

    selected_option.set("")

    for i in range(4):
        radio_buttons[i].config(
            text=q["options"][i],
            value=q["options"][i]
        )

def next_question():
    global current_question, score

    answer = selected_option.get()

    if answer == "":
        messagebox.showwarning(
            "Warning",
            "Please select an option!"
        )
        return

    if answer == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        percentage = (score / len(questions)) * 100

        if percentage >= 70:
            msg = f"🎉 Excellent!\n\nScore: {score}/{len(questions)}"
        elif percentage >= 50:
            msg = f"😊 Good Job!\n\nScore: {score}/{len(questions)}"
        else:
            msg = f"📚 Keep Practicing!\n\nScore: {score}/{len(questions)}"

        messagebox.showinfo("Quiz Completed", msg)

        root.destroy()

# Next Button
next_btn = tk.Button(
    root,
    text="Next ➜",
    command=next_question,
    font=("Arial", 14, "bold"),
    bg="#00C896",
    fg="white",
    activebackground="#00A67D",
    padx=20,
    pady=8,
    relief="flat"
)
next_btn.pack(pady=20)
load_question()
root.mainloop()