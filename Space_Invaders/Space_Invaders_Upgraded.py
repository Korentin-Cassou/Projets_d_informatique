import pyxel
import random

widthEntireScreen = 350
heightEntireScreen = 250

# Dimension de la fen�tre
widthScreen = [widthEntireScreen - (5/6) * widthEntireScreen, widthEntireScreen - (1/6) * widthEntireScreen]
heightScreen = heightEntireScreen
widthLenght = widthScreen[1] - widthScreen[0]

#----Cr�ation de la fen�tre
pyxel.init(widthEntireScreen, heightEntireScreen, "Space Invaders Upgraded - By Koko")
pyxel.load("TestVi.pyxres")



# Caract�ristiques du vaisseau
x_vaisseau = widthScreen[0] + widthLenght / 2
y_vaisseau = 9 * heightScreen / 10
infoVaisseau = (71, 0, 19, 18)
vSpeed = 3
isTouched = 0
animMove = 0
animMoveCooldown = 0
borderUp = heightScreen / 20
borderDown = 19 * heightScreen / 20

# Caract�ristiques des ennemies
ennemiSkin = [(17, 0, 11,15), (17, 16, 11,15) ,(17, 32, 11, 15)]
ennemiSkin2 = [(18, 48, 12,15), (18, 64, 12,15) ,(18, 80, 12, 15)]
ennemiSkin3 = [(34, 48, 12, 8), (34, 64, 12, 8) ,(34, 80, 12, 8)]
tabEnnemies = []
size_ennemyX = ennemiSkin[0][2]
decalEnnemyX = size_ennemyX / 2
size_ennemyY = ennemiSkin[0][3]
decalEnnemyY = size_ennemyY / 2
rightEnnemy = (0,0)
leftEnnemy = (0,0)
downEnnemy = (0,0)
marge = 10

# Variable qui passera � 0 lors du premier frame. Elle sert � effectuer toutes les configurations initiales
init = 2

# Caract�ristiques du groupe d'ennemis
maxEnnemies = 10
maxLines = 8
originalEnnemyPerLine = 4
originalNumberOfLine = 2
ennemyPerLine = originalEnnemyPerLine
numberOfLine = originalNumberOfLine

# Caract�ristique de la vitesse des ennemis
moveSpeedNexus = 60
moveSpeedOrigine = moveSpeedNexus
moveSpeedOriginal = moveSpeedOrigine
moveSpeed = 0

# Variables utiles dans le d�placement horizontal
waitOrigineH = 20
waitOriginalH = waitOrigineH
waitH = 0
countH = 0
sensH = 1

# Variables utiles dans le d�placement vertical
waitV = 0
waitOriginalV = 3
countV = 0
doingVertical = 0
canDoVertical = 0


# Variables relatives aux missiles
shotSkinAlly = [(32, 0, 6, 15), (32, 16, 6, 15), (32, 32, 6, 15)]
shotSkinEnnemy = [(48, 0, 6, 16), (48, 16, 6, 16), (48, 32, 6, 16)]
tabShot= []
infoShot = (32, 0, 16, 16)
shotCelerity = 3
waitShot = 15
waitShotEnnemy = 0
timeShotEnnemyOriginal = 100
timeShotEnnemy = timeShotEnnemyOriginal

# Variables relatives aux vies
actualLife = 5
waitHeartAnim = 0
chronoHeartAnim = 20
heartToShow = 1
maxLives = 8

# Variables relatives au score
actualScore = 0

# Variables relatives aux niveaux
currentLevel = 1
waitChangeLevel = 0
numberOfLetterDone = 0
timeBtwLetter = 10
columnOrLines = 0

# Variables relatives aux boutons
imgButton = 1
buttonNormal = (0, 0, 40, 16)
buttonTouched = (0, 16, 40, 16)
buttonCant = (0, 32, 40, 16)
buttonCooldown = 0

bigButtonNormal = [0, 48, 40, 32]
bigButtonTouched = [0, 112, 40, 32]
bigButtonWrong = [0, 80, 40, 32]
notEnoughTimer = 0

tabButtonGame = []
winButton = [marge + bigButtonNormal[2] / 2, heightEntireScreen - 10 - bigButtonNormal[3] / 2, 0]
bigShot = False
activatePortalBonus = False
portalPlaced = 0

portalSkin = [[128, 0, 12, 15], [128, 16, 12, 15], [128, 32, 12, 15]]
portalToShow = 0
tabPortal = []
chronoAnimPortal = 15
waitAnimPortal = 0
cooldownChoosePortal = 0
teleportationCooldown = 0

isWon = False

# Variables relatives au background
tabStar = []
spawnStarOriginal = 3
spawnStar = 0
spawnStarMenu = 0

# Variables relatives aux explosions
imgExplosion = 1
explosion = [64, 0, 16, 16]

# Variables relatives au Game Over

isGameOver = 0

# Variables relatives aux anims

vaisseauFire1 = [(64,24,5,7), (64,40,5,7), (64,56,5,7)]
vaisseauFire2 = [(80,24,1,7), (80,40,1,7), (80,56,1,7)]
fireToShow = 1
fireToShow = 1
waitFire = 0
chronoAnimFire = 10

ennemiToShow = 1
waitEnnemiAnim = 0
chronoEnnemiAnim = 15

waitAnimShot = 0
allyShotToShow = 1
ennemyShotToShow = 1
chronoAnimShot = 7


# Variables relatives aux astéroids / ovnis

tabAsteroid = []
spawnAsteroidOrigine = 250
spawnAsteroidOriginal = spawnAsteroidOrigine
waitAsteroid = 0
tabOvni = []
ovniInfos = [152, 4, 16, 10]
ovniCircles = [[157, 17, 7, 3], [155, 21, 10, 3], [153, 26, 14, 3]]
waitOvni = 0
chronoAnimCircles = 10
circleToShow = 0

# D�finition des bordures de la scène; ni les ennemies, ni le joeur ne pourront les franchir
margeBorder = 20
rightBorder = widthEntireScreen - margeBorder - bigButtonNormal[2]
leftBorder = margeBorder + bigButtonNormal[2] 

soundWinDone = False
soundOverDone = False


def update():
    """
       Mise à jour des positions et des états.
       La première fonction qui gère toutes les autres.
       Plus spécifiuement, elle gère les différentes rooms
    """
    
    global waitChangeLevel
    global init

    gameValue = 0
    changeValue = 1
    welcomeValue = 2
    gameOverValue = 3
    gameOverTransitValue = 4
    tutorialValue = 5
    winTransitValue = 6
    winValue = 7
    

    # Selon l'état de init, on affiche la partie du jeu correspondante (accueil, jeu, changement de niveaux...)
    if init == welcomeValue:
        
        welcomeMenu()
    

    if init == changeValue :
        
        # Compteur pour effectuer le changement de niveau, le temps d'afficher une lettre.
        waitChangeLevel = waitChangeLevel + 1
        
        # Si ça fait waitChangeLevel unités de temps, une lettre s'affiche.
        if waitChangeLevel % timeBtwLetter == 0 :
            
            changeLevel()
        
        

    if init == gameValue:
        
        game()



    if init == gameOverValue:

        gameOverMenu()



    if init == gameOverTransitValue :
        
        # Compteur pour effectuer le changement de niveau, le temps d'afficher une lettre.
        waitChangeLevel = waitChangeLevel + 1
        
        # Si ça fait waitChangeLevel unités de temps, une lettre s'affiche.
        if waitChangeLevel % timeBtwLetter == 0 :
            
            changeLevel("Game Over")



    if init == winValue:

        gameOverMenu(True)



    if init == winTransitValue :
        
        # Compteur pour effectuer le changement de niveau, le temps d'afficher une lettre.
        waitChangeLevel = waitChangeLevel + 1
        
        # Si ça fait waitChangeLevel unités de temps, une lettre s'affiche.
        if waitChangeLevel % timeBtwLetter == 0 :
            
            changeLevel("Congratulations")


    if init == tutorialValue:

        tutorial()



def initGame():
    """
        Fonction qui crée les boutons et les ennemis du niveau.
    """
    
    global tabEnnemies
    margeEnemy = 2

    # On crée les boutons ici
    createGameButton()

    # Définition des coordonnées de l'ennemi en haut à gauche (le premier).
    topEnnemy = (leftBorder + decalEnnemyX + margeEnemy, heightScreen / 6)
        
    # Selon le nombre souhaité de lignes d'ennemies et de nombre d'ennemies, ces deux boucles vont créer un tableau contenant les
    # coordonnées de chaque ennemi, ainsi que son état: 1 - en vie, 0 - mort, autre - en état d'explosion.
    for i in range (numberOfLine):
        
        tabToAdd= []
            
        for k in range (ennemyPerLine):
            
            
            # Exemple: On souhaite afficher les coordonnees du 3e ennemi
            # On ajoute aux coordonn�es du premier ennemi, la taille des 2 ennemis ainsi que les 2 marges, déjà affichée.
            # On obtient alors les coordonnées souhaitées pour cet ennemi.
            x = topEnnemy[0] + k * marge + k * size_ennemyX
            y = topEnnemy[1] + i * marge + i * size_ennemyX
            tabToAdd.append((x, y, 1))
                
        tabEnnemies.append(tabToAdd)  



