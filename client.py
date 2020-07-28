from os import system
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname() , 1234))

while True :
    msg = s.recv(1024).decode("utf-8")
    if len(msg) > 0:
        if msg.startswith("BOARD"):
            system('cls')
            print("\t\t" + player + "\n\n")
            board = msg.split(":")[1].split(",")
        
           
            print("\t\t " + board[0] + " | " + board[1] + " | " + board[2])
            print("\t\t" + "-----------")
            print("\t\t " + board[3] + " | " + board[4] + " | " + board[5])
            print("\t\t" + "-----------")
            print("\t\t " + board[6] + " | " + board[7] + " | " + board[8])
        elif msg.startswith("ENTER"):
            print("\n\n"+msg.split(":")[1])
            x = bytes(input(),"utf-8")
            s.send(x)
        elif msg.startswith("RESULT") : 
            print("\n\n\t\t"+msg.split(":")[1])
            break
        elif msg.startswith("PLAYER") : 
            player = msg.split(":")[1]