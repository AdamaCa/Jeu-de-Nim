
from fltk import * 
from ida import *


def ligne(n):
    return [ident() for i in range(n)]

def plateau_marienbad(rangée):
    return [ligne(i) for i in rangée]


def coup(plateau, k, i):
    if len(plateau[i]) < k:
        print("coup impossible")
        return plateau
    else:
        plateau[i] = plateau[i][:len(plateau[i])-k]
        return plateau

def comptage_plateau(pl):
    vide = 0
    for i in range(len(pl)):
        if pl[i] == []:
            vide += 1
    return len(pl) - vide

def victoire(nbre_objet):
    return bool(nbre_objet)

def placement_objet(plateau):
    for i in range(len(plateau)):
        for j  in range(len(plateau[i])):
            x, y = 25 + 75 * j , 35 + 200*i
            c, d = 75*(j+1) , 200*(i+1)
            plateau[i][j].placement(x, y, c, d)
            
def affichage_objet(plateau):
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            plateau[i][j].affichage()

def affichage_graphique(plateau):
    affichage_objet(plateau)
    affichage_BEnlevez()
    affichage_joueur(" 1")
           
def affichage_BEnlevez():
    texte(500, 750, "Enlevez", taille=25)
    rectangle(490 , 750 , 720, 785)
   
def Action_BEnlevez(plateau,rangee, y, x):
    if 490 < x < 720 and 750 < y < 785 and rangee != None:
        for ligne in plateau:
            while  ["" for element in ligne if element.GetSelection()] != []:
                list = [ligne.remove(element) for element in ligne if element.GetSelection()]
            if list != []:
                break
        rangee = None
    return rangee, plateau
   
def affichage_joueur(joueur):
    texte(600, 70, "Tour du joueur" +str(joueur))

def chg_j(joueur):
    return not joueur

cree_fenetre(900,900)

plateau = plateau_marienbad((7, 5, 3, 1 ))
nbre_objet = comptage_plateau(plateau)
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
                
        rangee, plateau = Action_BEnlevez(plateau, rangee, x, y)

    
    
    if tev == "Quitte":
        ferme_fenetre()
        break
    
    
    affichage_graphique(plateau)
    mise_a_jour()


    
