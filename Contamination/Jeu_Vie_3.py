from random import *
import pyxel

# Ce programme a pour but de reproduire le jeu de la vie, avec une grille finie.

#---------------------------------------------------------------------------------------------------------------------------------------------#
# Premièrement, l'utilisateur choisit la taille qu'il souhaite pour la grille grâce à cette boucle
# La taille maximale est 60; car si l'on excède cette valeur, les cellules sortent de l'écran.

goodTaille = False
maxTaille = 60

# Pour que le programme marche bien, il faut que la valeur entrée soit un integer, ce que permet cette boucle.
while goodTaille == False:
    
    tailleGrilleInput = input("Cher madame, cher monsieur, quelle taille souhaitez-vous pour la magnifique grille que nous allons choisir ?")
    
    # On vérifie si la string obtenue est bien constituée uniquement de nombres.
    if tailleGrilleInput.isdigit() == True:
        
        tailleGrille = int(tailleGrilleInput)
        
        # On vérifie que l'int est bien plus petit que la taille maximale de la grille, et on valide la taille pour sortir de la boucle.
        if tailleGrille <= maxTaille:
                
            goodTaille = True
                
        else:
                
            print("Cher bipède, vous voyez trop grand, c'est bien d'avoir de l'ambition, mais pas ici.\nLa taille maximale de la grille est 60 :)")
        
    else:
        
        print("Ah, je suis désolé mais vous avez essayé de me gruger là, c'est pas sympa...")


# Par défaut, le nombre de cellules vivantes est fixée à un quart des cellules. Vous pouvez changer cela grâce à la variable juste en dessous.
nbVivants = int((tailleGrille**2) / 4)

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Création de la fenêtre et chargement des ressources
widthScreen = 300
heightScreen = 200

pyxel.init(widthScreen, heightScreen)
pyxel.load("ressources.pyxres")

# Variables globales 
step = 0
grille = []

# Selon la taille de la grille, les cellules seront différentes, plus petites ou plus grandes. La marge entre elles changera donc aussi.
if tailleGrille <= 8:
    
    margeCellule = 8
    
elif tailleGrille <= 14:

    margeCellule = 5
    
elif tailleGrille <= 26:
    
    margeCellule = 3
    
else:
    
    margeCellule = 2

#-----------------------------------------------------------------------------------------------------------------#
# Informations sur les sprites, et sur leurs animations

buttonGreen = (0, 48, 0, 32, 32)
buttonYellow = (0, 80, 0, 32, 32)
buttonNext = (0, 112, 0, 32, 16)
buttonRestart = (0, 144, 0, 32, 16)

#-----------------------------------------------------------------------------------------------------------------#
# Animation des cellules vivantes
bigLivingCell = (0, 16, 0, 16, 16)
bigLivingCell0 = (0, 16, 0, 16, 16)
bigLivingCell1 = (0, 16, 16, 16, 16)
bigLivingCell2 = (0, 16, 32, 16, 16)
bigLivingCell3 = (0, 16, 48, 16, 16)
tabAnimBigLivingCell = [bigLivingCell0, bigLivingCell1, bigLivingCell2, bigLivingCell3]

bigLivingCellCounter = 0

middleLivingCell = (0, 176, 0, 8, 8)
middleLivingCell0 = (0, 176, 0, 8, 8)
middleLivingCell1 = (0, 176, 8, 8, 8)
tabAnimMiddleLivingCell = [middleLivingCell0, middleLivingCell1]

littleLivingCell = (0, 192, 0, 4, 4)
tabAnimLittleLivingCell = [littleLivingCell]

tinyLivingCell = (0, 208, 0, 1, 1)
tabAnimTinyLivingCell = [tinyLivingCell]

# Selon la taille de la grille, on adopte des sprites et animations différentes
if tailleGrille <= 8:
    
    tabAnimLivingCell = tabAnimBigLivingCell
    
elif tailleGrille <= 14:
    
    tabAnimLivingCell = tabAnimMiddleLivingCell
    