def game():  
    """
        Cette fonction gère tout ce qui se passe dans le jeu "pur", c'est à dire quand le joueur peut agir sur le vaisseau et s'amuser.
    """
    # On déclare les variables globales que l'on souhaitera modifier par la suite
    
    global init
    
    global moveSpeed
    
    global tabShot
    global waitShot
    global waitShotEnnemy
    global sensH

    global spawnStar

    global waitAsteroid
    global waitOvni
    
    timeBetweenAllyShoot = 15

    # A chaque frame, on commence par clear l'écran pour éviter les bugs d'affichage.
    # On affiche également la souris pour l'achat de bonus.
    pyxel.cls(0)
    pyxel.mouse(True)
    
    # Configuration initiales
    if init == 1:

        init = 0
        initGame()

        sensH = 1

        # moveSpeed est le délais de déplacement des ennemies. Quand celui-ci atteint 0, les ennemies effectuent un mouvement.
        moveSpeed = moveSpeed - 1
    

    # Si le joueur n'a pas perdu
    if isGameOver == 0:

        vaisseauManager() 

        # moveSpeed est le d�lais de d�placement des ennemies. Quand celui-ci atteint 0, les ennemies effectuent un mouvement.
        moveSpeed = moveSpeed - 1

        # On effectue les mouvements des ennemis
        horizontalManager()
        verticalManager()
        
        # Ceci sont les compteurs de tirs, alliés et ennemis.
        # Quand ils atteignent une certaine valeur, le joueur peut tirer / les ennemis tirent.
        waitShot = waitShot + 1 
        waitShotEnnemy = waitShotEnnemy + 1
    
        # Si la touche espace est touchée et qu'aucun missile allié n'a été crée pendant les 20 dernières frames, on crée un missile.
        if pyxel.btnp(pyxel.KEY_SPACE, 20, 1) and waitShot >= timeBetweenAllyShoot:
            
            # On réinitialise le timer
            waitShot = 0
            tabShot.append((int(x_vaisseau), int(y_vaisseau), 1, 1))
            
            
        # Si le temps timeShotEnnemy est passé, alors un ennemi tire un missile.
        if waitShotEnnemy >= timeShotEnnemy:
        
            waitShotEnnemy = 0
            chooseEnnemyToShot()
    
        # On effectue les mouvements des tirs.
        shotMove()

        # On vérifie si le vaisseau ne touche pas une ennemi.
        deathByEnnemy()

        # Compteur de création d'une étoile
        spawnStar = spawnStar + 1

        # Si le compteur attend le temps recherché, on le réinitialise, et on crée une étoile.
        if spawnStar == spawnStarOriginal:

            spawnStar = 0
            backgroundAdd()

        # Compteur de création d'un astéroid
        waitAsteroid = waitAsteroid + 1

        # Si le compteur attend le temps recherché, on crée un astéroid.
        if waitAsteroid % spawnAsteroidOriginal == 0:

            asteroidAdd()


        # Compteur de création d'un ovni
        waitOvni = waitOvni + 1

        # Si le compteur attend le temps recherché, et on crée un ovni.
        if waitOvni % 400 == 0:

            ovniAdd()


        # On fait bouger les différents éléments du jeu 
        backgroundMove()
        ovniMove()
        asteroidMove()

        # On affiche les vies et les boutons
        liveVaisseau(0)
        gameButton()
        winButtonFonction()

    # On fonction du pourcentage d'ennemis encore en vie, on accélère légèrement le mouvement des ennemis.
    columnChanges()
    
    # On affiche les ennemies, tirs, et le vaisseau, et le score.
    affiche_ennemies()
    affiche_shoot()
    affiche_vaisseau()
    score(0)

    gameButton()
    winButtonFonction()

    #pyxel.blt(x_vaisseau - infoVaisseau[2] / 2, y_vaisseau, 0, 168, 0, 1, 1, 0)
    #pyxel.blt(x_vaisseau + infoVaisseau[2] / 2, y_vaisseau, 0, 169, 0, 1, 1, 0)
    #pyxel.blt(x_vaisseau, y_vaisseau - infoVaisseau[3] / 2, 0, 170, 0, 1, 1, 0)
    #pyxel.blt(x_vaisseau, y_vaisseau + infoVaisseau[3] / 2, 0, 171, 0, 1, 1, 0)
    #pyxel.blt(x_vaisseau, y_vaisseau, 0, 172, 0, 1, 1, 0)

    # Si le bonus portail est acheté, on l'active.
    if activatePortalBonus == True:

        portalBonus()
   
    # Cette fonction vérifie si tous les ennemis sont en vie, donc si on a besoin de changer de niveau.
    needToChangeThelevel()

    # Cette fonction vérifie si le joueur a perdu ou gagné.
    gameOver( isWon )
     
    

def welcomeMenu():
    """
        Fonction qui gère le menu d'accueil
    """
    
    global buttonCooldown
    global spawnStarMenu

    # Variables relatives au logo
    logoInfos = (0, 0, 4 * 16, 3 * 16)
    spaceX = 15
    spaceY = 5
    ennemyExposition = (1, 0, 11,15)

    buttonCooldown = buttonCooldown - 1
    
    # Ces variables sont de simples infos de placement des boutons et des textes.
    pyxel.cls(0)
    pyxel.mouse(True)
    
    x_button = 1/2 * widthEntireScreen
    y_button = 1.75/3 * heightEntireScreen      
    decalBtwButton = 8
    
    xLogo = 1/2 * widthEntireScreen
    yLogo = 1/3.5 * heightEntireScreen


    # On met en place le background, comme dans la fonction game.
    spawnStarMenu = spawnStarMenu + 1

    if spawnStarMenu % 5 == 0:

        backgroundAdd(heightEntireScreen)

        
    backgroundMove(-1)
    
    # On stocke les infos des différents boutons du menu dans un tableau
    tabWelcomeButton = [(x_button, y_button, buttonNormal[2] / 2, buttonNormal[3] / 2, 0), (x_button, y_button + 2 * buttonNormal[3] / 2 + decalBtwButton, buttonNormal[2] / 2, buttonNormal[3] / 2, 1)]
    
    adjust = 1

    # On fait appel à la fonction centerText pour centrer le texte et obtenir ses positions de d�part.
    xPlay = centerText(tabWelcomeButton[0][0] + adjust, tabWelcomeButton[0][1], "Play")[0]
    yPlay = centerText(tabWelcomeButton[0][0], tabWelcomeButton[0][1], "Play")[1]
    xTutorial = centerText(tabWelcomeButton[1][0] + adjust, tabWelcomeButton[1][1], "Rules")[0]
    yTutorial = centerText(tabWelcomeButton[1][0], tabWelcomeButton[1][1], "Rules")[1]
       


    textLogo1 = "Space Invaders"
    textLogo2 = "Upgraded"

    coordTextLogo1 = centerText(xLogo, yLogo - logoInfos[3] / 2, textLogo1)
    coordTextLogo2 = centerText(xLogo, yLogo + logoInfos[3] / 2, textLogo2)
    
    coordVaisseau = [xLogo - infoVaisseau[2] / 2, yLogo - infoVaisseau[3] / 2]
    coordEnnemy1 = [xLogo - spaceX - infoVaisseau[2] / 2 - size_ennemyX / 2, yLogo - size_ennemyY / 2 + spaceY]
    coordEnnemy2 = [xLogo + spaceX + infoVaisseau[2] / 2 - size_ennemyX / 2, yLogo - size_ennemyY / 2 + spaceY]
    
    # On affiche chaque bouton grâce à cette boucle
    for i in range (len(tabWelcomeButton)):
        
        welcomeButtonActions(tabWelcomeButton[i])
        
        if welcomeButtonActions(tabWelcomeButton[i]) == "Stop":
            
            break
      
      
    # On affiche le texte

    pyxel.text(xPlay, yPlay, "Play", 7)
    pyxel.text(xTutorial, yTutorial, "Rules", 7)

    pyxel.text(10, 10, "Made by Koko", 5)
    pyxel.text(10, 20, "Thank you for playing !", 5)

    pyxel.text(coordTextLogo1[0],coordTextLogo1[1], textLogo1, 7)
    pyxel.text(coordTextLogo2[0], coordTextLogo2[1], textLogo2, 7)

    pyxel.blt(coordVaisseau[0], coordVaisseau[1], 0, infoVaisseau[0], infoVaisseau[1], infoVaisseau[2], infoVaisseau[3], 0)
    pyxel.blt(coordEnnemy1[0], coordEnnemy1[1], 0, ennemyExposition[0], ennemyExposition[1], ennemyExposition[2], ennemyExposition[3], 0)
    pyxel.blt(coordEnnemy2[0], coordEnnemy2[1], 0, ennemyExposition[0], ennemyExposition[1], ennemyExposition[2], ennemyExposition[3], 0)

    # Si le bouton Play a été touché, on change de scène, donc on efface tout ce qu'on a affich�.
    if init != 2:
        
        pyxel.cls(0)



def needToChangeThelevel():
    """
        Fonction qui vérifie si on a besoin de changer de niveau
    """
    global currentLevel
    global init
    global tabEnnemies
    global tabShot
    
    # On met needToChangeLevel à True par défaut.
    # Si après vérification, on voit qu'un ennemi est en vie, on le passe à False.
    needToChangeLevel = True
    
    for k in range (numberOfLine):
        
        for w in range (ennemyPerLine):
            
            if tabEnnemies[k][w][2] != 0:
                
                needToChangeLevel = False
                
                
    # S il faut changer de niveaux, on change de niveaux
    if needToChangeLevel:
        
        currentLevel = currentLevel + 1
        init = 1
        
        # On nettoie l'écran et on clear les missiles (et ennemis, juste par sécurité).
        pyxel.cls(0)
        pyxel.mouse(False)
        tabEnnemies = []
        tabShot = []
        
    

def changeLevel(typeOfChange = "Level"):
    """
         Cette fonction intervient à chaque changement de niveau, pour annoncer le niveau suivant, et augmenter la difficult�.
    """
    
    global currentLevel
    global waitChangeLevel
    global numberOfLetterDone
    global ennemyPerLine 
    global numberOfLine 
    global moveSpeedOriginal
    global timeShotEnnemy

    global countH
    global waitH
    global moveSpeed
    global canDoVertical
    global waitV 
    global countV 
    global doingVertical 
    global moveSpeedOrigine
    global waitOriginalH

    global x_vaisseau
    global y_vaisseau

    global tabAsteroid
    global waitAsteroid
    global tabOvni
    global waitOvni

    global init
    global tabButtonGame
    global bigShot

    global waitAnimPortal
    global portalToShow
    global cooldownChoosePortal
    global teleportationCooldown
    global activatePortalBonus
    global tabPortal
    global spawnAsteroidOriginal

    global columnOrLines

    margeLetter = 5
    pyxel.mouse(False)

    # On affiche un texte différent selon le type de changement de scène

    if typeOfChange == "Level":

        textToShow = "Level " + str(currentLevel)


    else :

        textToShow = str(typeOfChange)

    
    # On fait appel à la fonction centerText pour obtenir la valeur à prendre comme commen�ant du texte.
    xStart = centerText(1/2 * widthEntireScreen, 1/2 * heightEntireScreen, textToShow, margeLetter)[0]
    yStart = centerText(1/2 * widthEntireScreen, 1/2 * heightEntireScreen, textToShow, margeLetter)[1]
    
    # Les couleurs du texte sont générées aléatoirement.
    colorToText = random.randint(1, 15)
    
    # Si toutes les lettres n'ont pas encore été écrites, on affiche la lettre suivante au bon emplacement.
    if numberOfLetterDone + 1 <= len(textToShow):
        
        pyxel.text(xStart + margeLetter * numberOfLetterDone, yStart, textToShow[numberOfLetterDone], colorToText)
    
    
    # Si toutes les lettres ont été �crite et qu'un temps assez long est passé (pour que l'utilisateur puisse lire le niveau), on augmente la difficult�, et on réinitialise les
    # paramètres nécessaires. Puis on commence le jeu.
    if numberOfLetterDone + 1 > len(textToShow) and waitChangeLevel > timeBtwLetter * len(textToShow) + timeBtwLetter:
        
        if columnOrLines % 2 == 0:

            ennemyPerLine = ennemyPerLine + 1

        else:
            
            numberOfLine = numberOfLine + 1

        columnOrLines = columnOrLines + 1


        if ennemyPerLine > maxEnnemies:

            ennemyPerLine = maxEnnemies


        if numberOfLine > maxLines:

            numberOfLine = maxLines

        countH = 0
        moveSpeed = moveSpeedOriginal
        waitH = 0
        canDoVertical = 0
        doingVertical = 0
        countV = 0

        waitV = 0

        moveSpeedOrigine = moveSpeedOrigine - 5
        timeShotEnnemy = timeShotEnnemy - 5
        waitOriginalH = waitOriginalH - 1
        spawnAsteroidOriginal = spawnAsteroidOriginal - 5

        x_vaisseau = widthScreen[0] + widthLenght / 2
        y_vaisseau = 9 * heightScreen / 10

        tabAsteroid = []
        waitAsteroid = 0

        waitAnimPortal = 0
        portalToShow = 0
        cooldownChoosePortal = 0
        teleportationCooldown = 0
        activatePortalBonus = False
        tabPortal = []

        waitOvni = 0
        tabOvni = []
        tabButtonGame = []
        bigShot = False

        if waitOriginalH <= 1:

            waitOriginalH = 2

        if moveSpeedOrigine <= 0:

            moveSpeedOrigine = 1
        
        waitChangeLevel = 0
        numberOfLetterDone = 0
        
        # Selon le type de changement de room, on va dans une room différente.
        if typeOfChange == "Level":
            
            game()


        if typeOfChange == "Game Over":

            init = 3


        if typeOfChange == "Congratulations":

            init = 7
    
    
    # Sinon, une lettre a été écrite en plus, donc on ajoute 1 à la variable correspondante.
    else:
        
        numberOfLetterDone = numberOfLetterDone + 1
    
    

