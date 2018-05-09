import numpy as np
import random


class Node:
    def __init__(self,Current,Obj,G):
        self.Cord = Current 
        a = self.Cord[0] - Obj[0]
        b = self.Cord[1] - Obj[1]
        c = self.Cord[2] - Obj[2]
        self.G = G
        self.H = np.sqrt( np.square(a) + np.square(b) + np.square(c) )
        self.Cost = self.G+self.H
            

class Cube:
    def __init__(self,dimensions,obstacles):
        #gera um cubo NxNxN com custos aleatorios de 0-9
        self.cube = np.random.randint(9,size = (dimensions,dimensions,dimensions)) 
        self.number_of_blocks = 0
        for x in range(self.cube.shape[0]):
            for y in range(self.cube.shape[1]):
                for z in range(self.cube.shape[2]):
                    # Cria areas que nao pode passar a partir de uma probabilidade setada
                    if random.random() < obstacles:
                        self.cube[x][y][z] = '99'
                        print x,y,z,"--- Block"
    def get_cube(self):
        return self.cube
    def get_neighborhood(self,cord):
        neighbor = []
        for a in (-1,0,1):
            x = a + cord[0]
            for b in (-1,0,1):
                y = b + cord[1]
                for c in (-1,0,1):
                    z = c + cord[2]
                    print x,y,z 
                    if (x==y and y==x) :
                        pass
                    else:
                        if ( (x >= 0 and x < len(self.cube)) and
                           (y >= 0 and y < len(self.cube)) and
                           ((z >= 0) and z < len(self.cube))):
                            neighbor.append((x,y,z,self.cube[x][y][z]))
                        

        return neighbor
if  __name__ == "__main__":
    C = Cube(3,0.1)
    for c in C.get_cube():
        print len(c)
        print c
    print len(C.get_neighborhood((1,1,1)))
    #for c in C.get_neighborhood((1,1,1)):
    #    print c

