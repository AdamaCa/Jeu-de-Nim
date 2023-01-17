from fltk import *
import id

def ligne(n):
    return [id()]*n


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

    if tev == "ClickGauche":
        pass




    
