def grille_init(default):
    
    """
        Cette fonction renvoie un tableau initialTab constitué du nombre de lignes et de colonnes choisi par l'utilisateur.
        
        La boucle for permet de créer le tableau:
        - on crée un tableau temporaire tabToAdd qu'on remplit avec le nombre demandé de 0 (stocké dans columns)
        - on ajoute tabToAdd au tableau final.
        
        On répète cette action le nombre de fois choisi par l'utilisateur (stocké dans line). On crée alors le tableau initial contenant d'autres tableaux, contenant eux-mêmes des 0.

        La boucle renvoit le tableau.
        La boucle prend en argument default, pour si besoin, entrer les paramètres par défaut sans les demander
    """
    
    initialTab = []
    
    if default == "Def":
        
        columns = 7
        lines = 6
        
    else:
        
        columns = int( input( "Définissez la taille de votre grille.\nChoisissez le nombre de colonnes avec lesquelles vous souhaitez jouer.") )
        lines = int( input( "Choisissez le nombre de lignes avec lesquelles vous souhaitez jouer.") )


    for k in range (lines):
        
        tabToAdd = [0] * columns
        initialTab.append(tabToAdd)
            
    return initialTab       
         
        
        
def line_init (tab,Type):
    
    """
        Cette fonction trace les lignes de délimitation du tableau tab de la bonne longueur selon sa taille.
        
        On stocke le nombre de colonnes à afficher dans columnNumber, puis on trace la ligne de délimitation à chaque colonne grâce à la boucle for.
        On affiche un caractère autre à la fin pour fermer la ligne de délimitation.
        
        La fonction prend en argument "Type", c'est à dire le type de ligne a tracer:
        - first pour la première ligne du tableau.
        - last pour la dernière ligne du tableau.
        - non-nommé, pour toutes les lignes intermédiaires.
    """
    
    columnNumber = len(tab[0])
    
    if Type == "first":
    
        print ("┌───", end = "")
        
        for k in range (columnNumber - 1):
            
            # On met -1 car une "case" de la ligne a déjà été tracée lorsqu'on a affiché ┌───
    
            print ("┬───", end = "")
        
        print("┐")
    
    elif Type == "last":
    
        print ("└───", end = "")
        
        for k in range (columnNumber - 1):
            
            # On met -1 car une "case" de la ligne a déjà été tracée lorsqu'on a affiché └───
    
            print ("┴───", end = "")
        
        print("┘")
        
    else:
        
        print("├───",end = "")
        
        for k in range (columnNumber-1):
    
            print ("┼───", end = "")
        
        print("┤")
    

def affichage_grille (tab):
    
    """
        Cette fonction affiche le tableau demandé en argument.
        
        On trace d'abord la première ligne de délimitation du tableau.
        On stocke le nombre de ligne et de colonne grâce à la fonction len().
        
        Pour chaque ligne de valeur;
        - on affiche pour chaque valeur présente dans la ligne: | puis la valeur.
        - on affiche | pour fermer la ligne de valeur.
        - on trace une ligne de délimitation en dessous de ce que l'on vient d'afficher.
    """
    
    line_init (tab, "first")
    lineNumber = len(tab)
    columnNumber = len(tab[0])
    
    
    for line in range (lineNumber):
        
        for column in range (columnNumber):
            
            if tab[line][column] == 0:
                
                placeToShow = " "
                
            elif tab[line][column] == 1 :
            
                placeToShow = "•"
                
            else :
            
                placeToShow = "×"
            
            print ("│", placeToShow, "", end = "")
            
        print ("│")
        
        if line == lineNumber-1:
            
            # Car line = lineNumber = len(tab). Par exemple Si on a 8 lignes, len(tab) = 8, mais dans la boucle for de
            # line, la console va compter prendre line pour 8 valeurs: 0, 1, 2, 3, 4, 5, 6, 7 (mais pas 8). La dernière ligne
            # est alors désignée par 7, donc par lineNumber - 1 car lineNumber = 8.
            
            line_init (tab, "last")
            
        else:
            
            line_init (tab, "other")
        
        
