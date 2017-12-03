#-*- coding: utf-8 -*- #used in lab 2 to let python utilize non-ASCII symbol '�'
"""-----------------------------------------------------------------------------
# KenKen_board_data.py
# Student Name: Topher Sikorra
# Assignment: Project #2
#-------------------------------------------------------------------------------
# Comments: This file contains all of the data required for the KenKen board
# to populate itself, including board numbers, tile values, group functions, and
# group values.
#----------------------------------------------------------------------------"""

def grp_funct(tile_number, board_num):
    # """Assigns mathematical function symbol to indicated tiles"""
#    print board_num
    #board_num is passed all the way from the main menu
    if board_num == 1:
        if tile_number == 0 or tile_number == 18 or tile_number == 20:
            return 'x'
        elif tile_number == 7:
            return '�'
        elif tile_number == 1 or tile_number == 3 or tile_number == 11 \
        or tile_number == 13:
            return '+'
        elif tile_number == 4:
            return '-'
        else:
            return " "
    if board_num == 2:
        if tile_number == 0 or tile_number == 3 or tile_number == 15:
            return 'x'
        elif tile_number == 4 or tile_number == 5 or tile_number == 7:
            return '+'
        elif tile_number == 17 or tile_number == 19:
            return '-'
        else:
            return " "
    if board_num == 3:
        if tile_number == 4 or tile_number == 7:
            return 'x'
        elif tile_number == 19:
            return '�'
        elif tile_number == 1 or tile_number == 15 or tile_number == 18:
            return '+'
        elif tile_number == 0:
            return "-"
        else:
            return " "

def grp_value(tile_number, board_num):
    """Assigns group value symbol to indicated tiles"""
    tile_vals = {} #values are loaded per the individual boards
    if board_num == 1:
        try:
            tile_vals= {0:15,1:7,3:7,4:1,6:2,7:5,11:13,
            13:8,18:10,20:12}
            return tile_vals[tile_number]
        except:
            return ""
    if board_num == 2:
        try:
            tile_vals = {0:40,3:6,4:10,5:5,7:18,15:9,
            17:0,19:1}
            return tile_vals[tile_number]
        except:
            return ""

    if board_num == 3:
        try:
            tile_vals = {0:0,1:14,4:60,7:200,8:1,15:14,
            18:8,19:2}
            return tile_vals[tile_number]
        except:
            return ""

def tile_value(tile_number, board_num):
    """Return the --value-- of each tile to be compared to the user guess"""
    if board_num == 1:
        tile_val = {0:1, 1:5, 2:2, 3:3, 4:4,
                5:5, 6:2, 7:1, 8:4, 9:3,
                10:3, 11:4, 12:5, 13:2, 14:1,
                15:2, 16:3, 17:4, 18:1, 19:5,
                20:4, 21:1, 22:3, 23:5, 24:2}

    if board_num == 2:
        tile_val = {0:1, 1:2, 2:4, 3:3, 4:5,
                5:3, 6:5, 7:1, 8:2, 9:4,
                10:2, 11:3, 12:5, 13:4, 14:1,
                15:5, 16:4, 17:2, 18:1, 19:3,
                20:4, 21:1, 22:3, 23:5, 24:2}

    if board_num == 3:
        tile_val = {0:1, 1:5, 2:2, 3:4, 4:3,
                5:2, 6:3, 7:4, 8:1, 9:5,
                10:3, 11:2, 12:1, 13:5, 14:4,
                15:4, 16:1, 17:5, 18:3, 19:2,
                20:5, 21:4, 22:3, 23:2, 24:1}
    return tile_val[tile_number]

def distinct_group(tile_number, board_num):
    """Adds color to each group so borders between groups are distinct"""
    if board_num == 1:
        group1 = [0,5,10,13,14,19]
        group3 = [1,2,4,9,11,15,16,17]
        group2 = [7,12,18,23,24]
        group4 = [3, 6, 8,20,21,22]

    if board_num == 2:
        group1 = [0,1,2,6,17,22,23]
        group3 = [3,5,10,8,9,19,24]
        group2 = [4,9,14,15,20,21]
        group4 = [7,11, 12,13,16,18]

    if board_num == 3:
        group1 = [0,5,10,8,18,22,23]
        group3 = [1,2,3,6,19,24]
        group2 = [4,9,14,15,16,20,21]
        group4 = [7, 11, 12,13,17]

    if tile_number in group1:
        return "gray69"
    if tile_number in group2:
        return "turquoise"
    if tile_number in group3:
        return "orange"
    if tile_number in group4:
        return "dodgerblue"
