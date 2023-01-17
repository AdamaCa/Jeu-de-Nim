

from fltk import *





class Id():

    def __init__(self):
        self.x = x
        self.y = y


    

    def verif_click(self, pos_souris):
        if pos_souris[0] > self.x and pos_souris[1] < self.y:
            return self.x , self.y
        return False

    def affichage(self, x, y, i, j):
        rectangle(x, y, i, j, remplissage = "purple")    

   