def colonne_libre(tab, colonne):
    
    """
        Cette fonction vérifie si la colonne choisie est existante et libre. Si c'est le cas elle renvoit True, sinon elle renvoit False.
        
        La première boucle if vérifie ces conditions:
        - si la colonne choisie a un indice supérieure à celle ayant l'indice maximum, alors elle n'existe pas.
        - la première colonne étant la colonne 0, si la colonne choisie est négative, alors elle n'existe pas.
        
        La boucle else vérifie:
        - si le haut de la colonne est remplie ( donc différent de 0 ), alors on ne peut plus insérer de jetons.
        On ne peut pas rassembler cette condition avec les 2 autres de la boucle if, ou la mettre dans une boucle elif car cela donne lieu à une erreur (la valeur à tester est -out of range-)
        
        Si toutes ces conditions sont respectées, la colonne est libre; on renvoit True.
        Sinon, on renvoit False.
    """
    
    maxColonne = len(tab[0])-1
    # -1 car Par exemple Si on a 8 colonnes, len(tab) = 8, mais la ligne maximale à l'indice 7 (car la première ligne a l'indice 0)
    
    if colonne > maxColonne or colonne < 0:
        
        return False
    
    else:
        
        topOfTheColumn = tab[0][colonne]
        # On prend le tableau le plus haut de la grille, celui qui a l'indice le plus petit
    
        if topOfTheColumn != 0:
        
            return False
    
        else :
        
            return True
  

def place_jeton (tab, colonne, joueur):
  
    """
        Cette fonction place un jeton 1 ou 2 dans la colonne demandée, et dans la ligne innocupée ayant le plus grand indice ( donc étant le plu bas posisble visuellement)
        
        Pour chaque ligne du tableau, la boucle for teste si dans cette ligne, à l'emplacement de la colonne, la valeur est égale à 0:
        - si non, la boucle continue avec la ligne d'au dessus visuellement.
        - si oui, la fonction modifie ce 0 en le remplaçant par la valeur du joueur, puis renvoit le tableau.
        
        On écrit [-(line+1)], pour commencer par les lignes qui apparaîtront les plus basses, sinon le tableau se lirait en commençant par le haut, et on aurait une gravité inversée.
    """
    
    numberOfLines = len(tab)
    
    for line in range (numberOfLines):
        
        placeToTest = tab[-(line+1)][colonne]
        # - car on commence à vérifier le bas du tableau, on doit donc mettre un indice négatif
        # (line + 1) car quand on prend un indice négatif, on commence par -1, si on ajoute pas 1, on a alors 0 au début (donc la colonne la plus haute), et on ne prend pas en compte la colonne d'indice -8 (on s'arrête à -7)
        
        if placeToTest == 0:
                
            tab[-(line+1)][colonne] = joueur
            return tab



def horizontale (tab, joueur, numberToAlign):
    
    """
        Cette fonction vérifie si le nombre de pions définis au départ par l'utilisateur sont alignés horizontalement.
        Pour chaque ligne, on vérifie tous les emplacements à vérifier définis dans numberOfPlacesToTest.
        
        On retire numberToAlign à NumberOfPlacesToTest pour éviter de créer une erreur.
        Par exemple, si l'on doit aligner 4 pions, et qu'on est à la 7e colonne sur 8, le programme tentera de vérifier les valeurs des 3 emplacements suivants 7. Or l'emplacement 9 et 10 n'existent pas. On aura donc une erreur.
        
        On ajoute 1 à la variable car l'emplacement qu'on teste doit forcément avoir la valeur de joueur.
        Par exemple, si on n'avait pas mis le +1: on choisit 4 pions, le programme détecterait que l'on a gagné seulement si on avait aligné 5 pions et non 4.
        
        Si l'emplacement testé est égal à joueur, la boucle while vérifie que tous les nombre d'emplacement suivant définis dans numberToAlign (incluant l'emplacement testé lui-même) valent joueur.
        Si c'est le cas, succesToAlign sera égal à numberToAlign, et la fonction renverra True.
        Sinon, numberAligned et SuccessToAlign repasseront à 1 pour ne pas perturber la suite du programme, et la boucle for recommencera avec une autre valeur.
        
    """
    
    numberAligned = 1
    successToAlign = 1
    numberOfLines = len(tab)
    numberOfPlacesToTest = len(tab[0]) - numberToAlign + 1
    # - numberToAlign car si on ne fait pas ça, Thonny vérifiera des valeurs out of range et affichera une erreur
    # + 1 car si on ne fait pas ça, Thonny ne vériefiera pas le dernier emplacement horizontal
    
    for line in range (numberOfLines):
        
        for place in range (numberOfPlacesToTest):
            
            if tab[line][place] == joueur:
             
                while numberAligned != numberToAlign:
                    
                # Système de compteur: par exemple, si on veut aligner 4 pions, la boucle compte dans les 4 emplacements suivants, le nombre de valeurs de joueur. S'il y en a 3 (celle de départ et les trois comptées), alors le joueur a gagné.
                    
                    if tab[line][place + numberAligned] == joueur:
                        
                        successToAlign = successToAlign + 1
                    
                    numberAligned = numberAligned + 1
                    
                if successToAlign == numberToAlign:
                    
                    return True
                
                numberAligned = 1
                successToAlign = 1