def draw():
   """
        Fonction que je n'ai pas utilisé, mais que je mets quand même pour respecter la "syntaxe" du module pyxel.
   """
   1==1 



def gameOver(win = "False"):
    """
         Cette fonction g�re tout ce qui est relatif à la défaite et à la victoire.
    """

    global isGameOver
    global actualLife
    global init

    # Si le joueur n'a plus de vie ou qu'il a gagné, on enclenche l'animation de GameOver / Congratulations
    if actualLife <= 0 or win == "True":

        isGameOver = 50
        actualLife = 5

    # Mise à jour de l'animation de Game Over / Congratulations.
    if isGameOver > 1:

        isGameOver = isGameOver - 1
    
    
    # Fin de l'animation de Game Over / Congratulations
    if isGameOver == 1:

        # Changement du menu vers le menu de Game Over.
        init = 4
        pyxel.cls(0)

        # Changement du menu vers le menu de Win si il a gagné.
        if win == "True2":

            init = 6



def gameOverMenu(win = False):
    """
        Cette fonction gère tout ce qui est relatif à l'affichage du menu de Game Over / win
    """

    global soundWinDone
    global soundOverDone

    pyxel.cls(0)
    pyxel.mouse(True)

    marge = 10
    marge2 = 1
    color = 7

    # Si la fonction est appelée comme une défaite
    if win == False:

        if soundOverDone == False:

            pyxel.play(0, 9)
            soundOverDone = True
        # On affiche ici, simplement les infos sur la partie du joueur
        textToShow1 = "You loose"
        textToShow2 = "Score: " + str(actualScore)
        textToShow3 = "Level reached: " + str(currentLevel)


    # Si la fonction est appelée comme une victoire
    else : 

        # On affiche ici, simplement les infos sur la partie du joueur
        if soundWinDone == False:
            
            soundWinDone = True
            pyxel.play(1, 7)

        textToShow1 = "You Won !"
        textToShow2 = "Score: " + str(actualScore)
        textToShow3 = "Level reached: " + str(currentLevel)

    # On calcule les coordonnées des textes à afficher grâce à centerText, puis on affiche ces textes.
    coord1 = centerText(widthEntireScreen / 2, heightEntireScreen / 3, textToShow1)
    coord2 = centerText(widthEntireScreen / 2, heightEntireScreen / 2, textToShow2)
    coord3 = centerText(widthEntireScreen / 2, heightEntireScreen / 2 + marge, textToShow3)

    pyxel.text(coord1[0], coord1[1], textToShow1, color)
    pyxel.text(coord2[0], coord2[1], textToShow2, color)
    pyxel.text(coord3[0], coord3[1], textToShow3, color)

    # Et un bouton pour pouvoir rejouer en allant vers le menu.

    textMenu = "Menu"
    boutonMenu = (widthEntireScreen / 2, (heightEntireScreen / 3) * 2, buttonNormal[2] / 2, buttonNormal[3] / 2)
    coordMenu = centerText(widthEntireScreen / 2 + marge2, (heightEntireScreen / 3) * 2, textMenu)

    gameOverButtons(boutonMenu)

    pyxel.text(coordMenu[0], coordMenu[1], textMenu, color)



def tutorial():
    """
        Cette fonction affiche toutes les infos liées aux règles du jeu.
    """

    # On détermine les coordonnées des textes grâce à centerText, puis on affiche ces textes.
    adjust = 0
    margeText = 10
    startPositionY = heightEntireScreen / 6
    positionX = widthEntireScreen / 2 
    color = 7

    pyxel.cls(0)

    text1 = "This is an upgraded version of Space Invaders"


    text2 = "To move, use the left and right arrow keys"
    text3 = "To shoot, use Space"

    text4 = "If you loose all your lives, or if an enemy touches the back of your screen,"
    text5 = "you die"

    text6 = "You can buy upgrades thanks to your score points"
    text7 = "You win when you buy the upgrade Win."


    text8 = "Enjoy !"


    coord1 = centerText(positionX + adjust, startPositionY, text1)


    coord2 = centerText(positionX + adjust, startPositionY + margeText * 3, text2)
    coord3 = centerText(positionX, startPositionY + margeText * 4, text3)

    coord4 = centerText(positionX + adjust, startPositionY + margeText * 6, text4)
    coord5 = centerText(positionX, startPositionY + margeText * 7, text5)

    coord6 = centerText(positionX + adjust, startPositionY + margeText * 9, text6)
    coord7 = centerText(positionX + adjust, startPositionY + margeText * 10, text7)


    coord8 = centerText(positionX, startPositionY + margeText * 13, text8)

    pyxel.text(coord1[0], coord1[1], text1, color)
    pyxel.text(coord2[0], coord2[1], text2, color)
    pyxel.text(coord3[0], coord3[1], text3, color)
    pyxel.text(coord4[0], coord4[1], text4, color)
    pyxel.text(coord5[0], coord5[1], text5, color)
    pyxel.text(coord6[0], coord6[1], text6, color)
    pyxel.text(coord7[0], coord7[1], text7, color)
    pyxel.text(coord8[0], coord8[1], text8, color)


    buttonToShow = (positionX - 1, 5 * heightEntireScreen / 6, buttonNormal[2] / 2, buttonNormal[3] / 2)
    textMenu = "Menu"
    coordMenu = centerText(positionX, 5 * heightEntireScreen / 6, textMenu)

    tutorialButtons(buttonToShow)
    pyxel.text(coordMenu[0], coordMenu[1], textMenu, color)





#--------------------------------------------------------------------------------------------------------------------------------------#
        # Fonctions relatives au vaisseau
#--------------------------------------------------------------------------------------------------------------------------------------# 




def vaisseauManager():
    """
         Cette fonction gère les actions du vaisseau.
    """

    global x_vaisseau
    global y_vaisseau
    global waitFire
    global fireToShow
    
    
    # D�placement � droite du vaisseau
    if pyxel.btn(pyxel.KEY_RIGHT):
        
        deplace_vaisseau(vSpeed,0)
        
    # D�placement � gauche du vaisseau 
    if pyxel.btn(pyxel.KEY_LEFT):
        
        deplace_vaisseau(-vSpeed,0)

    # D�placement � droite du vaisseau
    if pyxel.btn(pyxel.KEY_UP):
        
        deplace_vaisseau(0, - vSpeed)
        
    # D�placement � gauche du vaisseau 
    if pyxel.btn(pyxel.KEY_DOWN):
        
        deplace_vaisseau(0 ,vSpeed)
        
    
    # 2 syst�mes qui permettent au vaisseau de ne pas sortir de l'�cran
    if x_vaisseau - infoVaisseau[2] / 2 < leftBorder:
        
        deplace_vaisseau(vSpeed,0)
        
        
    if x_vaisseau + infoVaisseau[2] / 2 > rightBorder:
        
        deplace_vaisseau(-vSpeed,0)


    if y_vaisseau + infoVaisseau[3] / 2 > borderDown:
        
        deplace_vaisseau(0 ,-vSpeed)


    if y_vaisseau - infoVaisseau[3] / 2 < borderUp:
        
        deplace_vaisseau(0 ,vSpeed)
        
    
    # On met en place le système d'animation des flammes du vaisseau.
    waitFire = waitFire + 1
    
    if waitFire == chronoAnimFire:
        
        waitFire = 0
        fireToShow = fireToShow + 1
        
        if fireToShow > 2:
            
            fireToShow = 0
        
    
    
def deplace_vaisseau(dx, dy):
    """
        Déplacement du vaisseau.
    """
    
    # On d�clare les variables globales pour pouvoir les modifier
    global x_vaisseau, y_vaisseau
    
    # On modifie les coordonn�es du vaisseau
    x_vaisseau = x_vaisseau + dx
    y_vaisseau = y_vaisseau + dy

     
    
