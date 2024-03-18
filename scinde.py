import numpy as np
import random

# Introduire le nombre de sommets :
while True :
    try:
        nombreDeSommets = int( input("Donner le nombre de sommets : ") )
        if nombreDeSommets < 1:
            print("le nombre de sommet doit etre strictement positif , retry ")
            continue
        break
    except ValueError :
        print("valeur invalide , donner un nombre positif ")

# Introduire les aretes :
aretes =[]
for i in range( nombreDeSommets ) :
    for j in range( i +1 , nombreDeSommets ) :
        while True :
            arete = input( f"les sommets {i+1} et {j+1} sont ils adjacents (repondre par 1 ou 0): ")
            if arete != '1' and arete != '0' :
                print(f"valeur invalide , veuillez repondre par 1 ou 0")
                continue
            break
        if arete.lower() == "1":
            aretes.append(( i , j ) )

# Calculer la matrice d’adjacence :
matrice_adjacence = np.zeros([ nombreDeSommets , nombreDeSommets ])
for i in range( nombreDeSommets ) :
    for j in range(i , nombreDeSommets ) :
        if (i , j ) in aretes :
            matrice_adjacence [ i ][ j ] = 1
            matrice_adjacence [ j ][ i ] = 1
   
# Fonction pour definir les voisins :
def voisins (s , matrice_adjacence ) :
    return [ sommet for sommet , adjacent in enumerate ( matrice_adjacence [ s ]) if adjacent ]

# Fonction pour verifier si un graphe est une clique :
def clique (matrice_adjacence) :
    for i in range(len(matrice_adjacence)):
        for j in range(len(matrice_adjacence)):
            if matrice_adjacence[i,j] == 0 and i != j:
                return 0
    return 1

# fonction complimentaire de G
def complimentaire(m):
    for i in range(len(m)):
        for j in range(len(m)):
            if(m[i][j] == 0):
                m[i][j] = 1
            else:
                m[i][j] = 0
    return m

# fonction pour verifier si le graphe est triangulé
def triangule(matrice_adjacence,nombreDeSommets):
    n = []
    w = random.sample(range(nombreDeSommets),nombreDeSommets)

    les_sommets = {}
    for i in range ( nombreDeSommets ) :
        les_sommets [ i ] = {'voisin_dans_n': 0}

    if len(w) < 2:
        return 1
    else :
        x = w.pop()
        n.append(x)
        for i in voisins(x,matrice_adjacence):
            les_sommets[i]["voisin_dans_n"] += 1

        while w != []:
            x = w[0]
            for i in w:
                if les_sommets[i]["voisin_dans_n"] > les_sommets[x]["voisin_dans_n"]:
                    x = i
            les_voisins_dans_n =[]
            for i in voisins(x,matrice_adjacence):
                if i in n:
                    les_voisins_dans_n.append(i)
            if len(les_voisins_dans_n) < 2:
                n.append(x)
                for i in voisins(x,matrice_adjacence):
                    les_sommets[i]["voisin_dans_n"] += 1
                w.remove(x)
            else:
                matrice_adjacence_des_voisins = np.zeros([ len(les_voisins_dans_n) , len(les_voisins_dans_n) ])
                k=0
                for i in les_voisins_dans_n:
                    t=0
                    for j in les_voisins_dans_n:
                        matrice_adjacence_des_voisins[k][t] = matrice_adjacence[i][j]
                        t+=1
                    k+=1
                if not clique(matrice_adjacence_des_voisins):
                    return 0
                else :
                    n.append(x)
                    for i in voisins(x,matrice_adjacence):
                        les_sommets[i]["voisin_dans_n"] += 1
                    w.remove(x)
        return 1

# virifie si le graphe G et son complimentaire son triangulé
if triangule(matrice_adjacence,nombreDeSommets) and triangule(complimentaire(matrice_adjacence),nombreDeSommets):
    print("Le graphe G est scindé")
else:
    print("Le graphe G n'est pas scindé")