def verticale (tab, joueur, numberToAlign):
    
    """
        Cette fonction vérifie si le nombre de pions définis au départ par l'utilisateur sont alignés verticalement.
        Pour chaque ligne, on vérifie tous les emplacements à vérifier définis dans numberOfPlacesToTest.
        
        On retire numberToAlign à NumberOfPlacesLinesTest pour éviter de créer une erreur.
        Par exemple, si l'on doit aligner 4 pions, et qu'on est à la 7e ligne sur 8 (en partant du bas), le programme tentera de vérifier les valeurs des 3 lignes au dessus de 7. Or les lignes au dessus de la 8e n'existent pas. On aura donc une erreur.
        
        On ajoute 1 à la variable car l'emplacement qu'on teste doit forcément avoir la valeur de joueur.
        Par exemple, si on n'avait pas mis le +1: on choisit 4 pions, le programme détecterait que l'on a gagné seulement si on avait aligné 5 pions et non 4.
        
        Si l'emplacement testé est égal à joueur, la boucle while vérifie que tous les nombre d'emplacement suivant verticalement définis dans numberToAlign (incluant l'emplacement testé lui-même) valent joueur.
        Si c'est le cas, succesToAlign sera égal à numberToAlign, et la fonction renverra True.
        Sinon, numberAligned et SuccessToAlign repasseront à 1 pour ne pas perturber la suite du programme, et la boucle for recommencera avec une autre valeur.
        
    """
    
    numberAligned = 1
    successToAlign = 1    
    numberOfLinesToTest = len(tab) - numberToAlign +1
    
    # - numberToAlign car si on ne fait pas ça, Thonny vérifiera des valeurs out of range et affichera une erreur
    # + 1 car si on ne fait pas ça, Thonny ne vériefiera pas le dernier emplacement vertical
    
    numberOfPlacesToTest = len(tab[0])
    
    for line in range (numberOfLinesToTest):
        
        for place in range ( numberOfPlacesToTest ):
            
            if tab[line][place] == joueur:
                
                while numberAligned != numberToAlign:
                    
                    # Système de compteur: par exemple, si on veut aligner 4 pions, la boucle compte dans les 4 emplacements suivants, le nombre de valeurs de joueur. S'il y en a 3 (celle de départ et les trois comptées), alors le joueur a gagné.
                    
                    if tab[line + numberAligned][place] == joueur:
                        
                        successToAlign = successToAlign + 1
                    
                    numberAligned = numberAligned + 1
                    
                if successToAlign == numberToAlign:
                    
                    return True
                
                numberAligned = 1
                successToAlign = 1
 
            
            

