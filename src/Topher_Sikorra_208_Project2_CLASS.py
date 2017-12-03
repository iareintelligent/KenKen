"""-----------------------------------------------------------------------------
# Topher_Sikorra_208_Project2_CLASS.py
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
# Comments: Originally used Labels instead of Buttons for the tiles.  While it
# looked better aesthetically, it wasn't as intuitive for a user to click on a
# label as it was for a button.
#----------------------------------------------------------------------------"""
from Tkinter import *
from tkFont import *
from KenKen_board_data import *


class KenKenTile(Frame):
    """Create KenKen tile frame objects"""
    def __init__(self, master, tile_number, board_num):
        Frame.__init__(self, master)

        #initiate Class attributes - self documenting, and explained more fully
        #as they're used.
        self.board_num = board_num
        self.tile_number = tile_number
        self.right_answer = False
        self.curr_time = 0
        self.tile_val = StringVar(self)
        self.bg_variable = distinct_group(tile_number,board_num)
        self.config(bd = 2, bg = distinct_group(tile_number, board_num),
        relief = RAISED)
        self.click = 0
        self.tile_ident = ["    ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 "]
#        print self.tile_ident
#        print self.click
#        print self.tile_ident[self.click]
        

        #create Fonts for the kenken tiles
        self.tile_font = Font(self,
        family = "arialblack",
        weight = "bold",
        size = 25)

        self.function_font = Font(self,
        family = "Arial",
        weight = "bold",
        size = 12)

        #frame headers to identify operations, values, etc
        self.frame_label = Label(self,
            text = str(grp_value(tile_number, board_num))
            + str(grp_funct(tile_number,board_num)),
            font = self.function_font,
            foreground = "black",
            anchor = W,
            bg = self.cget('bg'))
        self.frame_label.grid(row = 0, columnspan = 3, sticky = W+E)

        #When user clicks, this value changes from "  " to "5"
        self.tile_guess = StringVar()
        self.tile_guess.set(self.tile_ident[self.click])
        self.val_button = Button(self,
        textvariable = self.tile_guess,
        font = self.tile_font,
        relief = FLAT,
        anchor = N,
        width = 4,
        bg = self.cget('bg'))
        self.val_button.grid(row = 1, columnspan = 3, sticky = E+W)

        #stuff happens when mouse enters/leaves/clicks on each tile
        self.val_button.bind("<Enter>", self.m_enter)
        self.val_button.bind("<Leave>", self.m_leave)
        self.val_button.bind("<Button-1>", self.tile_select)

    def m_enter(self, event):
        """graphic stuff to let user know which tile could be changed"""
        check_bg = self.val_button.cget("bg")
        if check_bg != "coral":
            self.frame_label.config(bg = "PeachPuff")
            self.val_button.config(bg = "PeachPuff")

    def m_leave(self, event):
        """user is no longer highlighting block"""
        check_bg = self.val_button.cget("bg")
        if check_bg != "coral":
            self.frame_label.config(bg = self.cget('bg'))
            self.val_button.config(bg = self.cget('bg'))

    def tile_select(self, event):
        """Iterates through guesses until user's choice is selected"""
        self.click +=1
        if self.click > 5:
            self.click = 0
        #boolean value of true/false compared to KenKen_board_data file
        self.tile_guess.set(self.tile_ident[self.click])
        try:
            #exception handling to take care of "  "  value comparison
            user_guess = eval(self.tile_guess.get())
            tile_val = tile_value(self.tile_number, self.board_num)
        except:
            user_guess = (self.tile_guess.get())
            tile_val = tile_value(self.tile_number, self.board_num)
        if user_guess == tile_val: #self documenting...
            self.right_answer = True
        else:
            self.right_answer = False
#        print user_guess," = ",tile_val,": ",self.right_answer

    def start_time(self, event):
        #used for the timer.. just copied the lab notes...
        self.curr_time = 10
        self.tile_check()

    def tile_check(self):
        if self.right_answer == True:
            #temp green highlight if answer is true for 1/2 second
            self.frame_label.config(bg = 'green')
            self.val_button.config(bg = 'green')
            if self.curr_time == 0:
                self.curr_time -= 1;
                self.val_button.after(500, self.tile_check)
            else:
                self.frame_label.config(bg = self.cget('bg'))
                self.val_button.config(bg = self.cget('bg'))
                self.curr_time = 0
        else:
            #temp red highlight if answer is false for 1/2 second
            if self.tile_guess.get() != ("    "):
                self.frame_label.config(bg = 'coral', fg = 'white')
                self.val_button.config(bg = 'coral', fg = 'white')
                if self.curr_time == 0:
                    self.curr_time -= 1;
                    self.val_button.after(500, self.tile_check)
                else:
                    self.val_button.config(bg = self.cget('bg'), fg = 'black')
                    self.frame_label.config(bg = self.cget('bg'), fg = 'black')
                    self.curr_time = 0
        #when GUI calls function, return value of True/False for game_win status
        return self.right_answer

    def reset_tile(self):
        #when GUI calls function, reset the values of all tiles to " "
        self.click = 0
        self.tile_guess.set(self.tile_ident[self.click])
        #make sure now-empty tiles aren't getting a value of true from before
        self.right_answer = False   

