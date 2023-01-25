
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

def placement_objet():
    for i in range(len(plateau)):
        for j  in range(len(plateau[i])):
            x, y = 25 + 75 * j , 35 + 200*i
            c, d = 75*(j+1) , 200*(i+1)
            plateau[i][j].placement(x, y, c, d)
            
def affichage_objet():
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            plateau[i][j].affichage()

def affichage_graphique():
    affichage_objet()
    affichage_Benlever()
    affichage_joueur()
           
def affichage_Benlever():
    rectangle(645 , 505, 775, 530, remplissage = "green")
    texte(650, 750, "Enlevez", taille=25)
   
def Action_Benlever(y, x):
    list = []
    if 645 < x < 775 and 505 < y < 530 and rangee != None:
        for ligne in plateau:
            while  ["" for element in ligne if element.GetSelection()] != []:
                list = [ligne.remove(element) for element in ligne if element.GetSelection()]
            if list != []:
                print(ia())
                return plateau, not joueur
    return plateau, joueur    
        

def reset_rangee():
    for i in plateau:
        for j in i:
            if j.GetSelection():
                return rangee
    return None

def affichage_victoire():
    texte(500, 550, "le joueur " + str(int(joueur) + 1) + " a gagné")                
                
def calclul(num_somme,num, plateau):
    print(num_somme ^ num)

        
def encadrement(num,list):
    for i in range(len(list)):
        n =0
        while 2**n < len(list[i]) or 2**n < num < 2**(n+1):
            n += 1
            if 2 **n == len(list[i]):
                return i

def calclul(num_somme,num):
    a_enlever = num_somme ^ num
    return  num - a_enlever

    
def num(list):
    sum = len( list[-1])
    for i in range(len(list)-1):
        sum = sum ^ len(list[i])
        print(sum)
    return sum

def ia():
    num_somme =  num(plateau)
    return calclul(num_somme, num([plateau[encadrement(num_somme ,plateau)]])), encadrement(num_somme ,plateau)

def affichage_joueur():
    texte(600, 70, "Tour du joueur " + str(int(joueur) + 1))

cree_fenetre(900,900)

plateau = plateau_marienbad([7,4,2,3])
rangee = None
joueur = False
placement_objet()



while True:
    
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

        plateau, joueur = Action_Benlever(x, y)
        rangee = reset_rangee()

    
    
    if tev == "Quitte":
        break
    

    affichage_graphique()
    mise_a_jour()
    
    if victoire(comptage_plateau()):
        efface_tout()
        affichage_victoire()
        attend_ev()
        break
print("Fin du jeu")
ferme_fenetre()
    


    