elif tailleGrille <= 26:
    
    tabAnimLivingCell = tabAnimLittleLivingCell
    
else:
    
    tabAnimLivingCell = tabAnimTinyLivingCell
    
    
livingCell = tabAnimLivingCell[0]
animLivingCell = 0

#-----------------------------------------------------------------------------------------------------------------#
# Animation des cellules mortes
bigDyingCell = (0, 32, 0, 16, 16)
bigDyingCell0 = (0, 32, 0, 16, 16)
bigDyingCell1 = (0, 32, 16, 16, 16)
bigDyingCell2 = (0, 32, 32, 16, 16)
bigDyingCell3 = (0, 32, 48, 16, 16)
tabAnimBigDyingCell = [bigDyingCell0, bigDyingCell1, bigDyingCell2, bigDyingCell3]

bigDyingCellCounter = 0

middleDyingCell = (0, 184, 0, 8, 8)
middleDyingCell0 = (0, 184, 0, 8, 8)
middleDyingCell1 = (0, 184, 8, 8, 8)
tabAnimMiddleDyingCell = [middleDyingCell0, middleDyingCell1]

littleDyingCell = (0, 200, 0, 4, 4)
tabAnimLittleDyingCell = [littleDyingCell]

tinyDyingCell = (0, 216, 0, 1, 1)
tabAnimTinyDyingCell = [tinyDyingCell]


if tailleGrille <= 8:
    
    tabAnimDyingCell = tabAnimBigDyingCell
    
elif tailleGrille <= 14:
    
    tabAnimDyingCell = tabAnimMiddleDyingCell
    
elif tailleGrille <= 26:
    
    tabAnimDyingCell = tabAnimLittleDyingCell
    
else:
    
    tabAnimDyingCell = tabAnimTinyDyingCell
    


dyingCell = tabAnimDyingCell[0]
animDyingCell = 0

#-----------------------------------------------------------------------------------------------------------------#
# Paramètres d'animation (vitesse)
animCounter = 0
speedAnimCell = 25

#-----------------------------------------------------------------------------------------------------------------#
# Variable nécessaires à la gestion de la mécanique des boutons.
# (coordonnées, placement, si on peut appuyer sur le bouton...)

margeX = 10
margeY = 10

livingCellButton = buttonGreen
xLivingCellButton = margeX
yLivingCellButton = margeY
xIcon = xLivingCellButton + buttonGreen[3] / 4
yIcon = yLivingCellButton + buttonGreen[4] / 4

dyingCellButton = buttonYellow
xDyingCellButton = widthScreen - margeX - buttonGreen[3] 
yDyingCellButton = margeY
xIcon2 = xDyingCellButton + buttonGreen[3] / 4
yIcon2 = yDyingCellButton + buttonGreen[4] / 4

xRestartButton = margeX
yRestartButton = heightScreen - margeY - buttonRestart[4]

xNextButton = widthScreen - margeX - buttonNext[3]
yNextButton = heightScreen - margeY - buttonNext[4]

# Cette variable sotcke le changement manuel de cellule (c'est à dire si l'on tape sur une cellule, est ce qu'elle va devenir vivante ou morte).
placeWhat = 0

canPush = True
canPushTimer = 0
canPushChrono = 10


