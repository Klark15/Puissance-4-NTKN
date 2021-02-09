def diag_haut(gril, j ,lig, col):
    '''
    Fonction diag_haut(gril, j, lig, col):
    Détermine si il y a un alignement diagonal vers le haut de 4 pions du joueur j à partir de la cas (lig, col).
    Arguments:
    gril la grille avec les pions.
    j le joueur, un entier avec la valeur 1 ou 2
    lig la ligne, un entier avec la valeur entre 0 et 2
    col la colonne, un entier avec la valeur entre 0 et 6
    Renvoie True si c'est le cas, False sinon.
     '''
    nbr=0
    if col<=3:
        for i in range (4):
            if gril[lig+i][col+i]==j:
                nbr=nbr+1
    if nbr==4:
        return True
    nbr=0
    if col>=3:
        for i in range (4):
            if gril[lig+i][col-i]==j:
                nbr=nbr+1
    if nbr==4:
        return True
    return False
    
assert diag_haut
assert diag_haut
    
    def victoire(gril,j):
    '''
    fonction victoire(gril, j):
    Renvoie un booléen True si le joueur j a gagné, False sinon.
    Fait appel aux fonctions horiz(), vert(), diag_haut() et diag_bas()
    '''
    x = [horiz, vert, diag_haut, diag_bas]
    for i in (len(x)):
        if j[i] in gril:
            return True
        else:
            return False
            
assert victoire
assert victoire 