def affiche_vaisseau():
    """
        Affichage du vaisseau
    """

    global isTouched
    global infoVaisseau

    infoVaisseau1 = (71, 0, 19, 18)
    infoVaisseau2 = (103, 0, 19, 18)
    infoVaisseau3 = (103, 24, 19, 18)
    
    # On détermine les coordonnées des flammes du vaisseau
    coordFire1 = (x_vaisseau  - vaisseauFire1[fireToShow][2] / 2, y_vaisseau + infoVaisseau[2] / 2 + 1)
    coordFire2_1 = (x_vaisseau - infoVaisseau[2] / 2 + 1, y_vaisseau + infoVaisseau[2] / 2 - 2)
    coordFire2_2 = (x_vaisseau + infoVaisseau[2] / 2 - 2, y_vaisseau + infoVaisseau[2] / 2 - 2)
    
    
    # Si le vaisseau n'est pas en dehors de la zone de jeu, on l'affiche.
    if x_vaisseau - infoVaisseau[2] / 2 < rightBorder and x_vaisseau - infoVaisseau[2] / 2 > leftBorder:
        
        # Si le vaisseau est touché, il a une période d'invincibilité où il clignote
        if isTouched % 16 < 8:

            # Selon la vie du vaisseau, on affiche un sprite plus ou moins endommagé.
            if actualLife >= 4:

                infoVaisseau = infoVaisseau1

            elif actualLife < 4 and actualLife >= 2:

                infoVaisseau = infoVaisseau2

            else:

                infoVaisseau = infoVaisseau3

            # On affiche vaisseau et flammes.
            pyxel.blt(x_vaisseau - infoVaisseau[2] // 2, y_vaisseau - infoVaisseau[2] // 2, 0, infoVaisseau[0], infoVaisseau[1], infoVaisseau[2], infoVaisseau[3], 0)
            pyxel.blt(coordFire1[0], coordFire1[1], 0, vaisseauFire1[fireToShow][0], vaisseauFire1[fireToShow][1], vaisseauFire1[fireToShow][2], vaisseauFire1[fireToShow][3], 0)
            pyxel.blt(coordFire2_1[0], coordFire2_1[1], 0, vaisseauFire2[fireToShow][0], vaisseauFire2[fireToShow][1], vaisseauFire2[fireToShow][2], vaisseauFire2[fireToShow][3], 0)
            pyxel.blt(coordFire2_2[0], coordFire2_2[1], 0, vaisseauFire2[fireToShow][0], vaisseauFire2[fireToShow][1], vaisseauFire2[fireToShow][2], vaisseauFire2[fireToShow][3], 0)
    
        
        # Si le vaisseau est en état d'invicibilité, on réduit le temps restant au timer d'invincibilité
        if isTouched > 0:

            isTouched = isTouched - 1

            if isTouched % 16 >= 8:

                pyxel.blt(x_vaisseau - infoVaisseau[2] // 2, y_vaisseau - infoVaisseau[2] // 2, 0, 200, 0, 1, 1)



def liveVaisseau(modif):
    """
         On gère la vie du vaisseau ici
    """
    
    global actualLife
    global waitHeartAnim
    global heartToShow
    global maxlives

    if modif != 0:

        pyxel.play(1, 5)

    waitHeartAnim = waitHeartAnim + 1
    actualLife = actualLife + modif
    
    # Le nombre maximum de vie est 8. Si le joueur gagne un coeur alors qu'il a 8 vies, il obtient en récompense 200 points de score.
    if actualLife > maxLives:
        
        actualLife = maxLives
        score(200)
    
    heartAnim = [(48, 0, 16, 16),(48, 16, 16, 16),(48, 16 + 16, 16, 16),(48, 16 + 16 * 2, 16, 16),(48, 16 + 16 * 3, 16, 16)]
    margeHeart = 5
    firstHeartPlace = [marge + bigButtonNormal[2] / 2 - heartAnim[heartToShow][2] / 2 - 1, 2 * heightScreen / 16]   
    imgHeart = 1
    
    # Animation des coeurs
    if waitHeartAnim >= chronoHeartAnim:

        waitHeartAnim = 0
        heartToShow = heartToShow + 1

        if heartToShow > len(heartAnim) - 1:

            heartToShow = 0
    
    # Affichage des coeurs en une ligne verticale
    for i in range (actualLife):
        
        pyxel.blt(firstHeartPlace[0], firstHeartPlace[1] + heartAnim[heartToShow][3] / 2 + i * heartAnim[heartToShow][3] + i * margeHeart, imgHeart, heartAnim[heartToShow][0], heartAnim[heartToShow][1], heartAnim[heartToShow][2], heartAnim[heartToShow][3], 0)             
        
                       

def score(modif):
    """
        Cette fonction met à jour le score du joueur avant de l'afficher.
    """
    
    global actualScore
    
    margeText = 10
    marge = 10
    
    actualScore = actualScore + modif
    
    # On d�termine les coordonnées du d�but du texte grâce à la fonction centerText.
    xScore = centerText(marge + bigButtonNormal[2] / 2, heightScreen / 16, "Score:")[0]
    yScore = centerText(marge + bigButtonNormal[2] / 2, heightScreen / 16, "Score:")[1]
    xActualScore = centerText(marge + bigButtonNormal[2] / 2, heightScreen / 16 + margeText, str(actualScore))[0]
    yActualScore = centerText(marge + bigButtonNormal[2] / 2, heightScreen / 16 + margeText, str(actualScore))[1]
    colorScore = 10
    
    # On affiche le score.
    pyxel.text(xScore,yScore, "Score:" , colorScore)
    pyxel.text(xActualScore, yActualScore, str(actualScore) , colorScore)

                

#--------------------------------------------------------------------------------------------------------------------------------------#
        # Fonctions relatives aux missiles
#--------------------------------------------------------------------------------------------------------------------------------------# 


def affiche_shoot():
    """
        Cette fonction permet d'afficher les missiles tirés.
    """
    
    # Pour chaque missile

    global waitAnimShot
    global allyShotToShow
    global ennemyShotToShow

    # On met à jour l'animation des tirs
    waitAnimShot = waitAnimShot + 1

    if waitAnimShot >= chronoAnimShot:

        waitAnimShot = 0
        allyShotToShow = allyShotToShow + 1
        ennemyShotToShow = ennemyShotToShow + 1

        if allyShotToShow > 2:

            allyShotToShow = 0
            ennemyShotToShow = 0


    # Pour chaque tirs
    for i in range (len(tabShot)):
        
        if tabShot[i][3] == 1:
            
            # On différence les missiles adverses et les missiles alliés.
            if tabShot[i][2] == 1:

                # On affiche son sprite aux positions donn�es s'il est en vie.
                pyxel.blt(tabShot[i][0] - shotSkinAlly[allyShotToShow][2] / 2, tabShot[i][1] - shotSkinAlly[allyShotToShow][3] / 2, 0, shotSkinAlly[allyShotToShow][0], shotSkinAlly[allyShotToShow][1], shotSkinAlly[allyShotToShow][2], shotSkinAlly[allyShotToShow][3], 0)
            
            if tabShot [i][2] == -1:
                
                # On affiche son sprite aux positions données s'il est en vie.
                pyxel.blt(tabShot[i][0] - shotSkinEnnemy[ennemyShotToShow][2] / 2, tabShot[i][1] - shotSkinEnnemy[ennemyShotToShow][3] / 2, 0, shotSkinEnnemy[ennemyShotToShow][0],shotSkinEnnemy[ennemyShotToShow][1], shotSkinEnnemy[ennemyShotToShow][2], shotSkinEnnemy[ennemyShotToShow][3], 0)

        else:

            # S il est en état d'explosion, on affiche cela.
            pyxel.blt(tabShot[i][0] - shotSkinAlly[allyShotToShow][2] / 2, tabShot[i][1] - shotSkinAlly[allyShotToShow][3] / 2, imgExplosion, explosion[0], explosion[1], explosion[2], explosion[3], 0)
    


def shotMove():
    """
        On fait avancer les missiles grâce à cette fonction.
        Si le missile rencontre un ennemi / le vaisseau, on le détruit.
    """
    
    global tabShot
    global tabEnnemies
    global isTouched
    global tabOvni
    
    for i in range (len(tabShot)):
        
        # On change les coordonn�es du missile en fonction de son sens de d�placement, et de sa vitesse.
        margeScreen = 25
        
        margeTir = 5
        xNew = tabShot[i][0]
        yNew = tabShot[i][1] - shotCelerity * tabShot[i][2]
        tabShot[i] = (xNew, yNew,tabShot[i][2], tabShot[i][3])
        
        
        # Pour chaque ennemi
        for line in range (numberOfLine):
            
            for column in range (ennemyPerLine):
                
                # Si sa hitbox touche la hitbox du missile, et que l'ennemi est en vie, et que le missile est un missile du vaisseau.
                if tabShot[i][0] <= (tabEnnemies[line][column][0] + decalEnnemyX + margeTir) and tabShot[i][0] >= (tabEnnemies[line][column][0] - decalEnnemyX - margeTir) and tabShot[i][1] >= (tabEnnemies[line][column][1] - decalEnnemyY - margeTir) and tabShot[i][1] <= (tabEnnemies[line][column][1] + decalEnnemyY + margeTir) and tabEnnemies[line][column][2] == 1 and tabShot[i][2] == 1:
                    
                    if bigShot == False:
                        
                        pyxel.play(0, 0)

                    # On ajoute des points de score au joueur
                    score(100)
                    
                    # On élimine l'ennemi, et on détruit le tir.
                    x = tabEnnemies[line][column][0]
                    y = tabEnnemies[line][column][1]
                    alive = 20
                    tabEnnemies[line][column] = (x, y, alive)

                    # Si le bonus bigShot est activé, on détruit aussi tous les ennemis à côté de celui touché, s'ils existent.
                    if bigShot == True:

                        pyxel.play(1, 8)

                        if line - 1 >= 0:

                            x = tabEnnemies[line - 1][column][0]
                            y = tabEnnemies[line - 1][column][1]
                            alive = 20
                            tabEnnemies[line - 1][column] = (x, y, alive)


                            if column - 1 >= 0:

                                x = tabEnnemies[line - 1][column - 1][0]
                                y = tabEnnemies[line - 1][column - 1][1]
                                alive = 20
                                tabEnnemies[line - 1][column - 1] = (x, y, alive)


                            if column + 1 <= ennemyPerLine - 1:

                                x = tabEnnemies[line - 1][column + 1][0]
                                y = tabEnnemies[line - 1][column + 1][1]
                                alive = 20
                                tabEnnemies[line - 1][column + 1] = (x, y, alive)



                        if line + 1 <= numberOfLine - 1:

                            x = tabEnnemies[line + 1][column][0]
                            y = tabEnnemies[line + 1][column][1]
                            alive = 20
                            tabEnnemies[line + 1][column] = (x, y, alive)


                            if column - 1 >= 0:

                                x = tabEnnemies[line + 1][column - 1][0]
                                y = tabEnnemies[line + 1][column - 1][1]
                                alive = 20
                                tabEnnemies[line + 1][column - 1] = (x, y, alive)


                            if column + 1 <= ennemyPerLine - 1:

                                x = tabEnnemies[line + 1][column + 1][0]
                                y = tabEnnemies[line + 1][column + 1][1]
                                alive = 20
                                tabEnnemies[line + 1][column + 1] = (x, y, alive)



                        if column - 1 >= 0:

                                x = tabEnnemies[line][column - 1][0]
                                y = tabEnnemies[line][column - 1][1]
                                alive = 20
                                tabEnnemies[line][column - 1] = (x, y, alive)


                        if column + 1 <= ennemyPerLine - 1:

                                x = tabEnnemies[line][column + 1][0]
                                y = tabEnnemies[line][column + 1][1]
                                alive = 20
                                tabEnnemies[line][column + 1] = (x, y, alive)
                    
                    del(tabShot[i])
                    
                    # On retourne la fonction pour la recommencer avec le nouveau tableau de tir (et ainsi �viter les bugs d�s au changement).
                    return shotMove()
                
        # Si la hitboxe du vaisseau et du missile se touchent et que le missile est un missile ennemi, et que le missile est en vie.          
        if tabShot[i][0] <= (x_vaisseau + infoVaisseau[2] / 2) and tabShot[i][0] >= (x_vaisseau - infoVaisseau[2] / 2 ) and tabShot[i][1] >= (y_vaisseau - infoVaisseau[2] / 2 ) and tabShot[i][1] <= (y_vaisseau + infoVaisseau[2] / 2) and tabShot[i][2] == -1 and tabShot[i][3] == 1 and isTouched <= 0:
                
                # On retire une vie au vaisseau, et on détruit le missile.
                liveVaisseau(-1)
                isTouched = 120
                del(tabShot[i])
                
                # On retourne la fonction pour la recommencer avec le nouveau tableau de tir (et ainsi �viter les bugs d�s au changement).
                return shotMove()


        for w in range (len(tabOvni)):

            # Si la hitboxe de l'ovni et du missile se touchent et que le missile est un missile allié, et que le missile est en vie.          
            if tabShot[i][0] <= (tabOvni[w][0] + ovniInfos[2] / 2) and tabShot[i][0] >= (tabOvni[w][0] - ovniInfos[2] / 2) and tabShot[i][1] >= (tabOvni[w][1] - ovniInfos[2] / 2) and tabShot[i][1] <= (tabOvni[w][1] + ovniInfos[2] / 2) and tabShot[i][2] == 1 and tabShot[i][3] == 1 and tabOvni[w][3] == 1:
                
                    # On retire une vie au vaisseau, et on d�truit le missile.
                    pyxel.play(1, 4)
                    score(500)
                    tabShot[i] = (tabShot[i][0], tabShot[i][1], tabShot[i][2], 10 )
                    tabOvni[w][3] = 2
                
                    # On retourne la fonction pour la recommencer avec le nouveau tableau de tir (et ainsi �viter les bugs d�s au changement).
                    return shotMove()
            
        
        # Si un missile sort de la sc�ne
        if tabShot[i][0] < (0 - shotSkinAlly[allyShotToShow][3] / 2 - margeScreen) or tabShot[i][0] > (widthScreen[0] + widthLenght + shotSkinAlly[allyShotToShow][3] / 2  + margeScreen) or tabShot[i][1] < (0 - shotSkinAlly[allyShotToShow][3] / 2 - margeScreen) or tabShot[i][1] > (heightScreen + shotSkinAlly[allyShotToShow][3] / 2 + margeScreen):
            
            # On le supprime pour �viter les lags.
            del(tabShot[i])
            
            # On retourne la fonction pour la recommencer avec le nouveau tableau de tir (et ainsi �viter les bugs d�s au changement).
            return shotMove()
            
            
        # Pour chaque missile
        for w in range (len(tabShot)):
            
            # Si ce missile touche un autre missile du camp oppos�
            if w != i and tabShot[i][0] <=  (tabShot[w][0] + shotSkinAlly[allyShotToShow][2] / 2) and tabShot[i][0] >= (tabShot[w][0] - shotSkinAlly[allyShotToShow][2] / 2) and ( tabShot[i][1] >= (tabShot[w][1] - shotSkinAlly[allyShotToShow][3] / 2) and tabShot[i][1] <= (tabShot[w][1] + shotSkinAlly[allyShotToShow][3] / 2) ) and tabShot[w][3] == 1 and tabShot[i][3] == 1:
                
                # On lui affecte l'�tat d'explos�
                if w > i:
                    
                    tabShot[w] = (tabShot[w][0], tabShot[w][1], tabShot[w][2], 10 )
                    tabShot[i] = (tabShot[i][0], tabShot[i][1], tabShot[i][2], 10 )

        
        # Si le missile a l'�tat d'explos�
        if tabShot[i][3] != 1:

            # On modifie son compte � rebours
            tabShot[i] = (tabShot[i][0], tabShot[i][1], tabShot[i][2], tabShot[i][3] - 1)

            # Si le compte � rebours est termin�, on d�truit le missile.
            if tabShot[i][3] == 1:

                del(tabShot[i])

                return shotMove()



def laserVerticalBonus():
    """
        Cette fonction effectue le bonus laserVertical détruisant tous les ennemis d'une colonne colonne aléatoire, où au moins 1 ennemi est en vie.
    """
    global tabEnnemies

    pyxel.play(0, 3)

    # On choisit la colonne à tuer
    column = random.randint(0, ennemyPerLine - 1)
    liveVerification = False

    # On vérifie qu'il y ai au moins un ennemi vivant à l'intérieur
    for line in range (numberOfLine):

        if tabEnnemies[line][column][2] == 1:

            liveVerification = True

    # Sinon, on choisit une autre colonne
    if liveVerification == False:

        return laserVerticalBonus()

    # Si oui, on détruit tous les ennemis de la colonne.
    else:

        for line in range (numberOfLine):

            tabEnnemies[line][column] = (tabEnnemies[line][column][0], tabEnnemies[line][column][1], 20)



def laserHorizontalBonus():
    """
        Cette fonction effectue le bonus laserHorizontal détruisant tous les ennemis d'une ligne colonne aléatoire, où au moins 1 ennemi est en vie.
    """

    global tabEnnemies

    pyxel.play(0, 3)

    # On choisit la ligne
    line = random.randint(0, numberOfLine - 1)
    liveVerification = False

    # Si au moins un ennemi de la ligne est en vie, on la garde
    for column in range (ennemyPerLine):

        if tabEnnemies[line][column][2] == 1:

            liveVerification = True

    # Sinon, on en choisit une autre
    if liveVerification == False:

        return laserHorizontalBonus()

    # On détruit tous les ennemis de la ligne
    else:

        for column in range (ennemyPerLine):

            tabEnnemies[line][column] = (tabEnnemies[line][column][0], tabEnnemies[line][column][1], 20)



def portalBonus():
    """
        Cette fonction gère le bonus de téléportation, du placement des portails, jusqu'à la téléportation en elle-même.
    """

    global waitAnimPortal
    global portalToShow
    global cooldownChoosePortal
    global teleportationCooldown
    global x_vaisseau
    global y_vaisseau
    
    # On diminue les timers
    cooldownChoosePortal = cooldownChoosePortal - 1
    waitAnimPortal = waitAnimPortal + 1
    teleportationCooldown = teleportationCooldown - 1

    cooldown = 60
    
    # On anime le portail
    if waitAnimPortal % chronoAnimPortal == 0:

        portalToShow = portalToShow + 1

        if portalToShow == len(portalSkin):

            portalToShow = 0


    # Si les 2 portails n'ont pas encore été crée
    if len(tabPortal) < 2:

        # On affiche une icone de portail sur la souris
        pyxel.blt(pyxel.mouse_x - portalSkin[portalToShow][2] / 2, pyxel.mouse_y - portalSkin[portalToShow][2] / 2, 1, portalSkin[portalToShow][0], portalSkin[portalToShow][1], portalSkin[portalToShow][2], portalSkin[portalToShow][3], 0)

        # Si le joueur tente de placer le portail et que celui - ci se trouve dans une zone atteignable par le vaisseau, et que le cooldown de placement est respecté
        if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ) and pyxel.mouse_x < rightBorder and pyxel.mouse_x > leftBorder and pyxel.mouse_y < borderDown and pyxel.mouse_y > borderUp and cooldownChoosePortal <= 0:

            # On ajoute un portail, et on remet le cooldown
            tabPortal.append([pyxel.mouse_x, pyxel.mouse_y])
            cooldownChoosePortal = 10


    # On affiche chaque portail
    for portal in range (len(tabPortal)):

        pyxel.blt(tabPortal[portal][0] - portalSkin[portalToShow][2] / 2, tabPortal[portal][1] - portalSkin[portalToShow][2] / 2, 1, portalSkin[portalToShow][0], portalSkin[portalToShow][1], portalSkin[portalToShow][2], portalSkin[portalToShow][3], 0)


    # Si le vaisseau entre dans le portail 1 et que le cooldown de téléportation est respecté, on l'amène au portail 2
    if len(tabPortal) == 2 and tabPortal[0][0] < x_vaisseau + infoVaisseau[2] / 2 and tabPortal[0][0] > x_vaisseau - infoVaisseau[2] / 2 and tabPortal[0][1] < y_vaisseau + infoVaisseau[3] / 2 and tabPortal[0][1] > y_vaisseau - infoVaisseau[3] / 2  and teleportationCooldown <= 0:

        pyxel.play(1, 6)
        x_vaisseau = tabPortal[1][0]
        y_vaisseau = tabPortal[1][1]
        teleportationCooldown = cooldown


    # Si le vaisseau entre dans le portail 2 et que le cooldown de téléportation est respecté, on l'amène dans le portail 1
    if len(tabPortal) == 2 and tabPortal[1][0] < x_vaisseau + infoVaisseau[2] / 2 and tabPortal[1][0] > x_vaisseau - infoVaisseau[2] / 2 and tabPortal[1][1] < y_vaisseau + infoVaisseau[3] / 2 and tabPortal[1][1] > y_vaisseau - infoVaisseau[3] / 2  and teleportationCooldown <= 0:

        pyxel.play(1, 6)
        x_vaisseau = tabPortal[0][0]
        y_vaisseau = tabPortal[0][1]
        teleportationCooldown = cooldown



                    
#--------------------------------------------------------------------------------------------------------------------------------------#
        # Fonctions relatives aux ennemies
#--------------------------------------------------------------------------------------------------------------------------------------# 


def affiche_ennemies():
    """
        Cette fonction permet simplement d'afficher les visuels des ennemis aux coordonn�es demand�es.
    """

    global tabEnnemies
    global waitEnnemiAnim
    global ennemiToShow

    waitEnnemiAnim = waitEnnemiAnim + 1

    # On anime les ennemis
    if waitEnnemiAnim >= chronoEnnemiAnim:

        ennemiToShow = ennemiToShow + 1
        waitEnnemiAnim = 0

        if ennemiToShow > 2:

            ennemiToShow = 0
    
    # Pour chaque �l�ment pr�sent dans le tableau, donc chaque ennemi:
    for line in range ( len(tabEnnemies) ):
        
        for ennemy in range (len(tabEnnemies[0])):
        
            # Si l'ennemi est en vie, on affiche son visuel
            if tabEnnemies[line][ennemy][2] == 1:

                # Selon sa ligne, on lui offre un visuel différent
                if line + 1 >= 2 * len(tabEnnemies) / 3 :
                    
                    pyxel.blt(tabEnnemies[line][ennemy][0] - decalEnnemyX, tabEnnemies[line][ennemy][1] - decalEnnemyY, 0, ennemiSkin3[ennemiToShow][0], ennemiSkin3[ennemiToShow][1], ennemiSkin3[ennemiToShow][2], ennemiSkin3[ennemiToShow][3], 0)


                elif line + 1 <= 2 * len(tabEnnemies) / 3 and line + 1 >= len(tabEnnemies) / 3:
                    
                    pyxel.blt(tabEnnemies[line][ennemy][0] - decalEnnemyX, tabEnnemies[line][ennemy][1] - decalEnnemyY, 0, ennemiSkin2[ennemiToShow][0], ennemiSkin2[ennemiToShow][1], ennemiSkin2[ennemiToShow][2], ennemiSkin2[ennemiToShow][3], 0)


                elif line + 1 <= len(tabEnnemies) / 3 :
                    
                    pyxel.blt(tabEnnemies[line][ennemy][0] - decalEnnemyX, tabEnnemies[line][ennemy][1] - decalEnnemyY, 0, ennemiSkin[ennemiToShow][0], ennemiSkin[ennemiToShow][1], ennemiSkin[ennemiToShow][2], ennemiSkin[ennemiToShow][3], 0)
            

            # Si l'ennemi est en état d'explosion, on l'explose.
            if tabEnnemies[line][ennemy][2] > 1:

                pyxel.blt(tabEnnemies[line][ennemy][0] - decalEnnemyX, tabEnnemies[line][ennemy][1] - decalEnnemyY, imgExplosion, explosion[0], explosion[1], explosion[2], explosion[3], 0)
                
                tabEnnemies[line][ennemy] = (tabEnnemies[line][ennemy][0], tabEnnemies[line][ennemy][1], tabEnnemies[line][ennemy][2] - 1)


                # Si l'ennemi a fini d'exploser (compte à rebours à 1), on lui affecte le statut de mort.
                if tabEnnemies[line][ennemy][2] == 1:

                    tabEnnemies[line][ennemy] = (tabEnnemies[line][ennemy][0], tabEnnemies[line][ennemy][1], 0)



def horizontalManager():
    """
        Cette fonction gère tous les déplacements horizontaux
    """ 
    global countH
    global waitH
    global moveSpeed
    global canDoVertical
    global rightEnnemy
    global leftEnnemy
    

    # Cette boucle va permettre le d�placement de tout le groupe d'ennemi.
    # Si le d�lais entre chaque d�placement est �coul�, et que les ennemis ne sont pas d�j� en d�plcament vertical:
    if moveSpeed < 0 and doingVertical == 0:
        
        canDoVertical = 0

        # Cette boucle va permettre de faire bouger les ennemies colonne par colonne.
        for colonne in range (ennemyPerLine):
            
            # Si le d�lais d'attente entre chaque d�placement correspond � celui recherch�
            if colonne * waitOriginalH == waitH:
                
                # On bouge et on affiche la colonne.
                ennemyMoveHorizontal(sensH, colonne)
                countH = countH + 1
        
        waitH = waitH + 1
        
        
        # Si toutes les colonnes ont �t� effectu�es.
        if countH == ennemyPerLine:
            
            # On r�initialise les variables par d�faut.
            countH = 0
            moveSpeed = moveSpeedOriginal
            waitH = 0
            
            # Le mouvement horizontal est fini: le vertical peut donc s'�x�cuter.
            canDoVertical = 1
            
            # On met � jour � chaque frame la position de l'ennemi en vie le plus � droite et le plus � gauche (celui qui atteindra une bordure le plus vite).
            
            rightEnnemy = setRightEnnemy(0)
            leftEnnemy = setLeftEnnemy(0)   

                

def verticalManager():
    """
        Cette fonction gère tous les déplacements verticaux
    """
    global doingVertical
    global countV
    global sensH
    global waitV
    global canDoVertical
    global moveSpeed

    margeEnnemies = 10

    # Syst�me qui permettra le d�placement vertical: si une des 2 bordures est atteinte, et que le mouvement horizontal ne s'effectue pas
    if (rightEnnemy[0] + decalEnnemyX / 2 >= rightBorder - margeEnnemies or leftEnnemy[0] - decalEnnemyX / 2 <= leftBorder + margeEnnemies) and moveSpeed > 0 and canDoVertical == 1:
        
        moveSpeed = moveSpeed + 1
        doingVertical = 1
        
        # Cette boucle fait vouger les ennemis ligne par ligne
        for line in range (numberOfLine):
            
            # Si le d�lais d'attente entre chaque d�placement correspond � celui recherch�
            if line * waitOriginalV == waitV:
                
                # On bouge et on affiche la ligne
                ennemyMoveVertical(line)
                countV = countV + 1
                
        waitV = waitV + 1
        
        # Si toutes les lignes ont �t� effectu�es.
        if countV == numberOfLine:
            
            # On r�initialise les variables par d�faut.
            doingVertical = 0
            countV = 0
            
            # Les ennemies ont atteint une bordure, ils ne doivent pas la franchir. Pour cela on change le sens horizontal de d�placement en cours.
            sensH = - sensH
            waitV = 0
            
            # Cette variable est faite pour ne pas que le mouvement vertical se r�p�te � l'infini.
            canDoVertical = 0



def ennemyMoveHorizontal(sens, column):
    """
        Cette fonction permet de changer les coordonn�es d'une colonne d'ennemis pour un d�placement horizontal.
    """

    # Variables globales qu'on devra utiliser.
    global tabEnnemies
    
    # Vitesse de d�pacement de chaque colonne.
    celerity = 10
    
    # Pour chaque ligne
    for i in range(numberOfLine):
        
        # On ajoute la vitesse aux coordonn�es x de l'ennemi, positif ou n�gatif selon le sens du mouvement.
        xNew = tabEnnemies[i][column][0] + celerity * sens
        yNew = tabEnnemies[i][column][1]
        isAlive = tabEnnemies[i][column][2]
        tabEnnemies[i][column] = (xNew, yNew, isAlive)
        
    

def ennemyMoveVertical(line):
    """
        Fonction qui permet le changement des coordonn�es des ennemis pour un mouvement vertical.
    """
    global tabEnnemies
    
    # Vitesse de d�pacement de chaque ligne.
    celerity = 10
    
    # Pour chaque ennemi dans la ligne concern�e
    for ennemy in range(ennemyPerLine):
        
        # On ajoute la vitesse aux coordonn�es y de l'ennemi.
        xNew = tabEnnemies[line][ennemy][0]
        yNew = tabEnnemies[line][ennemy][1] + celerity
        isAlive = tabEnnemies[line][ennemy][2]
        tabEnnemies[line][ennemy] = (xNew, yNew, isAlive)
           
    
    
def setRightEnnemy(lastLine = 0):
    """
        Fonction qui permet de d�terminer l'ennemi en vie le plus � droite.
    """
       
    for line in range (numberOfLine):
        
        # Sur la ligne qu'on v�rifie, on regarde si l'ennemi le plus � droite est en vie d'o� le -1.
        # On fait �a pour chaque ligne
        # - lastLine permet de d�terminer quelle colonne on v�rifie.
        if tabEnnemies[line][-(1 + lastLine)][2] == 1:
            
            # S'il est en vie, on retourne ses positions.
            return tabEnnemies[line][-(1 + lastLine)]
    
    # Si tous les ennemis de la colonne d'ennemis sont morts, on v�rifie la colonne pr�c�dente (d'o� le moins 1)
    # Vive la r�cursivit� !

    if columnChanges(True) == True:

        return setRightEnnemy(lastLine + 1)

    else:
       
        return (rightBorder,heightScreen,0)



def setLeftEnnemy(lastLine):
    """
        Fonction qui permet de d�terminer l'ennemi en vie le plus � gauche.
    """
       
    for line in range (numberOfLine):
        
        # Sur la ligne qu'on v�rifie, on regarde si l'ennemi le plus � gauche est en vie.
        # On fait �a pour chaque ligne
        # lastLine permet de d�terminer quelle colonne on v�rifie.
        if tabEnnemies[line][lastLine][2] == 1:
            
            # S'il est en vie, on retourne ses positions.
            return tabEnnemies[line][lastLine]
    
    # Si tous les ennemis de la colonne d'ennemis sont morts, on v�rifie la colonne suivante (d'o� le moins 1)
    # Vive la r�cursivit� !

    if columnChanges(True) == True:

        return setLeftEnnemy(lastLine + 1)

    else:
       
        return (leftBorder,heightScreen,0)



def setDownEnnemy(lastLine):
    """
         Fonction qui permet de d�terminer l'ennemi en vie le plus bas.
    """
    
    # + 1 car on tuilisera des incides n�gatifs
    for line in range (numberOfLine + 1):
        
        for column in range (ennemyPerLine):
        
            # On v�rifie chaque ennemi en partant de la fin, et on retourne les coordonn�es du premier en vie trouv�
            if tabEnnemies[-line][column][2] == 1:
                
                # S'il est en vie, on retourne ses positions
                return tabEnnemies[-1 - column * line]
            
            

def chooseEnnemyToShot():
    
    randomLine = numberOfLine - 1
    randomEnnemy = ennemyPerLine - 1
    toShotLine = random.randint(0, randomLine)
    toShotEnnemy = random.randint(0, randomEnnemy)
    
    # Si l'ennemi choisit au hasard est en vie, on lui fait tirer un missile.
    if tabEnnemies[toShotLine][toShotEnnemy][2] == 1:
    
        tabShot.append((tabEnnemies[toShotLine][toShotEnnemy][0], tabEnnemies[toShotLine][toShotEnnemy][1], -1, 1))
    
    # Sinon, on va chercher un autre ennemi en vie pour tirer.
    else:
        
        # Simple s�curit� si aucun ennemi n'est en vie pour �viter les bugs.
        if columnChanges(True) == True:

            chooseEnnemyToShot()



def columnChanges(verification = False):
    """
        Cette fonction permet de v�rifier combien de colonnes sont encore en vie,
        C'est � dire s'il reste au moins un ennemi vivant dans la colonne.
        En fonction de cette info elle augmente la vitesse de d�placement des ennemis ou non.
    """

    global moveSpeedOriginal

    numberColumnAlive = 0

    for i in range (ennemyPerLine):

        alive = False

        for k in range (numberOfLine):

            if tabEnnemies[k][i][2] == 1:

                alive = True

        if alive == True:

            numberColumnAlive = numberColumnAlive + 1

    moveSpeedOriginal = numberColumnAlive * moveSpeedOrigine / ennemyPerLine


    # Si l'on veut juste v�rifier si des ennemis sont encore en vie, on utilise les lignes ci dessous.
    if verification == True and numberColumnAlive == 0:

        return False

    elif verification == True and numberColumnAlive != 0:

        return True



def deathByEnnemy():
    """
        Cette fonction permet de v�rifier si un ennemi touche ou non le vaisseau.
        Si oui, il perd une vie.
        Si l'ennemi touche le fond de l'écran, le joueur a perdu
    """

    global isTouched

    # Pour chaque ennemi
    for i in range (numberOfLine):

        for k in range (ennemyPerLine):

            # S'il touche le vaisseau
            if  ( (x_vaisseau - infoVaisseau[2] / 2 <= (tabEnnemies[i][k][0] + decalEnnemyX) and x_vaisseau + infoVaisseau[2] / 2 >= (tabEnnemies[i][k][0] - decalEnnemyX)) or ( (x_vaisseau + infoVaisseau[2] / 2 <= (tabEnnemies[i][k][0] + decalEnnemyX) and x_vaisseau + infoVaisseau[2] / 2 >= (tabEnnemies[i][k][0] - decalEnnemyX) ) ) ) and ( ( y_vaisseau - infoVaisseau[3] / 2 <= (tabEnnemies[i][k][1] + decalEnnemyY) and y_vaisseau - infoVaisseau[3] / 2 >= (tabEnnemies[i][k][1] - decalEnnemyY)) or ( y_vaisseau + infoVaisseau[3] / 2 >= (tabEnnemies[i][k][1] - decalEnnemyY) and  y_vaisseau + infoVaisseau[3] / 2 <= (tabEnnemies[i][k][1] + decalEnnemyY) ) ) and tabEnnemies[i][k][2] == 1 and isTouched <= 0:

                # Celui ci perd une vie et devient invincible
                liveVaisseau(-1)
                isTouched = 120

            # S'il touche le fond de l'écran, le joueur perd
            if tabEnnemies[i][k][1] + decalEnnemyY >= 19 * heightScreen / 20 and tabEnnemies[i][k][2] == 1:

                liveVaisseau(-100)



#--------------------------------------------------------------------------------------------------------------------------------------#
        # Fonctions relatives aux astéroïds / ovni
#--------------------------------------------------------------------------------------------------------------------------------------# 

def asteroidAdd():
    """
        Cette fonction crée un astéroid
    """
    global tabAsteroid

    x = 0
    marge = 50

    sens = random.randint(0,1)

    # On détermine sons sesn aléatoirement et on ajuste ses coordonnées selon cela
    if sens == 1:

        x = 0 - marge

    else:

        x = widthEntireScreen + marge
        sens = - 1

    # On ajoute un astéroid au tableau des astéroids.
    tabAsteroid.append([x, random.randint(y_vaisseau - infoVaisseau[3] * 3, y_vaisseau + infoVaisseau[3] * 3), sens, random.randint(0,1)])



def asteroidMove():
    """
        Cette fonction fait bouger chaque astéroid
    """

    global tabAsteroid
    global isTouched



    marge = 100

    asteroidSkin = [128, 2, 16, 13]
    asteroidSkin2 = [128, 18, 16, 12]

    decalAsteroidX = asteroidSkin[2] / 2
    decalAsteroidY = asteroidSkin[3] / 2

    asteroidCelerity = 4

    # Pour chaque astéroid
    for asteroid in range (len(tabAsteroid)):

        tabAsteroid[asteroid][0] = tabAsteroid[asteroid][0] + asteroidCelerity * tabAsteroid[asteroid][2]

        # Si celui sort de l'écran
        if tabAsteroid[asteroid][0] < - marge or tabAsteroid[asteroid][0] > widthEntireScreen + marge or tabAsteroid[asteroid][1] + decalAsteroidX > heightEntireScreen or tabAsteroid[asteroid][1] - decalAsteroidX < 0:

            # On le supprime
            del(tabAsteroid[asteroid])
            return asteroidMove()

        # Si l'ennemi touche l'astéroid
        if ( (x_vaisseau - infoVaisseau[2] / 2 <= (tabAsteroid[asteroid][0] + decalAsteroidX) and x_vaisseau - infoVaisseau[2] / 2 >= tabAsteroid[asteroid][0] - decalAsteroidX) or ( (x_vaisseau + infoVaisseau[2] / 2 <= (tabAsteroid[asteroid][0] + decalAsteroidX)) and x_vaisseau + infoVaisseau[2] / 2 >= (tabAsteroid[asteroid][0] - decalAsteroidX) ) ) and ( ( y_vaisseau - infoVaisseau[3] / 2 <= (tabAsteroid[asteroid][1] + decalAsteroidY) and y_vaisseau - infoVaisseau[3] / 2 >= (tabAsteroid[asteroid][1] - decalAsteroidY)) or ( ( y_vaisseau + infoVaisseau[3] / 2 >= (tabAsteroid[asteroid][1] - decalAsteroidY) and y_vaisseau + infoVaisseau[3] / 2 <= (tabAsteroid[asteroid][1] + decalAsteroidY) ) ) ) and isTouched <= 0 :

            # Il gagne un période d'invincibilité et perd une vie
            isTouched = 120
            liveVaisseau(-1)


        # On affiche l'astéroid selon son skin définit lors de sa création
        if tabAsteroid[asteroid][3] == 0:

            pyxel.blt(tabAsteroid[asteroid][0] - decalAsteroidX, tabAsteroid[asteroid][1] - decalAsteroidY, 0, asteroidSkin[0], asteroidSkin[1], asteroidSkin[2], asteroidSkin[3], 0)


        elif tabAsteroid[asteroid][3] == 1:

            pyxel.blt(tabAsteroid[asteroid][0] - decalAsteroidX, tabAsteroid[asteroid][1] - decalAsteroidY, 0, asteroidSkin2[0], asteroidSkin2[1], asteroidSkin2[2], asteroidSkin2[3], 0)



def ovniAdd():
    """
        Cette fonction crée un ovni
    """
    global tabOvni

    marge = 50

    # On détermine juste son sens aléatoirement, puis on ajoute les coordonnées correspondantes.
    sens = random.randint(0,1)

    if sens == 1:

        x = 0 - marge

    else:

        x = widthEntireScreen + marge
        sens = - 1

    tabOvni.append([x, heightEntireScreen / 16, sens, 1])



def ovniMove():
    """
        Cette fonction permet de faire bouger les ovnis
    """

    global tabOvni
    global isTouched

    global waitOvni
    global circleToShow

    marge = 100

    ovniCelerity = 2

    # Pour chaque ovni,
    for ovni in range (len(tabOvni)):

        # On le fait avancer
        tabOvni[ovni][0] = tabOvni[ovni][0] + ovniCelerity * tabOvni[ovni][2]

        # S'il sort de la scène, on le supprime
        if tabOvni[ovni][0] < - marge or tabOvni[ovni][0] > widthEntireScreen + marge or tabOvni[ovni][1] + ovniInfos[2] / 2 > heightEntireScreen or tabOvni[ovni][1] - ovniInfos[2] / 2 < 0:

            del(tabOvni[ovni])
            return ovniMove()


        # S'il touche le vaisseau, celui-ci perd une vie
        if ( ( (x_vaisseau - infoVaisseau[2] / 2 <= (tabOvni[ovni][0] + ovniInfos[2] / 2) and x_vaisseau + infoVaisseau[2] / 2 >= tabOvni[ovni][0] - ovniInfos[2] / 2)) or ( (x_vaisseau + infoVaisseau[2] / 2 <= (tabOvni[ovni][0] + ovniInfos[2] / 2)) and x_vaisseau + infoVaisseau[2] / 2 >= (tabOvni[ovni][0] - ovniInfos[2] / 2) ) ) and ( ( y_vaisseau - infoVaisseau[3] / 2 <= (tabOvni[ovni][1] + ovniInfos[3] / 2) and y_vaisseau - infoVaisseau[3] / 2 >= (tabOvni[ovni][1] - ovniInfos[3] / 2)) or ( y_vaisseau + infoVaisseau[3] / 2 >= (tabOvni[ovni][1] - ovniInfos[3] / 2) and  y_vaisseau + infoVaisseau[3] / 2 <= (tabOvni[ovni][1] + ovniInfos[3] / 2) ) ) and isTouched <= 0 and tabOvni[ovni][3] == 1:

            isTouched = 120
            liveVaisseau(-1)

        spaceCircle = 3


        # On anime ses petits cercles
        if waitOvni % chronoAnimCircles == 0:

            circleToShow = circleToShow + 1

            if circleToShow == len(ovniCircles):

                circleToShow = 0


        # Paramètre qui permet de faire explosé l'ovni si souhaité (non utilisé ici)
        if tabOvni[ovni][3] != 1:

            # On modifie son compte à rebours
            tabOvni[ovni][3] = tabOvni[ovni][3] - 1
            pyxel.blt(tabOvni[ovni][0] - explosion[2] / 2, tabOvni[ovni][1] - explosion[3] / 2, imgExplosion, explosion[0], explosion[1], explosion[2], explosion[3], 0)

            # Si le compte à rebours est terminé, on détruit le missile.
            if tabOvni[ovni][3] == 1:

                del(tabOvni[ovni])

                return ovniMove()


        # Si l'ovni est en vie, on l'affiche lui et ses cercles.
        elif tabOvni[ovni][3] == 1:

            pyxel.blt(tabOvni[ovni][0] - ovniInfos[2] / 2, tabOvni[ovni][1] - ovniInfos[3] / 2, 0, ovniInfos[0], ovniInfos[1], ovniInfos[2], ovniInfos[3], 0)
            pyxel.blt(tabOvni[ovni][0] - ovniCircles[circleToShow][2] / 2, tabOvni[ovni][1] + ovniInfos[3] / 2 + spaceCircle - ovniCircles[circleToShow][3] / 2 , 0, ovniCircles[circleToShow][0], ovniCircles[circleToShow][1], ovniCircles[circleToShow][2], ovniCircles[circleToShow][3], 0)

        
        
#--------------------------------------------------------------------------------------------------------------------------------------#
        # Fonctions utilitaires et autres
#--------------------------------------------------------------------------------------------------------------------------------------# 

def backgroundAdd(startPosition = 0):
    """
        Cette fonction fait partie du fonctionnement du background. Elle ajoute un peu d'�toile quand elle est appel�e.
    """

    global tabStar

    # Gr�ce � random, la fonction d�termine la position initiale des �toiles, ainsi que son type.
    toAppend = [random.randint(0 + 8, 400 - 8), heightEntireScreen - startPosition]
    
    # Puis on ajoute la nouvelle �toile � celle pr�c�demment cr�es dans le tableau qui les g�res.
    tabStar.append(toAppend)


    
def backgroundMove(sens = 1):
    """
        Cette fonction anime le fond en faisant avancer les �toiles.
    """

    global tabStar

    limit = -16
    starCelerity = 2 * sens

    # Pour chaque �toile
    for element in range (len(tabStar)):
        
        # On met � jour sa position en fonction de sa vitesse.
        tabStar[element][1] = tabStar[element][1] - starCelerity

        # Si elle est sortie de l'�cran, on la supprime.
        if tabStar[element][1] < limit:

            del(tabStar[element])
            return backgroundMove()

        pyxel.blt(tabStar[element][0], tabStar[element][1], 1, 80, 0, 1, 1, 0)



def createGameButton():
    """
        Cette fonction crée le nombre demandé de bouton de jeu voulu
    """
    global tabButtonGame

    marge = 10
    # On définit les coordonnées du premier bouton
    tabButtonGame.append([widthEntireScreen - marge - bigButtonNormal[2] / 2, heightEntireScreen / 6, 0, 0, 0])

    numberOfButtons = 5

    # On crée la suite des boutons (coordonnées, nombre, cooldown, wrongTime)
    for i in range (numberOfButtons - 1):

        tabButtonGame.append( [tabButtonGame[0][0], tabButtonGame[0][1] + marge * (i + 1) + bigButtonNormal[3] * (i + 1), tabButtonGame[0][2] + i + 1, 0, 0] )



def gameButton():
    """
        Cette fonction gère tous les boitons présents lors de la partie
    """
    global notEnoughTimer
    global actualScore
    global tabButtonGame

    global bigShot
    global activatePortalBonus

    wrongTime = 30
    cooldownButton = 30

    scoreHeal = 500
    scoreBigShot = 1000
    scoreLaser = 1000
    scorePortal = 500

    # Pour chaque bouton
    for k in range (len(tabButtonGame)):

        # On diminue son cooldown, ainsi que son temps Wrong
        tabButtonGame[k][3] = tabButtonGame[k][3] - 1
        tabButtonGame[k][4] = tabButtonGame[k][4] - 1


        # Si le joueur passe sa souris sur le bouton et que celui-ci n'est pas en mode Wrong
        if pyxel.mouse_x > tabButtonGame[k][0] - bigButtonNormal[2] / 2 and pyxel.mouse_x < tabButtonGame[k][0] + bigButtonNormal[2] / 2 and pyxel.mouse_y > tabButtonGame[k][1] - bigButtonNormal[3] / 2 and pyxel.mouse_y < tabButtonGame[k][1] + bigButtonNormal[3] / 2 and tabButtonGame[k][4] <= 0:


            # Selon le nombre du bouton appuyé, on effectue différentes actions
            # Si on appuie sur le bouton et qu'on a assez de score, un cooldown se met en place pour ne pas qu'on puisse rappuyer sur le bouton trop vite.
            # Si le bouton est pressé sans avoir le score nécessaire, alors le bouton passe en mode Wrong pendant un petit temps.
            
            # On affiche un bouton touché lorsque le joueur survole le bouton.
            pyxel.blt(tabButtonGame[k][0] - bigButtonNormal[2] / 2, tabButtonGame[k][1] - bigButtonNormal[3] / 2, imgButton, bigButtonTouched[0], bigButtonTouched[1], bigButtonTouched[2], bigButtonTouched[3], 0)



            if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ) and tabButtonGame[k][2] ==  0 and tabButtonGame[k][3] <= 0 and tabButtonGame[k][4] <= 0:

                if actualScore >= scoreHeal and actualLife < maxLives:
                        
                        pyxel.play(0, 2)
                        score(-scoreHeal)
                        liveVaisseau(1)
                        tabButtonGame[k][3] = cooldownButton

                else:

                        pyxel.play(0, 1)
                        tabButtonGame[k][4] = wrongTime



            if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ) and tabButtonGame[k][2] ==  1 and tabButtonGame[k][3] <= 0 and tabButtonGame[k][4] <= 1:

                if actualScore >= scoreBigShot and bigShot == False:

                        score(-scoreBigShot)
                        bigShot = True
                        tabButtonGame[k][3] = cooldownButton
                        pyxel.play(0, 2)

                else:
                        pyxel.play(0, 1)
                        tabButtonGame[k][4] = wrongTime



            if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ) and tabButtonGame[k][2] ==  2 and tabButtonGame[k][3] <= 0 and tabButtonGame[k][4] <= 1:

                if actualScore >= scoreLaser:

                        score(-scoreLaser)
                        laserVerticalBonus()
                        tabButtonGame[k][3] = cooldownButton

                else:
                        pyxel.play(0, 1)
                        tabButtonGame[k][4] = wrongTime



            if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ) and tabButtonGame[k][2] ==  3 and tabButtonGame[k][3] <= 0 and tabButtonGame[k][4] <= 1:

                if actualScore >= scoreLaser:

                        score(-scoreLaser)
                        laserHorizontalBonus()
                        tabButtonGame[k][3] = cooldownButton

                else:
                        pyxel.play(0, 1)
                        tabButtonGame[k][4] = wrongTime


            if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ) and tabButtonGame[k][2] ==  4 and tabButtonGame[k][3] <= 0 and tabButtonGame[k][4] <= 1:

                if actualScore >= scorePortal:

                        score(-scorePortal)
                        activatePortalBonus = True
                        tabButtonGame[k][3] = cooldownButton
                        pyxel.play(0, 2)

                else:
                        pyxel.play(0, 1)
                        tabButtonGame[k][4] = wrongTime
        

        # Si le bouton est en mode Wrong, on affiche un bouton Wrong sans aucune vergogne.
        elif tabButtonGame[k][4] >= 0:

            pyxel.blt(tabButtonGame[k][0] - bigButtonNormal[2] / 2, tabButtonGame[k][1] - bigButtonNormal[3] / 2, imgButton, bigButtonWrong[0], bigButtonWrong[1], bigButtonWrong[2], bigButtonWrong[3], 0)

        
        # Si le bouton n'est pas touchée et pas en mode Wrong, on affiche juste un bouton gentil tout plein.
        else:
            
            pyxel.blt(tabButtonGame[k][0] - bigButtonNormal[2] / 2, tabButtonGame[k][1] - bigButtonNormal[3] / 2, imgButton, bigButtonNormal[0], bigButtonNormal[1], bigButtonNormal[2], bigButtonNormal[3], 0)


    # Enfin, on détermine les coordonnées des textes et on les affiche ici.
    text1 = "Heal"
    text2 = "500"

    coord1 = centerText(tabButtonGame[0][0] + 1, tabButtonGame[0][1] - bigButtonNormal[3] / 6, text1 )
    coord2 = centerText(tabButtonGame[0][0] + 1, tabButtonGame[0][1] + bigButtonNormal[3] / 6, text2 )

    pyxel.text(coord1[0], coord1[1], text1, 7)
    pyxel.text(coord2[0], coord2[1], text2, 7)

    text3 = "Big Shot"
    text4 = "1000"

    coord3 = centerText(tabButtonGame[1][0] + 1, tabButtonGame[1][1] - bigButtonNormal[3] / 6, text3 )
    coord4 = centerText(tabButtonGame[1][0] + 1, tabButtonGame[1][1] + bigButtonNormal[3] / 6, text4 )

    pyxel.text(coord3[0], coord3[1], text3, 7)
    pyxel.text(coord4[0], coord4[1], text4, 7)

    text5 = "Laser 1"
    text6 = "1000"

    coord5 = centerText(tabButtonGame[2][0] + 1, tabButtonGame[2][1] - bigButtonNormal[3] / 6, text5 )
    coord6 = centerText(tabButtonGame[2][0] + 1, tabButtonGame[2][1] + bigButtonNormal[3] / 6, text6 )

    pyxel.text(coord5[0], coord5[1], text5, 7)
    pyxel.text(coord6[0], coord6[1], text6, 7)

    text7 = "Laser 2"
    text8 = "1000"

    coord7 = centerText(tabButtonGame[3][0] + 1, tabButtonGame[3][1] - bigButtonNormal[3] / 6, text7 )
    coord8 = centerText(tabButtonGame[3][0] + 1, tabButtonGame[3][1] + bigButtonNormal[3] / 6, text8 )

    pyxel.text(coord7[0], coord7[1], text7, 7)
    pyxel.text(coord8[0], coord8[1], text8, 7)


    text9 = "Portals"
    text10 = "500"

    coord9 = centerText(tabButtonGame[4][0] + 1, tabButtonGame[4][1] - bigButtonNormal[3] / 6, text9 )
    coord10 = centerText(tabButtonGame[4][0] + 1, tabButtonGame[4][1] + bigButtonNormal[3] / 6, text10 )

    pyxel.text(coord9[0], coord9[1], text9, 7)
    pyxel.text(coord10[0], coord10[1], text10, 7)



