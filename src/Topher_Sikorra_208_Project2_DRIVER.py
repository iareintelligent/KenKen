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
# References: Previous labs
#-------------------------------------------------------------------------------
# Comments:
#----------------------------------------------------------------------------"""
#standard GUI initiation file
from Tkinter import Tk
from Topher_Sikorra_208_Project2_GUI import KenKen_GUI

root = Tk()
root.title("KenKen, a game of mathematics, frustration, and awesomeness")
root.geometry("600x560")

app = KenKen_GUI(root)

root.mainloop()

