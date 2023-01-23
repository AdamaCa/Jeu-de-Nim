

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
        self.selection = not self.selection
           
    def placement(self, x, y, i, j):
        self.pos_x = (x,i)
        self.pos_y = (y, j)
        self.rectangle = rectangle(x, y, i, j, remplissage = "purple")
    
    def affichage(self):
        if not self.selection: 
            self.rectangle = rectangle(self.pos_x[0], self.pos_y[0], self.pos_x[1], self.pos_y[1], remplissage = "purple")
        else:
            self.rectangle = rectangle(self.pos_x[0], self.pos_y[0], self.pos_x[1], self.pos_y[1], remplissage = "black")
            
    def GetSelection(self):
        return self.selection

                

   