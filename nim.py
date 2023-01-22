
from fltk import * 
from ida import *


def ligne(n):
    return [ident() for i in range(n)]

def plateau_marienbad(rangée):
    return [ligne(i) for i in rangée]

def comptage_plateau():
    vide = 0
    for ligne in plateau:
        if ligne == []:
            vide += 1
    return len(plateau) - vide

def victoire(nbre_objet):
    return not bool(nbre_objet)




def affichage(plateau):
    for i in plateau:
        print(i)

def placement_objet(plateau):
    for i in range(len(plateau)):
        for j  in range(len(plateau[i])):
            x, y = 25 + 75 * j , 35 + 200*i
            c, d = 75*(j+1) , 200*(i+1)
            plateau[i][j].placement(x, y, c, d)
            
def affichage_objet():
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            plateau[i][j].affichage()

def affichage_graphique(plateau):
    affichage_objet(plateau)

            
def BoutonEffacement(plateau):
    pass
    
    
    
def Supression(plateau):
    for i in plateau:
        for l in i:
            if l.GetSelection():
                i.remove(l)
               

                
    return None, plateau
   


cree_fenetre(900,900)

plateau = plateau_marienbad((7, 5, 3, 1 ))
rangee = None
placement_objet(plateau)
while victoire(nbre_objet):

    ev = donne_ev()
    tev = type_ev(ev)


    efface_tout()

    if tev == "ClicGauche":
        x = ordonnee_souris()
        y = abscisse_souris()

        for i in plateau: #permet la selection

            for j in i:
                if j.verif_click((y,x)) and (i == rangee or rangee == None):
                    j.select()
                    rangee = i
                    break
        
        BoutonSuppr(plateau)
    
    rangee, plateau = BoutonEffacement(plateau)
    
    
    if tev == "Quitte":
        ferme_fenetre()
        break
    

    affichage_graphique()
    mise_a_jour()
    
    if victoire(comptage_plateau()):
        break
print("Fin du jeu")
ferme_fenetre()
    
    


    

