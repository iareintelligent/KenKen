"""-----------------------------------------------------------------------------
# Topher_Sikorra_208_Project2_DRIVER.py
# Student Name: Topher Sikorra
# Assignment: Project #2
# Submission Date:
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Class notes, previous labs, www.kenken.com, lab notes
#-------------------------------------------------------------------------------
# Comments: Tried doing some binding from the GUI to make stuff happen when the
# KenKen tiles were clicked, but coudln't get it to work... added functionality
# to the "Check Answers" button instead.  Only could get KenKen tile binding
# within the KenKenTile Class.
#----------------------------------------------------------------------------"""
from Tkinter import *
from tkFont import *
from Topher_Sikorra_208_Project2_CLASS import *
import os
#I used winsound in lab10 (though not in the submited version).  Clearly, it
#only works for Windows based machines.  Research indicates that I would have
#to use PyGame to get a more robust solution for multi-platform sound
from winsound import PlaySound, SND_ASYNC, SND_LOOP, SND_FILENAME


class KenKen_GUI(Frame):
    """A GUI KenKen_GUI for KenKen"""
    def __init__(self, master):
        #Create the main frame
        Frame.__init__(self, master)
        self.grid()

        if os.name == "nt":
            self.file = "kefka.wav"
            PlaySound(self.file, SND_ASYNC|SND_FILENAME|SND_LOOP)

        #text variables to modify the KenKen tiles as needed
        self.kktile = {} #a cubbyhole for all my KenKen tiles

        self.xspacer = {}   #\Easy way to create spacers
        self.yspacer = {}    #\to grid stuff out in Tkinter

        self.menu_widgets() #Menu that chooses board to play

    def menu_widgets(self):
        """Provides board choice, and a way to exit the program"""
        #Made the boards into big buttons with pics (nice on my touchscreen)
        board1 = PhotoImage(file="game1.gif")
        board2 = PhotoImage(file="game2.gif")
        board3 = PhotoImage(file="game3.gif")
        kenkengif = PhotoImage(file="toy_kenken.gif")

        #make 3 board buttons for user choice
        self.game1_btn = Button(self,
        image = board1)
        self.game2_btn = Button(self,
        image = board2)
        self.game3_btn = Button(self,
        image = board3)

        #Bind each button to its particular game
        self.game1_btn.bind("<Button-1>", self.game_1)
        self.game2_btn.bind("<Button-1>", self.game_2)
        self.game3_btn.bind("<Button-1>", self.game_3)

        #Instructions (abridged)
        self.instruct_text = Label(self,
        text = "Click any board to play!")
        self.kenkentag = Label(self,
        image = kenkengif)

        #widget placement
        self.kenkentag.grid(column = 1, row = 0)
        self.instruct_text.grid(column = 1, row = 0, sticky = S)
        self.game1_btn.grid(column = 0, row = 0)
        self.game2_btn.grid(column = 0, row = 1)
        self.game3_btn.grid(column = 1, row = 1)

        #if I don't declare this, *sometimes* the pics don't load... no idea why
        self.game1_btn.image = board1
        self.game2_btn.image = board2
        self.game3_btn.image = board3
        self.kenkentag.image = kenkengif
        #Let the user quit the game from the main menu
        self.quit_btn = StringVar()
        self.quit_btn.set("     Quit     ")
        self.quit_button = Button(self,
        textvariable = self.quit_btn,
        background = "red",
        foreground = 'white',
        command = self.quit_game)
        #shares a grid square with the instructions, but mapped to the NE corner
        self.quit_button.grid(column = 1, row = 0, rowspan = 2, sticky = N+E)

    """Button choice from main menu calls one of three functions"""
    """-------------------"""
    def game_1(self, event):
        self.board_num = 1
        self.board_creation()
    def game_2(self, event):
        self.board_num = 2
        self.board_creation()
    def game_3(self, event):
        self.board_num = 3
        self.board_creation()
    """--------------------"""


    def board_creation(self):
        """Creates game board based on input from Main Menu"""
        #destroy the menu... I'm sure there's a way to destroy all in one step,
        #but I don't know what it is without going beyond resources allowed.
        self.quit_button.destroy()
        self.game1_btn.destroy()
        self.game2_btn.destroy()
        self.game3_btn.destroy()
        self.instruct_text.destroy()
        self.kenkentag.destroy()
        #Label Spacers to keep the board in order
        """X Axis Spacers"""
        self.rowspacer(0)
        self.rowspacer(6)
        self.rowspacer(8)

        """Y Axis Spacers"""
        self.columnspacer(0)
        #self.columnspacer(1)
        self.columnspacer(6)

        #create all of the KenKen tiles
        for tile in range(25):
            #KenKenTile receives individual tile info, and the board number
            #passed forward when the user clicked on a board in the main menu
            frame = KenKenTile(self, tile, self.board_num)
            frame.grid(row = (tile/5)+1, column = (tile%5)+1)
            self.kktile[tile] = frame


        #fonts
        chkbtn_font = Font(self, weight = 'bold', size = 14, family = "Courier")

        #Check Answers... if button pressed and all are correct, game is won
        self.chk_ansr_btn = StringVar()
        self.chk_ansr_btn.set("Check Answers")
        self.check_bttn = Button(self,
        textvariable = self.chk_ansr_btn,
        background = 'seagreen',
        font = chkbtn_font,
        foreground = 'white',
        command = self.check_it)
        self.check_bttn.grid(row = 7, column = 1, columnspan = 5, sticky = E+W)

        #Reset Button: resets if pressed twice
        self.reset_lbl = StringVar()
        self.reset_lbl.set("")
        self.reset_label = Label(self,
        textvariable = self.reset_lbl)
        erase_img = PhotoImage(file = 'icon_eraser.gif')
        self.reset_button = Button(self,
        image = erase_img,
        command = self.reset_board)
        self.reset_button.image = erase_img
        self.reset_label.grid(row = 0, column = 7)
        self.reset_button.grid(row = 1, column = 7)

        #Main Menu Button - (Quit game is nested in main menu)
        self.main_men_label = Label(self,
        text = "  Main Menu  ")
        self.main_men_label.grid(row = 2, column = 7, sticky = E+W+S)

        self.main_men_btn = StringVar()
        self.main_men_btn.set("               ")
        self.main_men_button = Button(self,
        textvariable = self.main_men_btn,
        background = 'white',
        foreground = 'white',
        command = self.main_men_chk)
        self.main_men_button.grid(row = 3, column = 7, sticky = N)

        #use to test diff options for win scenario
        self.win_test = Button(self,
        text = "Winner button\n(for losers)",
        command = self.game_winner)
        self.win_test.grid(row = 8, column =7,)

    """rowspacer/column spacer used to aid in widget placement"""
    """-------------------------------------------------------"""
    def rowspacer(self, xcoord):
        Label(self,
        text = ""
        ).grid(row = xcoord)

    def columnspacer(self, ycoord):
        Label(self,
        text = "          "
        ).grid(column = ycoord)
    """-------------------------------------------------------"""
    
    def check_it(self):
        """Check button operations: checks guesses, cancels operations if user
        changes their mind, and resets texts"""
        game_finished = 0 #25 correct tiles = win!
        #reset any texts that might have changed due to cancellation
        self.chk_ansr_btn.set("Check Answers")
        self.check_bttn.config(bg = "seagreen", foreground = "white")
        self.main_men_btn.set("               ")
        self.main_men_button.config(bg = "white")
        self.reset_lbl.set("")
        
        for i in range(25): #count the number of 'True' tiles
            check_bool = self.kktile[i].tile_check()
            if check_bool == True:
                game_finished +=1
        if game_finished == 25:
            self.game_winner()

    
    def reset_board(self):
        """Resets the game board"""
        if self.reset_lbl.get() == (""):
            self.chk_ansr_btn.set("Cancel")
            self.check_bttn.config(bg = "lawngreen", foreground = "dodgerblue")
            self.reset_lbl.set("Are you Sure?")