def update():
    """
        Gère le jeu au fil du temps.
    """
    
    # On déclare les variables globales qui ont besoin d'être passé d'un instant t à un autre, les utiliser en tant que variables globales est la façon la plus simple de les passer à l'instant suivant.
    
    global step
    global grille
    
    global animLivingCell
    global animCounter
    global bigLivingCell
    global bigDyingCell
    global animDyingCell
    global canPushTimer
    global canPush
    global livingCell
    global dyingCell
    global bigLivingCellCounter
    global bigDyingCellCounter
    
    # On efface les dessins fait à l'écran au temps précédent pour éviter les bugs d'affichage, et on laisse apparaître la souris.
    pyxel.cls(0)
    pyxel.mouse(True)
    
    # Si le jeu vient de commencer (ou que le joueur vient de le réinitialiser), on récrée une nouvelle grille.
    if step == 0:
        
        grille = generation_grille(tailleGrille)
        grille = place_cellules_alea(grille, nbVivants)
        
        step = 1
        
    
    # Si un bouton a été touché, on place un petit temps durant lequel on ne peut plus le toucher, sinon il s'active en boucle.
    if canPush == False:
        
        canPushTimer = canPushTimer + 1
        
        if canPushTimer >= canPushChrono:
            
            canPush = True
            canPushTimer = 0
    
    
    # Le système d'animation.
    animCounter = animCounter + 1
    
    # A chaque intervalle speedAnimCell, on passe à l'étape suivante de l'animation.
    if animCounter % speedAnimCell == 0:
        
        animLivingCell = animLivingCell + 1
        animDyingCell = animDyingCell + 1
        bigLivingCellCounter = bigLivingCellCounter + 1
        bigDyingCellCounter = bigDyingCellCounter + 1
        
        # Gère l'animation des cellules
        if animLivingCell >= len(tabAnimLivingCell):
            
            animLivingCell = 0
            animDyingCell = 0
        
        # Gére l'animation des têtes sur les boutons.
        if bigLivingCellCounter >= len(tabAnimBigLivingCell):
            
            bigLivingCellCounter = 0
            bigDyingCellCounter = 0
        
        # Met à jour l'animation
        bigDyingCell = tabAnimBigDyingCell[bigDyingCellCounter]
        bigLivingCell = tabAnimBigLivingCell[bigLivingCellCounter]
        livingCell = tabAnimLivingCell[animLivingCell]
        dyingCell = tabAnimDyingCell[animDyingCell]
        
    
    # On active la fonction gérant l'affichage et l'intéractivité du jeu.
    manageInterface(grille)
        
    
    
    
def draw():
    """
        Cette fonction est censé gérer l'affichage du jeu. Elle doit être présente et fonctionne de paire avec update.
        Mais je trouvais plus pratique d'utiliser uniquement update, donc je n'ai pas utiliser celle-ci.
        Elle doit cependant être présente dans tous les cas, donc je l'ai laissé là.
    """
    pass
    
    
def detectCollision(item):
    """
        Détecte s'il y a collision entre la souris et un objet (une cellule ou un bouton). Renvoie True s'il y a collision, sinon renvoit False.
        item doit être un tuple ou un tableau de la forme (xCentre, yCentre, largeur, hauteur)
    """
    
    # Vérifie la collision
    if (pyxel.mouse_x < item[0] + item[2] / 2 and pyxel.mouse_x > item[0] - item[2] / 2) and (pyxel.mouse_y < item[1] + item[3] / 2 and pyxel.mouse_y > item[1] - item[3] / 2):
        
        return True
    
    else:
        
        return False
    
    
    
