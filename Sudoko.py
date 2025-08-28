import numpy as np
import time
import random
def check_row(board,row,num):
    if num in board[row]:
        return False
    return True
def check_column(board,col,num):
    for i in range(9):
        if num == board[i][col]:
            return False
    return True

def check_box(board,row,col,num):
    beg_row=(row//3)*3
    beg_col=(col//3)*3
    for i in range(beg_row,beg_row+3):
        for j in range(beg_col,beg_col+3):
            if board[i][j]==num:
                return False
    return True

def check_all(board,row,col,num):
    if check_row(board,row,num) and check_column(board,col,num) and check_box(board,row,col,num):
        return True
    return False
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)
    return None

def solve(board):
    not_fill=find_empty(board)
    if not not_fill:
        return True
    row,col=not_fill
    nums=list(range(1,10))
    random.shuffle(nums)
    for num in nums:
        if check_all(board,row,col,num):
            board[row][col]=num
            if solve(board):
                return True
            board[row][col]=0
    return False
def remove(board,n):
    while n>0:
        row=random.randint(0,8)
        col=random.randint(0,8)
        if board[row][col]!=0:
            board[row][col]=0
            n-=1
def play_game():

    board=np.zeros((9,9),dtype=int)
    solve(board)
    sol=board.copy()
    level=input(("Enter the Level(Easy,Medium,Hard):")).strip().lower()

    if level=='easy':
        r=random.randint(35,45)
    elif level=='medium':
        r=random.randint(45,50)
    elif level=='hard':
        r=random.randint(50,55)
    else:
        print("Invalid level!!!\nExit.")
        exit(0)

    remove(board,r)
    print("The Sudoku puzzle to be solved is:")
    print(board)

    start=time.time()
    while True:
        choice=input("Enter your choice(S for solution,M for move,E to Exit):")
        choice=choice.strip().lower()
        if choice=="s":
            print("The solution is:\n",sol)
        elif choice=='e':
            print("Exit!Thanks for playing...")
            exit(0)
        elif choice=='m':
            print(board)
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter col (0-8): "))
            num = int(input("Enter number (1-9, or 0 to erase): "))

            if check_all(board, row, col, num) or num == 0:
                board[row][col] = num
            else:
                print("Invalid move!")

            if find_empty(board) is None:
                print("Congratulations!You solved it!")
                end=time.time()
                time_taken=end-start
                print("Time taken to solve puzzle is:",time_taken)
                print("The Sudoku puzzle after solved:")
                print(board)
                return
        else:
            print("Invalid choice!!!choose the correct one...")

play_game()