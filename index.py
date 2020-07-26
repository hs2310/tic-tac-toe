board = [ [' ' , ' ' , ' '], [' ' , ' ' , ' '], [' ' , ' ' , ' ']]

current_player = "O" 

def printBoard():
    print("",end="\t\t")
    for i in range(3):
        for j in range(3):
            if j == 2 : print(board[i][j],end="\n\t\t")
            else : print(board[i][j],end= "|")
        if i != 2: print("-----", end="\n\t\t")

def checkGame():
    if board[0][0] == board[0][1] and board[0][2] == board[0][1] and board[0][0] != ' ': return True
    elif board[1][0] == board[1][1] and board[1][2] == board[1][1] and board[1][0] != ' ': return True
    elif board[2][0] == board[2][1] and board[2][2] == board[2][1] and board[2][0] != ' ': return True
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != ' ': return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != ' ': return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][1] and board[0][2] != ' ': return True
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ': return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ': return True
    return False

def isEmpty():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return True
    return False

while True:

    printBoard()

    x = int(input("\nEnter x coordinate ("+ current_player + ") : " ))
    y = int(input("Enter y coordinate ("+ current_player + ") : " ))
    
    if board[x][y] == ' ': 
        board[x][y] = current_player
    else :
        print("Invalid Move")
        continue
    if checkGame() == True:
        print( "Player (" + current_player + ") Won ")
        break
    elif not isEmpty() :
        print( "It's a Tie"  )
        break
    
    if current_player == 'O':
        current_player = 'X'
    else : current_player = 'O'