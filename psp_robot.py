#Creer une matrice carree via la fonction qui prend en entree un int qui correspond a la taille de la matrice
def squared_matrix(size):
    i = 0
    j = 0
    global my_matrix
    my_matrix = {}
    while i < size:
        my_matrix[j] = range(0, size)
        i += 1
        j += 1
    return my_matrix

#Creer une fonction qui va calculer le nombre correspondant a la moitie de la matrice
def index_middle_matrix(size):
    global index_middle_matrix
    index_middle_matrix = (size/2) - 1
    return index_middle_matrix

#Retourner les coordonnees de la moitie
def coordinate_middle(index_middle_matrix):
    i = 0
    for cle, valeur in my_matrix.items():
        #if i == index_middle_matrix:
        print cle, valeur
        i += 1

size = 6
squared_matrix(size)
index_middle_matrix(size)
coordinate_middle(index_middle_matrix)


#probleme parce que le parcours de la matrice ne se fait pas dans le bon sens, lecture de gauche à droite et pas en spirale
