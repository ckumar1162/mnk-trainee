from tkinter import *
import requests
from tkinter.simpledialog import askstring
import html
import json  # For persistent storage

# Fetch questions from API
parameters = {
    "amount": 10,
    "difficulty": "medium",
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# Initialize tkinter
tk = Tk()

THEME_COLOR = "#375362"
tk.title("Quizzler")
tk.config(padx=20, pady=20, bg=THEME_COLOR)

# UI setup
score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
score_label.grid(row=0, column=1)

canvas = Canvas(width=300, height=250, bg="white")
question_text = canvas.create_text(
    150, 125,
    width=280,
    text="Some Question Text",
    fill=THEME_COLOR,
    font=("Arial", 20, "italic")
)
canvas.grid(row=1, column=0, columnspan=2, pady=50)

# Placeholder for images
true_image = PhotoImage(file="images/true.png")
true_button = Button(image=true_image, highlightthickness=0, command=lambda: check_answer("True"))
true_button.grid(row=2, column=0)

false_image = PhotoImage(file="images/false.png")
false_button = Button(image=false_image, highlightthickness=0, command=lambda: check_answer("False"))
false_button.grid(row=2, column=1)

# SCOREBOARD
SCORE_FILE = "scores.json"

def load_scores():
    """Load scores from a file."""
    try:
        with open(SCORE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_scores():
    """Save scores to a file."""
    with open(SCORE_FILE, "w") as file:
        json.dump(top_score, file)

top_score = load_scores()

def update_scoreboard(name, score):
    """Update the top scores with the player's name and score."""
    global top_score
    top_score.append((name, score))  # Append a tuple (name, score)
    top_score.sort(key=lambda x: x[1], reverse=True)  # Sort by score in descending order
    top_score = top_score[:5]  # Keep only the top 5 scores
    save_scores()  # Save updated scores to the file
    print("Updated Scoreboard:", top_score)  # Debug print

def display_scoreboard():
    """Display the top scores in a new window."""
    scoreboard_window = Toplevel(tk)
    scoreboard_window.title("Scoreboard")
    scoreboard_window.config(padx=20, pady=20, bg=THEME_COLOR)

    Label(
        scoreboard_window, text="Top 5 Players",
        font=("Arial", 20, "bold"), bg=THEME_COLOR, fg="white"
    ).pack(pady=(10, 5))

    listbox = Listbox(scoreboard_window, font=("Arial", 16), width=30, height=5, bg="white", fg=THEME_COLOR)
    listbox.pack(pady=10)

    listbox.delete(0, END)  # Clear any previous entries

    if not top_score:
        listbox.insert(END, "No scores available yet!")
    else:
        for index, (name, score) in enumerate(top_score, start=1):
            listbox.insert(END, f"{index}. {name}: {score}")

def submit_score():
    """Prompt for the player's name using a Tkinter dialog and update the scoreboard."""
    name = askstring("Player Name", "Enter your name:")
    if name:
        update_scoreboard(name, score)
        display_scoreboard()

# Quiz logic
current_question_index = 0
score = 0

def get_next_question():
    """Display the next question or end the quiz."""
    global current_question_index
    canvas.config(bg="white")
    if current_question_index < len(question_data):
        question = html.unescape(question_data[current_question_index]["question"])
        canvas.itemconfig(question_text, text=question)
    else:
        canvas.itemconfig(question_text, text="You've completed the quiz!")
        true_button.config(state="disabled")
        false_button.config(state="disabled")
        submit_score()  # Allow the player to submit their score

def check_answer(user_answer):
    """Check if the user's answer is correct and update score."""
    global current_question_index, score
    correct_answer = question_data[current_question_index]["correct_answer"]
    if user_answer == correct_answer:
        score += 1
        score_label.config(text=f"Score: {score}")
        canvas.config(bg="green")
    else:
        canvas.config(bg="red")
    current_question_index += 1
    tk.after(1000, get_next_question)

# Start the quiz
get_next_question()

tk.mainloop()
