from fltk import * 
from ida import *


def ligne(n):
    list = []
    for i in range(n):
        r = ident()
        list.append(r)
    return list



def plateau_marienbad(rangée):
    list = []
    for i in rangée:
        list.append(ligne(i))
    return list


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




def affichage(plateau):
    for i in plateau:
        print(i)

def affichage_graphique(plateau):
    efface_tout()
    for i in range(len(plateau)):
        for j  in range(len(plateau[i])):
            x, y = 25 + 75 * j , 35 + 200*i
            c, d = 75*(j+1) , 200*(i+1)
            plateau[i][j].affichage(x, y, c, d)
            



cree_fenetre(900,900)

plateau = plateau_marienbad((7, 5, 3, 1 ))
nbre_objet = comptage_plateau(plateau)


while victoire(nbre_objet):

    ev = donne_ev()
    tev = type_ev(ev)


    efface_tout()
    affichage_graphique(plateau)
    mise_a_jour()
    
    

    if tev == "ClicGauche":
        print("fefefefefef")
        x = ordonnee_souris()
        y = abscisse_souris()
        print("wshs", x, y)
        
        for i in plateau:
            for j in i:
                if j.verif_click((y,x)):
                    j.select()
                    print("ta tzaidon")
                    break



    
