from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap("")

# Constants
PLAYER = "X"
COMPUTER = "O"
EMPTY = " "

# Initialize variables
board = [[EMPTY for _ in range(3)] for _ in range(3)]
player_score = 0
computer_score = 0

def highlight_losing_moves(symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            for j in range(3):
                buttons[i][j].config(bg="red")
            return

    for j in range(3):
        if all(board[i][j] == symbol for i in range(3)):
            for i in range(3):
                buttons[i][j].config(bg="red")
            return

    if all(board[i][i] == symbol for i in range(3)):
        for i in range(3):
            buttons[i][i].config(bg="red")
        return

    if all(board[i][2 - i] == symbol for i in range(3)):
        for i in range(3):
            buttons[i][2 - i].config(bg="red")
        return

# Function to reset the game
def reset_game():
    global board
    for i in range(3):
        for j in range(3):
            board[i][j] = EMPTY
            buttons[i][j]["text"] = EMPTY
            buttons[i][j].config(bg="SystemButtonFace", state=NORMAL)

# Function to check if someone has won
def check_win(symbol):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False

# Function to handle player's move
def player_move(row, col):
    global player_score
    if board[row][col] == EMPTY:
        board[row][col] = PLAYER
        buttons[row][col].config(text=PLAYER)
        buttons[row][col].config(state=DISABLED)  # Disable the button after it's filled
        if check_win(PLAYER):
            player_score += 1
            messagebox.showinfo("Tic Tac Toe", "Congratulations! You win!")
            score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")
            highlight_winner_moves(PLAYER)
            root.update()  # Update the GUI to show the highlighted moves
            disable_all_buttons()
            return
        if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
            messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
            highlight_tie_moves()
            root.update()  # Update the GUI to show the highlighted moves
            disable_all_buttons()
            return
        computer_move()
    else:
        highlight_losing_moves(PLAYER)
        messagebox.showinfo("Tic Tac Toe", "Computer wins!")
        score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")
        root.update()  # Update the GUI to show the highlighted moves
        disable_all_buttons()
        return

# Function to handle computer's move
def computer_move():
    global computer_score
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = COMPUTER
        buttons[row][col].config(text=COMPUTER)
        buttons[row][col].config(state=DISABLED)  # Disable the button after filling it
        if check_win(COMPUTER):
            computer_score += 1
            messagebox.showinfo("Tic Tac Toe", "Computer wins!")
            score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")
            highlight_losing_moves(COMPUTER)  # Highlighting the losing combination in red
            root.update()  # Update the GUI to show the highlighted moves
            disable_all_buttons()
            return
    else:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        highlight_tie_moves()
        root.update()  # Update the GUI to show the highlighted moves
        disable_all_buttons()


# Function to highlight winning moves
def highlight_winner_moves(symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            for j in range(3):
                buttons[i][j].config(bg="light blue")
            return

    for j in range(3):
        if all(board[i][j] == symbol for i in range(3)):
            for i in range(3):
                buttons[i][j].config(bg="light blue")
            return

    if all(board[i][i] == symbol for i in range(3)):
        for i in range(3):
            buttons[i][i].config(bg="light blue")
        return

    if all(board[i][2 - i] == symbol for i in range(3)):
        for i in range(3):
            buttons[i][2 - i].config(bg="light blue")
        return

# Function to highlight tie moves
def highlight_tie_moves():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(bg="red")

# Function to disable all buttons
def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=DISABLED)

# Create buttons
buttons = [[Button(root, text=EMPTY, font=("Helvetica", 20), height=3, width=6,
                   bg="SystemButtonFace", command=lambda row=i, col=j: player_move(row, col))
            for j in range(3)] for i in range(3)]

# Grid the buttons
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset_game)

# Create score label
score_label = Label(root, text=f"Player: {player_score}  Computer: {computer_score}")
score_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