#            self.cancel_button = Button(self,
#            )
        else:
            self.reset_lbl.set("")
            self.chk_ansr_btn.set("Check Answers")
            self.check_bttn.config(bg = "seagreen", foreground = "white")
            for i in range(25):
                self.kktile[i].reset_tile()

    def main_men_chk(self):
        """Sends user to the main menu"""
        if self.main_men_btn.get() == ("               "):
                self.main_men_button.config(background = "coral")
                self.main_men_btn.set("Progress will\nbe lost!")
                self.chk_ansr_btn.set("Cancel")
                self.check_bttn.config(bg = "lawngreen", 
                foreground = "dodgerblue")
       
        #If user is sure, widgets are destroyed and main menu is called
        else:  
            for i in range(25):
                self.kktile[i].destroy()
            #self.check_val.destroy()
            self.check_bttn.destroy()
            self.reset_label.destroy()
            self.main_men_label.destroy()
            self.main_men_button.destroy()
            self.menu_widgets()

    def quit_game(self):
        """duh"""
        exit()

    def game_winner(self):
        """If all tiles are true, display a screen for the winner"""
        #Toplevel creates new window on top of current frame
        win_screen = Toplevel()
        #type of error is displayed as the title of the Toplevel frame
        win_screen.title("Congrats KenKen Genius Extrordinaire!")

        winner_gif = PhotoImage(file="you_win.gif")
        #makes a huge button
        button = Button(win_screen, image = winner_gif,
        command=win_screen.destroy)
        button.image = winner_gif
        button.pack()

    


