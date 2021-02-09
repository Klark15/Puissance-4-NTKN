def jouer(grille, j, col) :
'''
Fonction jouer (gril, j, col):
Fonction qui joue un coup du joueur j dans la colonne col de la grille.
Arguments:
gril est la grille de 5 6 avec les pions des joueurs 
j est un entier qui a la valeur 1 ou 2 suivant le joueur 
col est entier entre 0 et 6, désigne une colonne non pleine de la grille.
Si j vaut 1 la première case vide de la colonne col prendra la valeur 1
Si j vaut 2 la première case vide de la colonne col prendra la valeur 2
'''
    k = [5,4,3,2,1,0]
    for i in k :
        if grille[i][col] == 0 :
            if j == 1 :
                grille[i][col] = 1
                return grille
            if j == 2:
                grille[i][col] = 2
                return grille
assert jouer(grille_vide(),1,2) == [[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0]]
assert jouer([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0]],2,2) == [[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0]]
 
 def horiz (gril,j,lig) :
 '''
 Fonction horiz(gril, j, lig, col):
 Détermine si il y a un alignement horizontal de 4 pions du joueur j
 à partir de la case (lig, col).
 arguments:
 gril la grille avec les pions.
 j le joueur, un entier avec la valeur 1 ou 2
 lig la ligne, unentier avec la valeur entre 0 et 5
 col la colonne, un entier avec la valeur entre 0 et 3
 Renvoie True si c'est le cas.
 '''
    tabl = gril
    m = 0
    if tabl[lig][0] == j and tabl[lig][1] == j and tabl[lig][2] == j and tabl[lig][3] == j :
        return True
    else :
        return False
    if tabl[lig][1] == j and tabl[lig][2] == j and tabl[lig][3] == j and tabl[lig][4] == j :
        return True
    else :
        return False
    if tabl[lig][2] == j and tabl[lig][3] == j and tabl[lig][4] == j and tabl[lig][5] == j :
        return True
    else :
        return False
    if tabl[lig][3] == j and tabl[lig][4] == j and tabl[lig][5] == j and tabl[lig][6] == j :
        return True
    else :
        return False 
assert horiz([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 2, 1, 0, 0]],1,5) == False
assert horiz([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [2, 2, 2, 2, 0, 0, 0]],2,5) == True
 
 def vert (gril,j,lig,col) :
 '''
 Fontion vert(gril, j, lig, col):
 Détermine si il y a alignement vertical de 4 pions du joueur j
 à partir de la case (lig, col).
 arguments:
 grill la grille avec les pions.
 j le joueur, un entier avec la valeur 1 ou 2
 lig la ligne, un entier avec la valeur entre 0 et 2
 col la colonne, un entier avec la valeur entre 0 et 6
 Renvoie True si c'est le cas.
 '''
    tabl = gril
    if tabl[lig][col] == j and tabl[lig+1][col] == j and tabl[lig+2][col] == j and tabl[lig+3][col] == j :
        return True
    else :
        return False
assert vert([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0]],1,2,0) == False
assert vert([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0]],2,2,0) == True