def winButtonFonction():
    """
        Fonction qui gère le bouton de victoireS
    """
    global winButton
    global isWon

    winPrice = 20000

    # Cette fonction utilise exactement les mêmes principes que la précédente.

    wrongTime = 30

    winButton[2] = winButton[2] - 1

    if pyxel.mouse_x > winButton[0] - bigButtonNormal[2] / 2 and pyxel.mouse_x < winButton[0] + bigButtonNormal[2] / 2 and pyxel.mouse_y > winButton[1] - bigButtonNormal[3] / 2 and pyxel.mouse_y < winButton[1] + bigButtonNormal[3] / 2 and winButton[2] <= 0:


        pyxel.blt(winButton[0] - bigButtonNormal[2] / 2, winButton[1] - bigButtonNormal[3] / 2, imgButton, bigButtonTouched[0], bigButtonTouched[1], bigButtonTouched[2], bigButtonTouched[3], 0)


        if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ) and winButton[2] <= 0:

            if actualScore >= winPrice:

                gameOver("True")
                isWon = "True2"
                pyxel.play(0, 2)

            else:

                pyxel.play(0, 1)
                winButton[2] = wrongTime


    elif winButton[2] >= 0 :

        pyxel.blt(winButton[0] - bigButtonNormal[2] / 2, winButton[1] - bigButtonNormal[3] / 2, imgButton, bigButtonWrong[0], bigButtonWrong[1], bigButtonWrong[2], bigButtonWrong[3], 0)

    else:

        pyxel.blt(winButton[0] - bigButtonNormal[2] / 2, winButton[1] - bigButtonNormal[3] / 2, imgButton, bigButtonNormal[0], bigButtonNormal[1], bigButtonNormal[2], bigButtonNormal[3], 0)


    text1 = "! Win !"
    text2 = "20 000"

    coord1 = centerText(winButton[0] + 1, winButton[1] - bigButtonNormal[3] / 6, text1 )
    coord2 = centerText(winButton[0] + 1, winButton[1] + bigButtonNormal[3] / 6, text2 )

    pyxel.text(coord1[0], coord1[1], text1, 7)
    pyxel.text(coord2[0], coord2[1], text2, 7)



