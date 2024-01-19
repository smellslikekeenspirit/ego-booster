# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import random

def my_tkinter_view(request):
    root = tk.Tk()
    root.title("Egobooster")

    label = tk.Label(root, text="", font=("Helvetica", 14))
    label.pack(pady=20)

    entry = tk.Entry(root, font=("Helvetica", 12))
    entry.pack(pady=10)

    submit_button = tk.Button(root, text="Submit", command=lambda: submit(entry, label))
    submit_button.pack(pady=20)

    set_random_question(label)

    root.mainloop()

    return HttpResponse("Tkinter view executed successfully.")


questions = [
    "What is your name?",
    "What is your mom's name?",
    "What is your dad's name?"
]


def submit(entry, label):
    user_answer = entry.get()
    question = label.cget("text")

    if question == "What is your name?":
        message = f"As someone named {user_answer}, \n" \
                  f"you've literally unlocked intelligence lol."
    elif question == "What is your mom's name?":
        message = f"What the actual fuck. " \
                  f"You're {user_answer}'s genius offspring.\n" \
                  f"Your IQ is beyond 180. What the fuck.\n"
    elif question == "What is your dad's name?":
        message = f"Hi, {user_answer}'s child! " \
                  f"Your IQ is soaring beyond 180.\n" \
                  f"Did you know that everyday you produce surplus IQ\n" \
                  f"which comes out of your dick when you cum?\n" \
                  f"Your body has to excrete it everyday so your brain doesn't explode.\n" \
                  f"Congratulations!\n"

    show_dancing_bee_in_message_box(message)


def set_random_question(label):
    question = random.choice(questions)
    label.config(text=question)


def show_dancing_bee_in_message_box(message):
    bee_window = tk.Toplevel()
    bee_window.title("Congratulations OMG")

    bee_gif = Image.open("egobooster/dancing_bee.gif")
    bee_gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(bee_gif)]

    label = tk.Label(bee_window, text=message, font=("Helvetica", 12))
    label.pack()

    image_label = tk.Label(bee_window)
    image_label.pack()

    def update_frame(index):
        frame = bee_gif_frames[index]
        image_label.configure(image=frame)
        image_label.image = frame
        bee_window.after(100, update_frame, (index + 1) % len(bee_gif_frames))

    update_frame(0)
