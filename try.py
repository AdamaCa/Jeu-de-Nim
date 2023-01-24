


def encadrement(list):
    for i in range(len(list)):
        n =0
        while n < len(list[i]):
            n = n
            if n == len(list[i]):
                return i 

def calclul(rangee, num_somme,num):
    a_enlever = num_somme ^num
    return rangee , num - a_enlever



print(encadrement([[0,0,0], [0,0,0,0], [0,0]]))