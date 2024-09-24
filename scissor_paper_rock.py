from tkinter import *
import pygame
from PIL import Image, ImageTk
import tkinter.messagebox
from random import randint

pygame.mixer.init()

def win_sound():
    global s1
    s1 = pygame.mixer.Sound("success.mp3")
    s1.play()

def lose_sound():
    global s2
    s2 = pygame.mixer.Sound("slider.mp3")
    s2.play()

def switch_to_second_window(event):
    gui.withdraw()  # Hide the first window
    root.deiconify()  # Show the second window
def quit(evnt):
   ans = tkinter.messagebox.askquestion("Confirm","Are you sure you want to exit?")
   if ans=="yes":
      exit()
   else :
      pass

gui = Tk()
gui.title("Full Screen Image")

# Get the screen width and height
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
gui.attributes("-fullscreen", True)

# Load and resize the image
image2 = Image.open("rps.png")  # Replace with the path to your image
image2 = image2.resize((screen_width, screen_height))
photo2 = ImageTk.PhotoImage(image2)

# Create a full-screen canvas
canvas = Canvas(gui, width=screen_width, height=screen_height)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=NW, image = photo2)

# Function to handle window resizing
def on_resize(event):
    # Update the canvas size to match the window size
    canvas.config(width=gui.winfo_width(), height=gui.winfo_height())

# Bind the resize function to window resizing
gui.bind("<Configure>", on_resize)
play_imag = ImageTk.PhotoImage(Image.open("rps_play.png"))

button1 = canvas.create_image(767,410,image = play_imag)

canvas.tag_bind(button1,'<Button-1>',switch_to_second_window)
exit_imag = ImageTk.PhotoImage(Image.open("rps_exit.png"))
button3 = canvas.create_image(780,580,image = exit_imag)
canvas.tag_bind(button3,'<Button-1>',quit)




# main window
root = Toplevel(gui)
root.withdraw()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


# scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# update message


def updateMessage(x):
    msg['text'] = x

# update user score


def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score


def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner


def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            lose_sound()

            updateMessage("You loose")
            updateCompScore()
        else:
            win_sound()
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            lose_sound()
            updateMessage("You loose")
            updateCompScore()
        else:
            win_sound()
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            lose_sound()
            updateMessage("You loose")
            updateCompScore()
        else:
            win_sound()
            updateMessage("You Win")
            updateUserScore()

    else:
        pass


# update choices

choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


# buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)




gui.mainloop()
root.mainloop()