def manageInterface(grille):
    """
        Cette fonction gère tout l'affichage et l'intéractivité des cellules, et du jeu en général.
    """
    
    global canPush
    global step
    global placeWhat
    global livingCellButton
    global dyingCellButton
    
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    # On gère d'abord l'intéractivité avec les boutons.
    # Si un des boutons est touchée et que le joueur fait un clic avec sa souris, et que le bouton peut être touché, il effectue l'action correspondante.
    
    if canPush and detectCollision((xNextButton + buttonNext[3] / 2, yNextButton + buttonNext[4] / 2, buttonNext[3], buttonNext[4])) and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT)):
        
        # Si le bouton next est pressé, la grille s'actualise et passe à l'étape suivante.
        grille = update_grille(grille)
        canPush = False
    
    
    if canPush and detectCollision((xRestartButton + buttonRestart[3] / 2, yRestartButton + buttonRestart[4] / 2, buttonRestart[3], buttonRestart[4])) and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT)):
        
        # Si le bouton restart est touché, le jeu génère une nouvelle grille.
        step = 0
        canPush = False
        
        
        
    if canPush and detectCollision((xLivingCellButton + livingCellButton[3] / 2, yLivingCellButton + livingCellButton[4] / 2, livingCellButton[3], livingCellButton[4])) and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT)):
        
        # Si le bouton Cellules vivantes est pressé, le joueur pourra maintenant placer des cellulles vivantes dans la grille
        placeWhat = 0
        canPush = False
        
        
    if canPush and detectCollision((xDyingCellButton + dyingCellButton[3] / 2, yDyingCellButton + dyingCellButton[4] / 2, dyingCellButton[3], dyingCellButton[4])) and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT)):
        
        # Si le bouton Cellules mortes est pressé, le joueur pourra maintenant placer des cellulles mortes dans la grille
        placeWhat = 1
        canPush = False
        
    
    # Selon la cellule que l'on peut placer dans la grille, les boutons correspondants à chaque cellule change de couleur pour indiquer à l'utilisateur ce qu'il est en train de placer.
    if placeWhat == 0:
        
        livingCellButton = buttonGreen
        dyingCellButton = buttonYellow
        
    else:
        
        livingCellButton = buttonYellow
        dyingCellButton = buttonGreen
    
    
    #----------------------------------------------------------------------------------------------------------------------------------#
    # Interfaces des boutons
    # On dessine simplement tous les boutons du jeu.
    
    margeX = 10
    margeY = 10
    
    pyxel.blt(xLivingCellButton, yLivingCellButton, livingCellButton[0], livingCellButton[1], livingCellButton[2], livingCellButton[3], livingCellButton[4], 0)
    pyxel.blt(xIcon, yIcon, bigLivingCell[0], bigLivingCell[1], bigLivingCell[2], bigLivingCell[3], bigLivingCell[4], 0)


    pyxel.blt(xDyingCellButton, yDyingCellButton, dyingCellButton[0], dyingCellButton[1], dyingCellButton[2], dyingCellButton[3], dyingCellButton[4], 0)
    pyxel.blt(xIcon2, yIcon2, bigDyingCell[0], bigDyingCell[1], bigDyingCell[2], bigDyingCell[3], bigDyingCell[4], 0)
    
    pyxel.blt(xRestartButton, yRestartButton, buttonRestart[0], buttonRestart[1], buttonRestart[2], buttonRestart[3], buttonRestart[4], 0)
    
    pyxel.blt(xNextButton, yNextButton, buttonNext[0], buttonNext[1], buttonNext[2], buttonNext[3], buttonNext[4], 0)
    
    
    #----------------------------------------------------------------------------------------------------------------------------------#
    # Grille de cellules
    # Dans ces boucles, on dessine chaque cellule de façon à ce que la grille formée soit centrée.
    # On détecte aussi un clique sur les cellules, qui peut les changer en cellules mortes ou vivantes selon l'option choisie par l'utilisateur.
    
    # On détermine d'abord les coordonnées de la première cellule (en haut à gauche)
    dimensionGrille = len(grille) * (margeCellule + livingCell[3]) - margeX
    xFirstPlace = widthScreen / 2 - dimensionGrille / 2
    yFirstPlace = heightScreen / 2 - dimensionGrille / 2
    
    nextY = yFirstPlace
    
    
    for i in range (len(grille)):
        
        nextX = xFirstPlace
        
        for k in range (len(grille)):
            
            # Si l'utilisateur appuye sur la cellule, elle se change en la cellule correspondante.
            if detectCollision((nextX + livingCell[3] / 2, nextY + livingCell[4] / 2, livingCell[3], livingCell[4])) and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT)):
                
                if placeWhat ==0:
                    
                    grille[i][k] = 1
                    
                else:
                    
                    grille[i][k] = 0
            
            # On affiche le type de la cellule.
            if grille[i][k] == 1:
                
                pyxel.blt(nextX, nextY, livingCell[0], livingCell[1], livingCell[2], livingCell[3], livingCell[4], 0)
                
            else :
                
                pyxel.blt(nextX, nextY, dyingCell[0], dyingCell[1], dyingCell[2], dyingCell[3], dyingCell[4], 0)
            
            # On définit les nouvelles coordonnées de la prochaine cellule
            nextX = nextX + margeCellule + dyingCell[3]
        
        # On définit les nouvelles coordonnées de la prochaine cellule
        nextY = nextY + margeCellule + dyingCell[4]  



