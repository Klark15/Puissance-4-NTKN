def match_nul(gril):
    '''
    Fonction match_nul(gril):
    Renvoie True si la partie est nulle,
    c'est à dire si la ligne du haut est remplie,
    False sinon.
    '''
    gril=gril[::-1]
    for i in gril[-1]:
        if i==0:
            return False
    return True
    
 assert    
 assert
 assert       

def coup_aleatoire(gril,j):
    '''
    Fonction coup_aleatoire(gril,j):
    Joue un coup aléatoire pour le joueur j.
    On suppose la grille non pleine,
    condition indispensable pour ne pas se trouver dans une boucle  infinie !
    '''
    if match_nul(gril)==False:
        fin=0
        from random import randint
        while fin==0:
            x=randint(0,6)
            if coup_possible(gril,x)==True:
                jouer(gril,j,x)
                fin=1
    return gril
    
