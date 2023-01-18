

from operator import pos
from fltk import *





class ident():

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.selection = False
        self.rectangle = 0


    

    def verif_click(self, pos_souris):
        if self.pos_x[0] <= pos_souris[0] <= self.pos_x[1]  and self.pos_y[0] < pos_souris[1] < self.pos_y[1]:
            return True
        return False
    
    
    def select(self):
        self.selection = True
           
        
        
    def affichage(self, x, y, i, j):
        self.pos_x = (x,i)
        self.pos_y = (y, j)
        if not self.selection: 
            self.rectangle = rectangle(x, y, i, j, remplissage = "purple")
        else:
            self.rectangle = rectangle(x, y, i, j, remplissage = "black")
                

   