from ida import ident

print( 7 ^ 2)

def num(list):
    sum = 0
    print(list)
    print(len(list))
    for i in range(len(list)):
        print("tour")
        sum = sum ^ len(list[i])
    return sum

def ligne(n):
    return [ident() for i in range(n)]

def plateau_marienbad(rangée):
    return [ligne(i) for i in rangée]

def encadrement(num, list):
    for i in range(len(list)):
        n =0
        while 2**n < len(list[i]) or 2**n < num < 2**(n+1):
            n += 1
            if 2 **n == len(list[i]):
                return i

def calclul(num_somme,num):
    a_enlever = num ^ num_somme
    print(num_somme, num,":", a_enlever)
    return  num -  a_enlever
    
plateau = plateau_marienbad([7, 3, 2 , 1])
num_somme = num(plateau)
num_rangee = num([plateau[encadrement(num_somme, plateau)]])
rangee = encadrement(num(plateau), plateau)
print(calclul(num_somme, num([plateau[encadrement(num_somme, plateau)]])))
print(rangee) 
