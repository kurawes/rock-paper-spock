from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title("   Rock - Paper - Scissors - Lizard - Spock")
root.iconbitmap("images/Rivee.ico")
root.geometry("500x600")

# Setting background to white instead of regular gray
root.config(bg="white")

# Defined images for every variable
rock = PhotoImage(file="images/Rock.png")
paper = PhotoImage(file="images/Paper.png")
scissors = PhotoImage(file="images/Scissors.png")
lizard = PhotoImage(file="images/Lizard.png")
spock = PhotoImage(file="images/Spock.png")
starter_image = PhotoImage(file="images/RPSLS.png")

# Adding images to a list
image_list = [rock, paper, scissors, lizard, spock]

# Pick a random number between 0 and 4
picked_number = randint(0, 4)

# Throws up an image when the program starts
image_label = Label(root, image=starter_image, bd=0, bg="white")
image_label.pack(pady=10)


# Spin function for computers selection
def spinning():
    # Picks a random nr and show the corresponding image
    pick_rand_nr = randint(0, 4)
    image_label.config(image=image_list[pick_rand_nr])

    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors
    # 3 = Lizard
    # 4 = Spock

    # Converting dropdown menu choice to a number
    if user_selection.get() == "Rock":
        user_number = 0
    elif user_selection.get() == "Paper":
        user_number = 1
    elif user_selection.get() == "Scissors":
        user_number = 2
    elif user_selection.get() == "Lizard":
        user_number = 3
    elif user_selection.get() == "Spock":
        user_number = 4

    # Determines who won - compares user_number with pick_rand_nr
    if user_number == 0:  # user chose - Rock
        if pick_rand_nr == 0:  # computer chose - Rock
            result_label.config(text="It's a draw! Spin again ...", bg="yellow")
        elif pick_rand_nr == 1:  # computer chose - Paper
            result_label.config(text="Paper covers Rock! You loose ...", bg="red")
        elif pick_rand_nr == 2:  # computer chose - Scissors
            result_label.config(text="You win!!! Rock crushes Scissors!", bg="lime green")
        elif pick_rand_nr == 3:  # computer chose - Lizard
            result_label.config(text="You win!!! Rock crushes Lizard!", bg="lime green")
        elif pick_rand_nr == 4:  # computer chose - Spock
            result_label.config(text="Spock vaporizes Rock! You loose ...", bg="red")

    elif user_number == 1:  # user chose - Paper
        if pick_rand_nr == 0:  # computer chose - Rock
            result_label.config(text="You win!!! Paper covers Rock!", bg="lime green")
        elif pick_rand_nr == 1:  # computer chose - Paper
            result_label.config(text="It's a draw! Spin again ...", bg="yellow")
        elif pick_rand_nr == 2:  # computer chose - Scissors
            result_label.config(text="Scissors cuts Paper! You loose ...", bg="red")
        elif pick_rand_nr == 3:  # computer chose - Lizard
            result_label.config(text="Lizard eats Paper! You loose ...", bg="red")
        elif pick_rand_nr == 4:  # computer chose - Spock
            result_label.config(text="You win!!! Paper disproves Spock!", bg="lime green")

    elif user_number == 2:  # user chose - Scissors
        if pick_rand_nr == 0:  # computer chose - Rock
            result_label.config(text="Rock crushes Scissors! You loose ...", bg="red")
        elif pick_rand_nr == 1:  # computer chose - Paper
            result_label.config(text="You win!!! Scissors cuts Paper!", bg="lime green")
        elif pick_rand_nr == 2:  # computer chose - Scissors
            result_label.config(text="It's a draw! Spin again ...", bg="yellow")
        elif pick_rand_nr == 3:  # computer chose - Lizard
            result_label.config(text="You win!!! Scissors decapitates Lizard", bg="lime green")
        elif pick_rand_nr == 4:  # computer chose - Spock
            result_label.config(text="Spock smashes Scissors! You loose ...", bg="red")

    elif user_number == 3:  # user chose - Lizard
        if pick_rand_nr == 0:  # computer chose - Rock
            result_label.config(text="Rock crushes Lizard! You loose ...", bg="red")
        elif pick_rand_nr == 1:  # computer chose - Paper
            result_label.config(text="You win!!! Lizard eats Paper!", bg="lime green")
        elif pick_rand_nr == 2:  # computer chose - Scissors
            result_label.config(text="Scissors decapitates Lizard! You loose ...", bg="red")
        elif pick_rand_nr == 3:  # computer chose - Lizard
            result_label.config(text="It's a draw! Spin again ...", bg="yellow")
        elif pick_rand_nr == 4:  # computer chose - Spock
            result_label.config(text="You win!!! Lizard poisons Spock!", bg="lime green")

    elif user_number == 4:  # user chose - Spock
        if pick_rand_nr == 0:  # computer chose - Rock
            result_label.config(text="You win!!! Spock vaporizes Rock!", bg="lime green")
        elif pick_rand_nr == 1:  # computer chose - Paper
            result_label.config(text="Paper disproves Spock! You loose ...", bg="red")
        elif pick_rand_nr == 2:  # computer chose - Scissors
            result_label.config(text="You win!!! Spock smashes Scissors!", bg="lime green")
        elif pick_rand_nr == 3:  # computer chose - Lizard
            result_label.config(text="Lizard poisons Spock! You loose ...", bg="red")
        elif pick_rand_nr == 4:  # computer chose - Spock
            result_label.config(text="It's a draw! Spin again ...", bg="yellow")


# User choice dropdown menu
user_selection = ttk.Combobox(root, value=("Rock", "Paper", "Scissors", "Lizard", "Spock"))
user_selection.current(0)
user_selection.pack(pady=30)

# Spin button to play the next round
spin_button = Button(root, text="Spin!", command=spinning)
spin_button.pack(pady=20)

# Label for showing the result
result_label = Label(root, text="", font=("Helvetica", 18), bg="white")
result_label.pack(pady=40)

# Runs the program
root.mainloop()