def diagonale (tab, joueur, numberToAlign):
    
    """
        Cette fonction vérifie si le nombre de pions définis au départ par l'utilisateur sont alignés diagonalement.
        Pour chaque ligne, on vérifie tous les emplacements à vérifier définis dans numberOfPlacesToTest.
        
        On retire numberToAlign à NumberOfPlacesLinesTest pour éviter de créer une erreur.
        Par exemple, si l'on doit aligner 4 pions, et qu'on est à la 7e ligne sur 8 (en partant du bas), le programme tentera de vérifier les valeurs des 3 lignes au dessus de 7. Or les lignes au dessus de la 8e n'existent pas. On aura donc une erreur.
        
        On retire numberToAlign à NumberOfPlacesToTest pour éviter de créer une erreur.
        Par exemple, si l'on doit aligner 4 pions, et qu'on est à la 7e colonne sur 8, le programme tentera de vérifier les valeurs des 3 emplacements suivants 7. Or l'emplacement 9 et 10 n'existent pas. On aura donc une erreur.
        
        On ajoute 1 à la variable car l'emplacement qu'on teste doit forcément avoir la valeur de joueur.
        Par exemple, si on n'avait pas mis le +1: on choisit 4 pions, le programme détecterait que l'on a gagné seulement si on avait aligné 5 pions et non 4.
        
        Si l'emplacement testé est égal à joueur, les 2 boucles while vérifient que tous les nombre d'emplacement suivant diagonalement définis dans numberToAlign (incluant l'emplacement testé lui-même) valent joueur.
        Une boucle sert à vérifier les diagonales parant du côté droit, et l'autre celles partant du côté gauche de l'emplacement détecté.
        Si c'est le cas, succesToAlign sera égal à numberToAlign, et la fonction renverra True.
        Sinon, numberAligned et SuccessToAlign repasseront à 1 pour ne pas perturber la suite du programme, et la boucle for recommencera avec une autre valeur.
        
    """
    
    numberAligned = 1
    successToAlign = 1
    
    numberOfLinesToTest = len(tab) - numberToAlign + 1
    # - numberToAlign car si on ne fait pas ça, Thonny vérifiera des valeurs out of range et affichera une erreur
    # + 1 car si on ne fait pas ça, Thonny ne vérifiera pas le dernier emplacement vertical
    
    numberOfPlacesToTest = len(tab[0]) - numberToAlign + 1
    # - numberToAlign car si on ne fait pas ça, Thonny vérifiera des valeurs out of range et affichera une erreur
    # + 1 car si on ne fait pas ça, Thonny ne vériefiera pas le dernier emplacement horizontal
    
    for line in range ( numberOfLinesToTest ):

        for place in range ( numberOfPlacesToTest ):
                               
        # On parcourt la grile dans le sens
        # +
        #   +
        #     +
        #       +
                
            if tab[line][place] == joueur:
                
                while numberAligned != numberToAlign:
                    
                    if tab[line + numberAligned][place + numberAligned] == joueur:
                        
                        successToAlign = successToAlign + 1
                    
                    numberAligned = numberAligned + 1
          
                if successToAlign == numberToAlign:
                    
                    return True
                
                numberAligned = 1
                successToAlign = 1
                
        
        # On parcourt la grile dans le sens
        #       +
        #     +
        #   +
        # +
        
            if tab[-(line + 1)][place] == joueur:
                
            # - car on commence à vérifier le bas du tableau, on doit donc mettre un indice négatif
            # (line + 1) car quand on prend un indice négatif, on commence par -1, si on ajoute pas 1, on a alors 0 au début (donc la colonne la plus haute), et on ne prend pas en compte la colonne d'indice -8 (on s'arrête à -7)
                
                while numberAligned != numberToAlign:
                    
                    if tab[-(line + 1 + numberAligned)][place + numberAligned] == joueur:
                        
                        successToAlign = successToAlign + 1
                    
                    numberAligned = numberAligned + 1
                    
                if successToAlign == numberToAlign:
                    
                    return True
                
                numberAligned = 1
                successToAlign = 1
                     
            
    
def gagne (tab, joueur, numberToSuccess):
    
    """
        Cette fonction vérifie si un joueur a gagné.
        
        Pour cela elle appelle les fonctions horizontale, verticale, et diagonale, pour vérifier si le nombre de pion défini est aligné.
        Si c'est le cas, elle affiche un message de félicitation et retourne True.
    """
    isWonHorizontale = horizontale (tab, joueur, numberToSuccess)
    isWonVerticale = verticale (tab, joueur, numberToSuccess)
    isWonDiagonale = diagonale (tab, joueur, numberToSuccess)
    
    if isWonHorizontale == True or isWonVerticale == True or isWonDiagonale == True:
        
        return True
        