def welcomeButtonActions(infosButton):
    """
        Cette fonction r�git tout ce qui touche aux boutons du menu.
        Elle le change de couleur quand la souris est pass�e dessus.
        Elle effectue l'action correspondant au bouton si demand�.
    """
    
    global init
    global tabStar
    
    # Si la souris passe sur le bouton, celui - ci change de couleur
    if pyxel.mouse_x > infosButton[0] - infosButton[2] and pyxel.mouse_x < infosButton[0] + infosButton[2] and pyxel.mouse_y > infosButton[1] - infosButton[3] and pyxel.mouse_y < infosButton[1] + infosButton[3]:
        
        pyxel.blt(infosButton[0] - infosButton[2], infosButton[1] - infosButton[3], imgButton, buttonTouched[0], buttonTouched[1], buttonTouched[2], buttonTouched[3], 0)
        
        
        # Si la souris est cliqu�e, l'action est effectu�e selon le type de bouton.
        if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ) and infosButton[4] ==  0 and buttonCooldown < 0:
            
            tabStar = []
            init = 1
            pyxel.mouse(False)
            pyxel.cls(0)            
            pyxel.play(0, 2)
            return("Stop")


        if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ) and infosButton[4] ==  1 and buttonCooldown < 0:
            
            init = 5
            pyxel.cls(0)
            pyxel.play(0, 2)
            return("Stop")
            
    # Sinon, le bouton s'affiche de la couleur de base.    
    else:
        
        pyxel.blt(infosButton[0] - infosButton[2], infosButton[1] - infosButton[3], imgButton, buttonNormal[0], buttonNormal[1], buttonNormal[2], buttonNormal[3], 0)
    
     

