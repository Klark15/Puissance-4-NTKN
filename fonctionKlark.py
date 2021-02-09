def grille_vide():
    '''
    Fonction grille_vide():
    La fonction construit un tableau à deux dimensions de taille 6 x 7 :
    6 lignes et 7 colonnes.
    Chaque case contient la valeur 0.
    La fonction ne prend pas d'argument.
    La foncion renvoie le tableau.
    '''
    grille=[[0 for j in range(7)] for i in range(6)]
    return grille
assert len(grille_vide())==6
assert len(grille_vide()[0])==7
def affiche(gril) :
    '''
    Fonction affiche(gril):affiche une grille de 6 lignes sur 7 colonnes.
    Une ligne prend en argument un tableau de taille 6 x 7.
    Une ligne est notée lig et prend une valeur entre 0 et 5,
    la ligne 0 est située en bas.
    Une colonne est notée col et prend une valeur entre 0 et 6,
    la colonne 0 est située à gauche.
    Dans la grille:
    la valeur 0 représente une case vide, représentée par un.
    la valeur 0 représente un pion du joueur 1, représenté par un x.
    la valeur 2 représente un pion du joueur 2, représenté par un 0.'''
    num = ['  0 ','1 ','2 ','3 ','4 ','5 ','6 ']
    n = 6
    for k in num :
        print (k, end='')
    print ('')
    for i in gril :
        n = n - 1
        print (n, end='')
        for j in i :
            if j == 0 :
                print ('|.', end ='')
            if j == 1 :
                print ('|x', end ='')
            if j == 2 :
                print ('|O', end ='')
        print ("|")
def coup_possible(grille, col) :
    '''
    Fonction coup_possible(gril, col):
    Détermine si possible de jouer dans la colonne col.
    Prend en argument la grille, tableau de 5x6, avec la position des pions des joueurs et un entier, le numéro de colonne col, False sinon.
    Il est possible de joueur dans la colonne col, si il existe une case avec la valeur 0 dans cette colonne.
    '''
    if grille[0][col] == 1 :
        return False
    if grille[0][col] == 2 :
        return False
    if grille[0][col] == 0 :
        return True
assert coup_possible(grille_vide(),0) == True
assert coup_possible([[0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 0, 0]],3) == False
