import pygame

from PIL import Image

import csv

import time

boardFile = "./board.csv"

# Image

imageFile = "./tabla.jpg"

image = Image.open(imageFile)

width, height = image.size

width1, height1 = width, height

# Board

def board_function(boardFile):

        global board

        board = []

        with open(boardFile, 'r') as pfile:

            p_reader = csv.reader(pfile)

            for p_row in p_reader:

                board.append(p_row)
            
        for i in range(0, len(board)):

            board[i] = [int(j) for j in board[i]]

# Functions

def coordinates(width, height):

    global box_height
    
    global box_width

    box_height = height / 9

    box_width = width / 9

def print_var(row, col, i):

    global font, screen
 
    text = font.render(str(i), True, (0, 0, 0), (255,255,255))
    
    textRect = text.get_rect()

    X = box_width*(col + 1) - box_width/2

    Y = box_height*(row + 1) - box_height/2
    
    textRect.center = (X, Y)

    screen.blit(text, textRect)

    pygame.display.update()

# Sudoku solver code

def solve(bo):

    find = find_empty(bo)

    if not find:

        return True

    else:

        row, col = find

    for i in range(1,10):

        if valid(bo, i, (row, col)):

            bo[row][col] = i

            print_var(row, col, i)

            if solve(bo):

                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):

    # Check row

    for i in range(len(bo[0])):

        if bo[pos[0]][i] == num and pos[1] != i:

            return False

    # Check column

    for i in range(len(bo)):

        if bo[i][pos[1]] == num and pos[0] != i:

            return False

    # Check box

    box_x = pos[1] // 3

    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):

        for j in range(box_x * 3, box_x*3 + 3):

            if bo[i][j] == num and (i,j) != pos:

                return False

    return True

def find_empty(bo):

    for i in range(len(bo)):

        for j in range(len(bo[0])):

            if bo[i][j] == 0:

                return (i, j)  # row, col

    return None

def find_NonEmpty(bo):

    for i in range(len(bo)):

        for j in range(len(bo[0])):

            if bo[i][j] != 0:

                print_var(i, j, bo[i][j])

coordinates(width, height)

board_function(boardFile)

pygame.init()

pygame.display.set_caption('Sudoku')

clock = pygame.time.Clock()

screen = pygame.display.set_mode([width, height])

done = False

background = pygame.image.load(imageFile).convert()

font = pygame.font.Font(None, 32)

z = 1

while not done:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

    if z != 0:

        screen.blit(background, [0, 0])

        find_NonEmpty(board)

        solve(board)

        clock.tick(30)

        pygame.display.flip()

        z = 0

    
pygame.quit()