def gameOverButtons(infosButton):
    """
        Cette fonction r�git tout ce qui touche aux boutons du menu.
        Elle le change de couleur quand la souris est pass�e dessus.
        Elle effectue l'action correspondant au bouton si demand�.
    """

    global init
    global buttonCooldown

    global vSpeed
    global isTouched
    global ennemyPerLine
    global numberOfLine
    global timeShotEnnemy
    global actualLife
    global actualScore
    global currentLevel
    global tabStar
    global isGameOver
    global tabEnnemies
    global tabShot
    global moveSpeedOrigine
    global moveSpeedOriginal
    global waitOriginalH
    global spawnAsteroidOriginal

    global tabAsteroid
    global waitAsteroid

    global waitAnimPortal
    global portalToShow
    global cooldownChoosePortal
    global teleportationCooldown
    global activatePortalBonus
    global tabPortal

    global tabOvni
    global waitOvni

    global soundOverDone
    global soundWinDone

    global isWon
    
    # Si la souris passe sur le bouton, celui - ci change de couleur
    if pyxel.mouse_x > infosButton[0] - infosButton[2] and pyxel.mouse_x < infosButton[0] + infosButton[2] and pyxel.mouse_y > infosButton[1] - infosButton[3] and pyxel.mouse_y < infosButton[1] + infosButton[3]:
        
        pyxel.blt(infosButton[0] - infosButton[2], infosButton[1] - infosButton[3], imgButton, buttonTouched[0], buttonTouched[1], buttonTouched[2], buttonTouched[3], 0)
        
        
        # Si la souris est cliqu�e, les param�tres par d�faut sont initialis�s pour une nouvelle partie.
        if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ):
            
            pyxel.play(0, 2)
            init = 2
            pyxel.cls(0)
            buttonCooldown = 50

            vSpeed = 3
            isTouched = 0
            ennemyPerLine = originalEnnemyPerLine
            numberOfLine = originalNumberOfLine

            moveSpeedOrigine = moveSpeedNexus
            moveSpeedOriginal = moveSpeedOrigine

            spawnAsteroidOriginal = spawnAsteroidOrigine

            tabAsteroid = []
            waitAsteroid = 0

            waitOvni = 0
            tabOvni = []

            waitAnimPortal = 0
            portalToShow = 0
            cooldownChoosePortal = 0
            teleportationCooldown = 0
            activatePortalBonus = False
            tabPortal = []

            soundWinDone = False
            soundOverDone = False

            isWon = "False"

            timeShotEnnemy = timeShotEnnemyOriginal
            waitOriginalH = waitOrigineH
            actualLife = 5
            actualScore = 0
            currentLevel = 1
            tabStar = []
            isGameOver = 0
            tabEnnemies = []
            tabShot = []
            
    # Sinon, le bouton s'affiche de la couleur de base.    
    else:
        
        pyxel.blt(infosButton[0] - infosButton[2], infosButton[1] - infosButton[3], imgButton, buttonNormal[0], buttonNormal[1], buttonNormal[2], buttonNormal[3], 0)
    