def egalite (tab):
    
    """
        Cette fonction vérifie s'il y a égalité.
        
        S'il y a égalité, c'est que toute la grille est remplie. Si toute la grille est remplie, alors le haut des colonnes (alors l'entiéreté du premier tableau de notre tableau) vaut 0.
        
        Par défaut, equality = True.
        La boucle for vérifie la valeur de chaque haut de colonne. Si un haut de colonne vaut 0, alors equality passe à False.
        
        La fonction renvoie equality.
    """
    
    equality = True
    topOfColumns = len(tab[0])
    
    for place in range (topOfColumns):
        
        if tab[0][place] == 0:
                
            equality = False
    
    return equality
    
    

def tour_joueur (tab, joueur):
    
    """
        Cette fonction permet au jouer de placer un jeton.
        
        Elle lui demande la colonne où il veut placer le pion. Puisqu'on ne peut pas mettre plusieurs arguments à un input, on fait un print de la question sans retour à la ligne, puis on appelle l'input, on donne ainsi l'illusion d'un input classique.
        Si l'input est convertissable en int (elle ne contient que des nombres, ce qui est vérifié par la fonction isDigit()), alors on appelle la fonction colonne_libre pour vérifier si la colonne est disponible.
        Si elle est déclarée comme libre par la fonction colonne_libre, alors la fonction place_jeton est appelée pour placer le jeton.
        Sinon, la fonction se ré-appelle pour permettre au joueur de choisir une autre colonne.
        SI l'input demandé n'est constitué que de nombres, alors 
    """
    print("Bonjour jeune entrepeneur", joueur,", dans quelle case souhaitez-vous placer votre signe (de gang) ?", end="")
    
    colonne = input()
    
    if colonne.isdigit() == True:
        
        columnsVerification = colonne_libre(tab, int(colonne) - 1)
        
    else:
        
        print("Mais, frérot... Tu es cringe... Il faut un nombre entier...")
        return tour_joueur(tab, joueur)
    
    
    if columnsVerification == True:
        
        return place_jeton(tab, int(colonne) - 1, joueur)
    # -1 car les joueurs comptent à partir de 1 mais la machine à partir de 0 ( sauf si le joueur en question fait NSI peut être...)
    
        
    else:
    
        print("Cette colonne est déjà pleine ou inexistante, choisissez-en une nouvelle.\nReinitialisation du tour.")
        return tour_joueur(tab, joueur)
        
    

def jouer ():
    
    """
        Cette fonction permet de jouer.
        
        La boucle while s'effectuera à l'infini tant que la boucle n'est pas cassée (elle a une vérité inchangeable en condition).
        A chaque relecture de la boucle, le joueur change, puis la fonctione appelle tour_joueur pour permettre au joueur de jouer, et affichage_grille, pour lui permettre de visualiser le jeu.
        Avec les fonctions gagne et egalite, elle vérifie s'il y a egalite, ou si un joueur a gagné.
        Si c'est le cas, la fonction affiche un message, puis brise la boucle.
    """
    
    joueurToPlay = 2
    
    
    numberToWin = input("Combien de jetons faut-il aligner pour gagner :o ?\nPour insérer les paramètres par défaut, entrez Def.")
    tabToShow = grille_init(numberToWin)
    affichage_grille (tabToShow)
    
    if numberToWin == "Def":
        
        numberToWin = int(4)
        
    else:
        
        numberToWin = int(numberToWin)
        
        
    while 1 == 1:
        
        if joueurToPlay == 1:
            
            joueurToPlay = 2
            
        else:
            
            joueurToPlay = 1
            
        tabToShow = tour_joueur(tabToShow, joueurToPlay)
        affichage_grille (tabToShow)
        isWon = gagne(tabToShow, joueurToPlay, numberToWin)
        isEqual = egalite(tabToShow)
        
        if isEqual == True:
   
            print("Egalite, vous êtes tous les 2 aussi pas doués que l autre :)")
            break

        elif isWon == True:
            
            print("GG jeune entrepreneur", joueurToPlay,"tu l'as explosé :o !!!")
            break
            
jouer()