def generation_grille(taille):
    ''' genere un tableau de tableaux de longueur et de largeur valant taille et  contenant des zéros (cellules mortes)
        taille <- int '''
    
    # On créé la grille
    grille = []
    
    # On crée le nombre de ligne 'taille' que l'on veut pour la grille
    for i in range (taille):
        
        grille.append([])
        
        # On remplit cette ligne de cellules mortes, avec un nombre 'taille' de 0
        for k in range (taille) :
            
            grille[i].append(0)
            
    return grille
    
    

def place_cellules_v(grille, cellules_vivantes):
    '''place des cellules vivantes dans la grille (matérialisés par des 1)
    grille <- généré grace à la fonction generation_grille()
    cellules_vivantes <- tableau contenant les tuples de coordonnées des cellules vivantes
    renvoie la grille modifiée
    '''
    
    # Pour chaque couple de coordonnées dans cellules_vivantes
    for i in (cellules_vivantes):
        
        # On cherche la ligne correspondante (i[1]) et on place 1 dans la colonne i[0] qui croise cette ligne.
        # On obtient alors bien un 1 aucx coordonnées demandées
        grille[i[1]][i[0]] = 1
        
    return grille



def choose_alea(grille, cellulesToAdd):
    ''' Cette fonction choisit un nombre aléatoire à placer différents de ceux déja dans le tableau. Elle est séparé de place_alea pour pouvoir s'appeler elle-même et utiliser une récurrence plus facilement. '''
        
    # On choisit aléatoirement des coordonnées
    toAddX = randrange(0, len(grille))
    toAddY = randrange(0, len(grille))
    
    # Pour chaque cellule déjà ajoutée
    for k in (cellulesToAdd):
        
        # Si la cellule existe déjà, on rappelle la fonction pour en avoir une autre 
        if k == (toAddX, toAddY):
                    
            return choose_alea(grille, cellulesToAdd)
    
    # Si les coordonnées de la cellule ne sont pas déjà utilisée, on l'ajoute au tableau à ajouter.
    cellulesToAdd.append((toAddX, toAddY))        
    return cellulesToAdd
                           
                           

def place_cellules_alea(grille, nombre):
    ''' place de manière aléatoire un nombre de cellules vivantes dans la grille
        grille <- généré grace à la fonction generation_grille()
        renvoie la grille modifiée
        '''
    # On crée le tableau contenant les cellules vivantes que l'on aura à ajouter
    cellulesToAdd = []
    
    # On crée un tuple par nombre de cellule voulu
    for i in range (nombre):
        
        # Si le tableau n'est pas vide, on vérifie que les coordonnées de cette cellule n'existe pas déja
        if cellulesToAdd != []:
            
            # On appelle la fonction qui choisit une cellule aléatoire.
            cellulesToAdd = choose_alea(grille, cellulesToAdd)
            
        else:
            
            # On choisit aléatoirement des coordonnées
            toAddX = randrange(0, len(grille) - 1)
            toAddY = randrange(0, len(grille) - 1)
            cellulesToAdd.append((toAddX, toAddY))
    
    # On retourne le tableau modifié grâce à la fonction place_cellules_v
    return place_cellules_v(grille, cellulesToAdd)



