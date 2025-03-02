# Program to help children practice reading.
# Randomly generates a word from a CSV file.
import tkinter as tk
import random 
import csv

#GUI Setup
window = tk.Tk()
window.title("Kids Reading Program")
window.geometry('520x300')

with open("words.csv", newline="") as new_file:
    contents = csv.reader(new_file)
    rows = list(contents)

def on_button_click():
    rand_number = random.randint(0,len(rows) - 1)
    word = rows[rand_number][0]
    label.config(text = word)
    label.config(font=("Ariel", 70))
    print(word)
    
label = tk.Label(window, text="")
label.pack(pady = 20)

button = tk.Button(window, text = "Click for next word", command = on_button_click)
button.pack(pady = 20)

window.mainloop()



