import numpy as np
import time
import random


def printa_cubo(cubo):
    print len(cubo)
    for x in range(len(cubo)):
        for y in range(len(cubo)):
            for z in range(len(cubo)):
                print cubo[x][y][z].get_node()


def printa_lista(lista,who):
    print "\n\t\t#####\t",who,"\t####"
    
    for l in lista:
        print l.get_node()
    

def printa_node(n):
    node = n.get_node()
        
    print "\n\nNode\tCoord: ",node[0],"  G: ",node[1],"  H: ",node[2],"  Cost: ",node[3],"  Wall: ",node[4]
    if parent ==None:
        print "Parent Start" 
    else:
        parent = n[1].get_node()
        print "Parent\tCoord: ",parent[0],"  G: ",parent[1],"  H: ",parent[2],"  Cost: ",parent[3],"  Wall: ",parent[4]

class Node:
    def __init__(self,Cord,Obj):
        self.Cord = Cord 
        self.wall = False 
        self.H = calcula_heuristica(Cord,Obj)
        self.weigth = random.randint(0,9)
        self.parent = None
        self.cost = self.weigth + self.H
    def get_parent(self):
        return self.parent
    def set_parent(self,pai):
        self.parent = pai
    def get_heu(self):
        return self.H
    def set_wall(self):
        self.wall = True
    def get_wall(self):
        return self.wall
    def get_cord(self):
        return self.Cord
    def get_node(self):
        return (self.Cord,self.weigth,self.H,self.cost,self.wall,self.parent)
    def get_weigth(self):
        return self.weigth
    def set_weigth(self,weigth):
        self.weigth = weigth
    def set_cost(self,cost):
        self.Cost = self.weigth + cost
    def get_cost(self):
        return self.cost

class Cube:
    def __init__(self,dim,obstacles):
        self.End = (random.randint(0,dim-1),random.randint(0,dim-1),random.randint(0,dim-1))
        self.Start = (random.randint(0,dim -1 ),random.randint(0,dim -1),random.randint(0,dim-1))
        self.Cube = []
        for x in range(dim):
            for y in range(dim):
                for z in range(dim):
                    node = Node((x,y,z),self.End)
                    if random.random() < obstacles :
                        if (x,y,z) != self.Start and (x,y,z) != self.End:
                            node.set_wall()
                    self.Cube.append(node)
        self.Cube = np.array(self.Cube)
        self.Cube = self.Cube.reshape(dim,dim,dim)
        # demarca o start e end como custo zero
        self.Cube[self.Start[0]][self.Start[1]][self.Start[2]].set_weigth(0)
        self.Cube[self.End[0]][self.End[1]][self.End[2]].set_weigth(0)
    def get_cube(self):
        return self.Cube
    def get_start(self):
        return self.Start
    def get_end(self):
        return self.End
    def get_neighborhood(self,cord):
        cords = cord.get_cord()
        print "Procurando vizinhanca de",cords
        neighbor = []
        for a in (-1,0,1):
            x = a + cords[0]
            for b in (-1,0,1):
                y = b + cords[1]
                for c in (-1,0,1):
                    z = c + cords[2]
                    if (x==y and y==z):
                        pass
                    else:
                        if((x >= 0 and x < len(self.Cube)) and
                           (y >= 0 and y < len(self.Cube)) and
                           ((z >= 0) and z < len(self.Cube))):
                                neighbor.append(self.Cube[x][y][z])
                                
        return neighbor
    def calcula_custo(self,node,pai):
        custo = node.get_weigth()
        H = node.get_heu()
        custo = custo + H
        print "CAlculando o custo de ", node.get_cord()
        while(pai):
            if pai.get_parent() != None:
                break
            print "parent", pai.get_cord()
            weigth_pai  = pai.get_weigth()
            custo = custo + weigth_pai
            pai = pai.get_parent()
            time.sleep(1)

        print "\t\tCalcula custo =", custo
        return custo

def calcula_heuristica(Cord,End):
    a = Cord[0] - End[0]
    b = Cord[1] - End[1]
    c = Cord[2] - End[2]
    H = int(round(np.sqrt( np.square(a) + np.square(b) + np.square(c) ))) 
    return H    
def calcula_custo(no):
    print "recalcula custo"
    custo_no = 0
    pai = no 
    while( pai != None):
        print "pai.get_parent=",pai.get_node(),"custo",custo_no 
        custo_no = custo_no + pai.get_weigth()
        pai = pai.get_parent()
        time.sleep(0.5)
    no.set_weigth(custo_no)
       
    
class A_Estrela:
    def __init__(self):
        self.open = []
        self.closed = []
    def solve(self,dim,obstacles):
        c = Cube(dim,obstacles)
        cube = c.get_cube()

        end = c.get_end()
        end = cube[end[0]][end[1]][end[2]]
        
        start = c.get_start()
        start = cube[start[0]][start[1]][start[2]]
        H = calcula_heuristica(start.get_cord(),end.get_cord())
        self.open.append(start)
        printa_cubo(cube)

        print "Start === ",start.get_node()
        print "END  === ",end.get_node()
        



        while(True):
            print "\tAbertos",self.open
            print "\tFechados",self.closed
            if not self.open:
                print "\n\n\n\n NO SOLUTION\n\n\n\n"
                break
            current = self.open.pop(0)
            print "\tCurrent",current.get_node(),current
            self.closed.append(current)
            # pega o primeiro da lista
            if current == end:
                print "Chegou no final, current = end"
                break
            

            neighbors = c.get_neighborhood(current)
            print "\nVizinhanca \t:",neighbors,"\n"
            # gera vizinhanca e adiciona nos abertos
            new_open = []
            for n in neighbors:
                # so vale se nao for parede nem ele mesmo
                if n.get_wall() == False:
                    print "vizinho",n.get_node()
                    calcula_custo(n)
                    # verifica se a cordenada visitada ja ta nos abertos, se tiver compara os custos e poem o menor
                    self.open.append(n)
            printa_lista(self.open,"open")
            open_sorted = sorted(self.open,key = Node.get_cost)
            printa_lista(open_sorted,"open Sorted")
            print "closed",self.closed
            printa_lista(self.closed,"Closed")
            #custo = Calcula_Custo(n,current[0])
            #H = calcula_heuristica(n,end)
            
            time.sleep(3)

if  __name__ == "__main__":
    dim = 10
    obstacles = 0.6
    IA = A_Estrela()
    IA.solve(dim,obstacles)