def compte_voisins_vivants(grille,coord):
    ''' Compte le nombre de cellules vivantes voisines de la cellule de coordonnées (i,j), i représentant la colonne et j la ligne
        grille <- tableau de tableaux
        coord <- tuple contenant des entiers compris entre 0 et len(grille)-1
        renvoie un entier'''
    
    # On stocke chaque coordonnée séparément pour rendre le code plus explicite
    x = coord[0]
    y = coord[1]
    neighbourCounter = 0
    
    # Pour chaque case du plateau, on vérifie si les cases adjacentes contiennent une cellule en vie, si oui, on ajoute un au compteur de cellules vivantes.
    # On vérifie si la position à vérifier dans le tableau existe, pour ne pas créer de bugs.
    if x + 1 < len(grille):
        
        # On vérifie alors la case de droite
        if grille[y][x + 1] == 1:
            
            neighbourCounter = neighbourCounter + 1
            
        if y + 1 < len(grille):
            
            # Case bas droite
            if grille[y + 1][x + 1] == 1:
                
                neighbourCounter = neighbourCounter + 1
            
        if y - 1 >= 0:
            
            # Case haut droite
            if grille[y - 1][x + 1] == 1:
            
                neighbourCounter = neighbourCounter + 1
                
            
    if x - 1 >= 0:
        
        # Case gauche
        if grille[y][x - 1] == 1:
            
            neighbourCounter = neighbourCounter + 1
            
        if y + 1 < len(grille):
            
                # Case bas gauche
            if grille[y + 1][x - 1] == 1:
                
                neighbourCounter = neighbourCounter + 1
                
        if y - 1 >= 0:
                
            # Case haut gauche
            if grille[y - 1][x - 1] == 1:
                    
                neighbourCounter = neighbourCounter + 1
            
            
            
    if y + 1 < len(grille):
        
        # Case bas
        if grille[y + 1][x] == 1:
            
            neighbourCounter = neighbourCounter + 1
            
    if y - 1 >= 0:
        
        # Case haut
        if grille[y - 1][x] == 1:
            
            neighbourCounter = neighbourCounter + 1

    return neighbourCounter


  
def grille_voisins(grille):
    ''' genere une grille contenant le nombre de cellules vivantes voisines
    grille <- tableau de tableaux
    renvoie un tableau de tableaux
      '''
    
    # On crée la grille qu'on remplira ensuite
    grilleCount = []
    
    # Pour chaque ligne de la grille, on crée un tableau
    for i in range (len(grille)):
        
        grilleCount.append([])
        
        # Et pour chaque cellule de la ligne, morte ou vivante, on compte combien elle a de cellules voisines vivantes grâce à la fonction compte_voisins_vivants
        # On ajoute cette valeur à la même place qu'occupe la cellule évaluée dans la grille en paramètre, mais dans la nouvelle grille.
        for k in range (len(grille)):
            
            grilleCount[i].append( compte_voisins_vivants(grille,(k, i)) )
            
    return grilleCount



def update_grille(grille):
    ''' actualise la grille aprés un cycle de vie
    grille <- tableau de tableaux contenant les cellules vivantes et les cases vides.
    renvoie la grille modifiée'''
    
    grilleCount = grille_voisins(grille)
    
    # Pour chaque cellule de grille, on vérifie grâce à grilleCount combien de cellules vivantes lui sont adjacentes.
    for i in range (len(grille)):
        
        for k in range (len(grille)):
            
            if grille[i][k] == 1:
                
                # Si la cellule est vivante, et qu'il n'y a pas 2 ou 3 autres cellules vivantes autour d'elle, elle meurt.
                if grilleCount[i][k] != 2 and grilleCount[i][k] != 3:
                    
                    grille[i][k] = 0
                    
            # Si la cellule est morte et que 3 cellules vivantes lui sont adjacentes, elle naît.       
            if grille[i][k] == 0:
                
                if grilleCount[i][k] == 3:
                    
                    grille[i][k] = 1
                    
    return grille



def print_grille(grille):
    """
        Cette fonction servait simplement pour des tests avant que l'affichage pyxel soit mis en place.
        Je l'ai laissé là au cas où j'en ai besoin un jour pour je ne sais quelle raison.
    """
    for i in range (tailleGrille):
        
        print(grille[i])


# On lance le programme.
pyxel.run(update, draw)