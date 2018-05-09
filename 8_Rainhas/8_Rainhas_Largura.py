import numpy as np
import random 
import os
import time


class Game:
    def __init__(self):
        self.board = np.zeros((8,8))            
        self.queens = 0
    def get_board(self):
        return self.board
    def get_queens(self):
        return self.queens
    def set_queen(self,pos):
        self.board[pos[0],pos[1]] = 1.0
        self.queens +=1
    
    def validation(self):
        Rx,Ry = np.where(self.board ==1)
        flag  = "VALID"
        for i in range(Rx.shape[0]):
            x,y = Rx[i], Ry[i]
            diagonal =  np.sum(np.diag(self.board,y-x))
            antidiagonal = np.sum(np.diag(self.board[:, ::-1],8 - y -1 -x)    )
            line = np.sum(self.board,axis=0)[y]
            column = np.sum(self.board,axis =1)[x]
            s = diagonal + antidiagonal + line + column
            if s != 4.0:
                flag = "INVALID"
                break
        return flag

class IA:
    def __init__(self):
        # Principal e o jogo pra uma rainha inserida aleatoria
        self.principal = Game()
        x,y = random.randint(0,7),random.randint(0,7)
        self.principal.set_queen((x,y))    
        
    def get_principal(self):
        return self.principal.get_board()
    def set_queen_principal(self,x,y):
        self.principal.set_queen((x,y))
    def generate_child(self,board):
        children= []
        for a in range(len(board)):
            for b in range(len(board)):
                if board[a][b] != 1.0:
                    child =  Game()
                    Rx,Ry = np.where(board == 1)
                    for i in range(Rx.shape[0]):
                        x,y= Rx[i],Ry[i]
                        child.set_queen((x,y))
                    child.set_queen((a,b))
                    if child.validation() == "VALID":
                        children.append(child)
        return children
if __name__ =="__main__":
    start_time = time.time()
    ia = IA()
    os.system("clear")
    print '\t8 Queens'
    print '\n Busca em Largura'
    print '\n\tFirst Board \n',ia.get_principal()
    end = "Unsolved" 
    while end != "Solved":
        
        Tree = ia.generate_child(ia.get_principal()) 
        for node in Tree:
            a = node.get_queens()
            if a == 8:
                end = "Solved"
                Solution = node.get_board()
                break
            else:
                new_node = ia.generate_child(node.get_board())
                for a in new_node:
                    Tree.append(a)
    
            Tree.remove(node) 


    if end == "Solved":
        print "\tSOLVED"
        print Solution
    else:
        print "\tUNSOLVED"
    print "\n\tTime taken: \n"
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s minutes ---" % ((time.time() - start_time)/60.0))
