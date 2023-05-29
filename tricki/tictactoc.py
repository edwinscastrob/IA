from tkinter import *
from tkinter import messagebox

main = Tk()
main.title('Triki')
main.iconbitmap('C:/Users/poloa/OneDrive/Documentos/IA/IA/tricki/tic-tac-toe.ico')
main.resizable(False, False)
buttons = []
winner = False
count = 0
clicked = True


def checkIfWon():
    global winner
    lines_to_check = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]  # Diagonales
    ]

    for line in lines_to_check:
        b1, b2, b3 = buttons[line[0]], buttons[line[1]], buttons[line[2]]
        if b1["text"] == b2["text"] == b3["text"] != " ":
            b1.config(bg="green")
            b2.config(bg="green")
            b3.config(bg="green")
            winner = True
            messagebox.showinfo("Tic Tac Toe", f"¡¡¡ {b1['text']} Wins !!!")
            disable_all_buttons()
            return

    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a tie \nNo One Wins")
        disable_all_buttons()


def b_click(b):
    global count, clicked
    if b["text"] == " " and clicked:
        b["text"] = "X"
        clicked = False
        count += 1
        b.config(state=DISABLED)
        checkIfWon()
    elif b["text"] == " " and not clicked:
        b["text"] = "O"
        clicked = True
        count += 1
        b.config(state=DISABLED)
        checkIfWon()

def disable_all_buttons():
    for button in buttons:
        button.config(state=DISABLED)


def reset():
    global buttons, count, clicked, winner
    count = 0
    clicked = True
    winner = False

    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace", state=NORMAL)


def create_buttons():
    for i in range(3):
        for j in range(3):
            button = Button(main, text=" ", font=('Helvetica', 25, 'bold'), height=3,
                            width=6, bg="SystemButtonFace", command=lambda x=i, y=j: b_click(buttons[3 * x + y]))
            button.grid(row=i, column=j)
            buttons.append(button)


my_menu = Menu(main)
main.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

create_buttons()

main.mainloop()
