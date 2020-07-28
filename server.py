import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))

s.listen(5)

board = [ [' ' , ' ' , ' '], [' ' , ' ' , ' '], [' ' , ' ' , ' ']]

current_player = "O" 

def printBoard():
    print("",end="")
    for i in range(3):
        for j in range(3):
            if j == 2 : print(board[i][j],end="\n")
            else : print(board[i][j],end= "|")
        if i != 2: print("-----", end="\n")

def checkGame():
    if board[0][0] == board[0][1] and board[0][2] == board[0][1] and board[0][0] != ' ': return True
    elif board[1][0] == board[1][1] and board[1][2] == board[1][1] and board[1][0] != ' ': return True
    elif board[2][0] == board[2][1] and board[2][2] == board[2][1] and board[2][0] != ' ': return True
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != ' ': return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != ' ': return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != ' ': return True
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ': return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ': return True
    return False

def isEmpty():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return True
    return False



players = dict()
i = 0
while True : 
    if i == 2 :
        break
    clientsocket,  address = s.accept() 
    print(f"Connection from {address} has been established!!")
    clientsocket.send(bytes("Welcome to the server!" , "utf-8"))
    if i == 0 :
        players["O"] = clientsocket
    if i == 1 : 
        players["X"] = clientsocket
    i+=1



players["O"].send(bytes("PLAYER :WELCOME YOU ARE PLAYER \"O\"" , "utf-8"))
players["X"].send(bytes("PLAYER :WELCOME YOU ARE PLAYER \"X\"" , "utf-8"))

while True:

    # printBoard()
    players['O'].send(bytes("BOARD :"+",".join(item for inner in board for item in inner) , "utf-8"))
    players['X'].send(bytes("BOARD :"+",".join(item for inner in board for item in inner) , "utf-8"))
    # print("\nEnter x coordinate ("+ current_player + ") : ")
    players[current_player].send(bytes("ENTER :Enter x coordinate  : " , "utf-8"))
    x = int(players[current_player].recv(1024).decode("utf-8"))
    
    # print("\nEnter y coordinate ("+ current_player + ") : ")
    players[current_player].send(bytes("ENTER :Enter y coordinate  : " , "utf-8"))
    y = int(players[current_player].recv(1024).decode("utf-8"))
    
    
    if board[x][y] == ' ': 
        board[x][y] = current_player
    else :
        print("Invalid Move")
        continue
    if checkGame() == True:
        print( "RESULT : Player (" + current_player + ") Won ")
        players['O'].send(bytes("RESULT :Player (" + current_player + ") Won " , "utf-8"))
        players['X'].send(bytes("RESULT :Player (" + current_player + ") Won " , "utf-8"))
        break
    elif not isEmpty() :
        print( "RESULT : It's a Tie" )
        players['O'].send(bytes("RESULT :It's a Tie" , "utf-8"))
        players['X'].send(bytes("RESULT :It's a Tie" , "utf-8"))
        break
    
    if current_player == 'O':
        current_player = 'X'
    else : current_player = 'O'
