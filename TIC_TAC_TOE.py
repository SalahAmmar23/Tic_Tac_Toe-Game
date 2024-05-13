from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Almdrasa.com Project")
root.iconbitmap("")

# x starts so true
count = 0
player_score = 0
computer_score = 0

score_label = Label(root, text=f"Player: {player_score}  Computer: {computer_score}")
score_label.grid(row=3, column=0, columnspan=3)

# Disable all buttons
def disable_all_buttons():
    for b in buttons:
        b.config(state=DISABLED)

# Check to see if someone won
def check_if_won(symbol):
    winning_combinations = [
        [b1, b2, b3], [b4, b5, b6], [b7, b8, b9],  # rows
        [b1, b4, b7], [b2, b5, b8], [b3, b6, b9],  # columns
        [b1, b5, b9], [b3, b5, b7]  # diagonals
    ]
    for combination in winning_combinations:
        if all(b["text"] == symbol for b in combination):
            for b in combination:
                b.config(bg="light blue" if symbol == "X" else "red")
            if symbol == "X":
                messagebox.showinfo("Tic Tac Toe", "Congratulation! You wins")
            else:
                messagebox.showinfo("Tic Tac Toe", "Congratulation! Computer wins")
            disable_all_buttons()
            return True
    return False

# Button Clicked function
def b_click(b):
    global count, player_score, computer_score
    if b["text"] == " ":
        b["text"] = "X"
        count += 1
        if check_if_won("X"):
            player_score += 1
            score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")
            return
        if count == 9:
            messagebox.showinfo("Tic Tac Toe", "It's A Tie!\nNo one Wins")
            for button in buttons:
                button.config(bg="red")
            disable_all_buttons()
            return
        computer_move()

# Computer makes a move
def computer_move():
    global count, player_score, computer_score
    empty_buttons = [b for b in buttons if b["text"] == " "]
    if empty_buttons:
        chosen_button = random.choice(empty_buttons)
        chosen_button["text"] = "O"
        count += 1
        if check_if_won("O"):
            computer_score += 1
            score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")
            return
    else:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\nNo one Wins")
        for button in buttons:
            button.config(bg="red")
        disable_all_buttons()

# Start the game over!
def reset():
    global buttons, b1, b2, b3, b4, b5, b6, b7, b8, b9
    global count
    count = 0
    # Start Building our buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()