def tutorialButtons(infosButton):

    """
        Cette fonction r�git tout ce qui touche aux boutons du menu.
        Elle le change de couleur quand la souris est pass�e dessus.
        Elle effectue l'action correspondant au bouton si demand�.
    """

    global init
    global buttonCooldown

    
    # Si la souris passe sur le bouton, celui - ci change de couleur
    if pyxel.mouse_x > infosButton[0] - infosButton[2] and pyxel.mouse_x < infosButton[0] + infosButton[2] and pyxel.mouse_y > infosButton[1] - infosButton[3] and pyxel.mouse_y < infosButton[1] + infosButton[3]:
        
        pyxel.blt(infosButton[0] - infosButton[2], infosButton[1] - infosButton[3], imgButton, buttonTouched[0], buttonTouched[1], buttonTouched[2], buttonTouched[3], 0)
        
        
        # Si la souris est cliqu�e, on retourne au menu d'accueil
        if ( pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) ):
            
            pyxel.play(0, 2)
            init = 2
            buttonCooldown = 50

            
    # Sinon, le bouton s'affiche de la couleur de base.    
    else:
        
        pyxel.blt(infosButton[0] - infosButton[2], infosButton[1] - infosButton[3], imgButton, buttonNormal[0], buttonNormal[1], buttonNormal[2], buttonNormal[3], 0)

    

def centerText(xCenter, yCenter, text, espaceLetter = 4):
    """
        Fonction qui centre un texte, selon les coordonn�es du centre de ce texte.
    """
    
    heightLetter = 4
    
    # Les coordonn�es sont renvoy�es dans un tableau.
    return [xCenter - len(text) * espaceLetter / 2, yCenter - heightLetter / 2]

            

# On lance le moteur de Pyxel
pyxel.run(update, draw)