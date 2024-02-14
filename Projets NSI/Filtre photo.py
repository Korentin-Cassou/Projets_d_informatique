from PIL import Image


def menu():
    """
        Cette fonction est un menu. A partir de celui-ci, l'utilisateur peut naviguer dans les menues secondaires et choisir n'importe quel filtre disponible.
    """
    
    # On récupère le nom de l'image voulue par l'utilisateur. Celui-ci doit mettre l'image dans le fichier et entrer son nom. On ajoute .jpg pour que l'utilisateur n'ai pas à le faire.
    imageName = input("Entrez le nom de votre fichier jpg cher bipède.\n") + ".jpg"
    
    # Si l'utilisateur appuie sur entrée, l'image par défaut sera chargée.
    if imageName == ".jpg":
        
        imageName = "Omori.jpg"
    
    # On charge l'image et on récupère ses dimensions
    image = Image.open(imageName)
    width = image.width
    height = image.height
    
    # Cette boucle étant présente plusieurs fois dans le programme, elle ne sera expliquée qu'ici.
    # Elle permet de vérifier que la valeur choisie est bien un nombre, et respectant les critères demandés (positif, inférieur à une certaine valeure...)
    intVerification1 = False
    
    while intVerification1 == False:
        
        print("Vous allez maintenant choisir le type de filtre à appliquer. \n\n1.- Echelles de teinte \n2.- Colorisation \n3.- Filtre Rétro \n4.- Filtre Miroir \n")
    
        functionToRealizeString = input("Entrez le nombre correspondant au filtre désiré (je vous en prie)\n")
        
        #Si la string ne contient que des nombres, alors on la convertit en int.
        if functionToRealizeString.isdigit() == True :
        
            functionToRealize = int(functionToRealizeString)
            
            # Si l'int respecte toutes les conditions, alors on met intVerification à True, ce qui nous fait sortir de la boucle while de vérification
            if functionToRealize <= 4 and functionToRealize > 0 :
            
                intVerification1 = True
            
            # Sinon, on affiche un message d'erreur et l'utilisateur doit rentré une nouvelle valeur.
            else:
                    
                print("Vraiment désolé, mais votre chiffre ne correspond à rien ^^'\n")
        
        # Si la variable est une string vide (Enter), on prend la valeur par défaut.
        elif functionToRealizeString == "" :
            
            functionToRealize = 1
            intVerification1 = True
        
        # Sinon, on affiche un message d'erreur et l'utilisateur doit rentrer une valeur.
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")
        
        
    # Ce tableau stocke les fonctions à éxécuter selon le choix de l'utilisateur.
    filters = [colorScaleMenu, colorisationMenu, retroMenu, mirrorFilter]
    # On prend la valeur choisie par l'utilisateur, et on retire 1 (car la liste affichée commence par 1 tandis que notre tableau filters commence par 0).
    # On effectue alors la fonction correspondante, puis on montre l'image obtenue.
    newImage = filters[functionToRealize - 1](width, height, image)
    newImage.show()
    
    # On propose à l'utilisateur de faire une sauvegarde de la nouvelle image.
    save = input("Eh, psss... Vous voulez une sauvegarde... C est gratuit pour cette fois... \nRépondez Yes ou No. \n")
    
    # S'il veut, il choisit un nom à la sauvegarde et l'image est sauvegardée.
    if save == "Yes":
        
        newName = input("Quel sera le nom du fichier céleste ?\n")+".jpg"
        newImage.save(newName)
        print("Votre image a bien été sauvegardée ! ;)")
    
    # Sinon, l'image est supprimée.
    elif save == "No":
        
        print("Votre création a été détruite...")
    
    # Si l'utilisateur tape autre chose, nous lui montrons un RickRoll pour le punir.
    else:
        
        print("Votre irrespect sera puni...")
        imagePunition = Image.open("punition.jpg")
        imagePunition.show()
    


def colorisationMenu(widthR, heightR, imageR):
    """
        Cette fonction est le menu de tous les filtres relatifs à la colorisation.
        Il permet d'accéder à tous les filtres qui colorent l'image.
    """
    
    print("Choisissez la colorisation a réaliser s'il vous plaît :).\n \n1.- Colorisation classique \n2.- Noir et Blanc \n3.- Image négative \n4.- Changements de luminosité")
    
    
    intVerification1 = False
    
    # Boucle de vérification de l'input.
    while intVerification1 == False:
        
        functionToRealizeString = input("Entrez le nombre correspondant :)\n")
          
        if functionToRealizeString.isdigit() == True :
        
            functionToRealize = int(functionToRealizeString)
            
            if functionToRealize <= 4 and functionToRealize > 0:
            
                intVerification1 = True
                    
            else:
                    
                print("Vraiment désolé, mais votre chiffre ne correspond à rien ^^'\n")
            
        elif functionToRealizeString == "" :
            
            functionToRealize = 1
            intVerification1 = True
            
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")
            
    
    # Ce tableau stocke les fonctions à éxécuter selon le choix de l'utilisateur.
    # On prend la valeur choisie par l'utilisateur, et on retire 1 (car la liste affichée commence par 1 tandis que notre tableau filters commence par 0).
    # On effectue alors la fonction correspondante, puis on retourne l'image obtenue.
    filters = [color, blackWhiteFilter, negativeColors, lum]
    newColorisation = filters[functionToRealize - 1](widthR, heightR, imageR)
    
    return newColorisation
    


def colorScaleMenu(widthR, heightR, imageR):
    """
        Cette fonction est le menu de tous les filtres relatifs aux échelles de teinte.
        Il permet d'accéder à tous les filtres qui effectuent une échelle de teinte.
    """
      
    print("Choisissez l'échelle de teinte à effectuer s'il vous plaît :).\n \n1.- Filtre rouge \n2.- Filtre vert \n3.- Filtre bleu \n4.- Filtre magenta \n5.- Filtre cyan \n6.- Filtre jaune \n7.- Filtre gris \n")
    
    # Boucle de vérification d'input.
    intVerification1 = False
    
    while intVerification1 == False:
        
        functionToRealizeString = input("Entrez le nombre correspondant :)\n")
          
        if functionToRealizeString.isdigit() == True :
        
            functionToRealize = int(functionToRealizeString)
            
            if functionToRealize <= 7 and functionToRealize > 0:
            
                intVerification1 = True
                    
            else:
                    
                print("Vraiment désolé, mais votre chiffre ne correspond à rien ^^'\n")
            
        elif functionToRealizeString == "" :
            
            functionToRealize = 1
            intVerification1 = True
            
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")
    
    # Ce tableau stocke les fonctions à éxécuter selon le choix de l'utilisateur.
    # On prend la valeur choisie par l'utilisateur, et on retire 1 (car la liste affichée commence par 1 tandis que notre tableau filters commence par 0).
    # On effectue alors la fonction correspondante, puis on retourne l'image obtenue.
    filters = [redFilter, greenFilter, blueFilter, magentaFilter, cyanFilter, yellowFilter, grayFilter]
    newColorScale = filters[functionToRealize - 1](widthR, heightR, imageR)
    
    return newColorScale



def retroMenu(widthR, heightR, imageR):
    """
        Cette fonction est le menu de tous les filtres rétro.
        Il permet d'accéder à tous les filtres rétro.
    """
        
    print("Choisissez votre filtre Retro. \n\n1.- Pixellisation \n2.- Old Games\n")
    
    # Boucle de vérification d'input.
    intVerification1 = False
    
    while intVerification1 == False :
        
        functionToRealizeString = input("Entrez le nombre correspondant au filtre rétro désiré s'il vous plaît :)\n")
          
        if functionToRealizeString.isdigit() == True :
        
            functionToRealize = int(functionToRealizeString)
            
            if functionToRealize <= 2 and functionToRealize > 0:
            
                intVerification1 = True
                    
            else:
                    
                print("Vraiment désolé, mais votre chiffre ne correspond à rien sur cette Terre ^^'\n")
            
        elif functionToRealizeString == "" :
            
            functionToRealize = 1
            intVerification1 = True
            
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")
    
    # Ce tableau stocke les fonctions à éxécuter selon le choix de l'utilisateur.
    # On prend la valeur choisie par l'utilisateur, et on retire 1 (car la liste affichée commence par 1 tandis que notre tableau filters commence par 0).
    # On effectue alors la fonction correspondante, puis on retourne l'image obtenue.
    filters = [pixelFilter, color512]
    newImageRetro = filters[functionToRealize - 1](widthR, heightR, imageR)
    
    return newImageRetro



def redFilter(widthF, heightF, imageF):
    """
        Cette fonction effectue une échelle de teinte rouge de l'image.
    """
    
    # On parcourt chaque pixel de l'image, en gardant seulement la valeur de la composante rouge, et en affectant 0 aux autres composantes.
    for i in range (widthF) :

        for j in range (heightF) :
            
            # On récupère les couleurs originelles du pixel correspondant dans l'image originelle.
            Colors = imageF.getpixel((i, j))
            # On change les valeurs des composantes souhaitées.
            imageF.putpixel((i, j), (Colors[0], 0, 0))
            
    return imageF
            
        
      
def greenFilter(widthF, heightF, imageF):
    """
        Cette fonction effectue une échelle de teinte verte de l'image.
    """
    
    # On parcourt chaque pixel de l'image, en gardant seulement la valeur de la composante verte, et en affectant 0 aux autres composantes.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            imageF.putpixel((i, j), (0, Colors[1], 0))
            
    return imageF
            
     
       
def blueFilter(widthF, heightF, imageF):
    """
        Cette fonction effectue une échelle de teinte bleue de l'image.
    """
    
    # On parcourt chaque pixel de l'image, en gardant seulement la valeur de la composante bleue, et en affectant 0 aux autres composantes.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            imageF.putpixel((i, j), (0, 0, Colors[2]))
            
    return imageF
            


def magentaFilter(widthF, heightF, imageF):
    """
        Cette fonction effectue une échelle de teinte magenta de l'image.
    """
    
    # On parcourt chaque pixel de l'image, en gardant seulement les valeurs des composantes rouge et bleue, et en affectant 0 à l'autre composante.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            imageF.putpixel((i, j), (Colors[0], 0, Colors[2]))
            
    return imageF



def cyanFilter(widthF, heightF, imageF):
    """
        Cette fonction effectue une échelle de teinte cyan de l'image.
    """
    
    # On parcourt chaque pixel de l'image, en gardant seulement les valeurs des composantes verte et bleue, et en affectant 0 à l'autre composante.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            imageF.putpixel((i, j), (0, Colors[1], Colors[2]))
            
    return imageF



def yellowFilter(widthF, heightF, imageF):
    """
        Cette fonction effectue une échelle de teinte jaune de l'image.
    """
    
    # On parcourt chaque pixel de l'image, en gardant seulement les valeurs des composantes rouge et verte, et en affectant 0 à l'autre composante.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            imageF.putpixel((i, j), (Colors[0], Colors[1], 0))
            
    return imageF
  
  
  
def grayFilter(widthF, heightF, imageF):
    """
        Cette fonction effectue une échelle de teinte grise de l'image.
    """
    
    # On parcourt chaque pixel de l'image.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            # On fait la moyenne des 3 valeurs RGB, et on la stocke dans grayValor
            grayValor = int((Colors[0] + Colors[1] + Colors[2])/3)
            # On affecte cette moyenne aux 3 valeurs RGB de l'image, ce qui donnera un gris plus ou moins foncé en fonction de la valeur de la moyenne.
            imageF.putpixel((i, j), (grayValor, grayValor, grayValor))
            
    return imageF
        


def blackWhiteFilter(widthF, heightF, imageF):
    """
        Cette fonction effectue une colorisation en noir et blanc.
    """
    
    # On parcout chaque pixel de l'image.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            # On fait la moyenne des 3 valeurs RGB
            valor = int((Colors[0] + Colors[1] + Colors[2])/3)
            
            # Si cette moyenne est plus proche de 0, alors on affectera 0 aux trois composantes, ce qui donnera un pixel noir.
            if valor < 128:
                
                valor = 0
            # Si cette moyenne est plus proche de 255, alors on affectera 255 aux trois composantes, ce qui donnera un pixel blanc.   
            else:
                
                valor = 255
            
            imageF.putpixel((i, j), (valor, valor, valor))
            
    return imageF



def mirrorFilter(widthF, heightF, imageF):
    """
        Cette fonction permet d'afficher une image miroir, c'est à dire, comme si on la voyait dans un miroir.
    """
    
    # On crée une nouvelle image car si on modifie directement l'image originelle, on obtiendrait une image symétrique.
    newImage = Image.new("RGB", (widthF, heightF))
    
    # On parcourt chaque pixel de l'image.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            
            # On affecte les valeurs du pixel que l'on est en train de modifier, à son opposé sur la nouvelle image.
            # C'est à dire à son symétrique par symétrie axiale, avec comme axe la médiatrice de la largeur.
            newImage.putpixel((-i, j), (Colors[0], Colors[1], Colors[2]))
            
    return newImage
        


def pixelFilter(widthF, heightF, imageF):
    """
        Cette fonction permet de pixelliser une image.
        L'image sera plus ou moins pixellisée selon la valeur choisie par l'utilisateur.
    """
    
    # Boucle de vérification d'int. (je devrais faire une fonction pour ça.)
    intVerification1 = False
    
    while intVerification1 == False :
        
        pixelValueString = input("Choisissez votre niveau de pixellisation. \nPlus la valeur numérique sera grande, plus l'image sera pixellisée. \n")
          
        if pixelValueString.isdigit() == True :
        
            pixelValue = int(pixelValueString)
            
            # Si la valeur de pixellisation est trop grande (supérieur soit à la hauteur, soit à la largeur de l'image), alors cela créera une erreur.
            # On redemande donc à l'utilisateur de chosir une nouvelle valeur.
            if pixelValue < widthF and pixelValue < heightF and pixelValue > 0:
            
                intVerification1 = True
                    
            else:
                    
                print("Je suis désolé chère personne, mais cette valeur de pixellisation est trop grande (ou trop petite si inférieure ou égale à 0).\nIl faut qu'elle soit inférieure à la hauteur et à la largeur de votre image.\nRéinitialisation du choix.\n")
            
        elif pixelValueString == "" :
            
            pixelValue = 10
            intVerification1 = True
            
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")
            
    # On crée une nouvelle image de même dimension que la première pour éviter les problèmes.
    newImage = Image.new("RGB", (widthF, heightF))
    
    # On parcourt tous les pixels avec un pas de pixelValue en largeur et hauteur.
    # Si pixelValue = 3 par exemple, on prendra le pixel 0, puis 3, puis 6...
    for i in range (0, widthF, pixelValue):

        for j in range (0, heightF, pixelValue) :
        
            Colors = [0, 0, 0]
            
            # On parcourt tous les pixels dans le carré de côté pixelValue, et dont le coin supérieur gauche est le pixel de coordonnées (i, j).
            for li in range (pixelValue):
               
                for lj in range (pixelValue):
                    
                    # Si le pixel est dans l'image (donc inférieur à sa largeur et à sa hauteur).
                    if (i + li) < widthF and (j + lj) < heightF :
                        
                        # Alors on prend sa composante rouge, et on l'ajoute à l'indice 1 d'un tableau stockant la somme de toutes les composantes rouges dans l'indice 1.
                        # On fait de même avec les 2 autres composantes et avec les indices suivants.
                        newColors = imageF.getpixel((i + li, j + lj))
                        Colors = [Colors[0] + newColors[0], Colors[1] + newColors[1], Colors[2] + newColors[2]]
                    
                    # Sinon, on ajoute au tableau les valeurs du pixel le plus proche de lui que est dans l'image; celui de coordonnées (i, j).
                    else:
                        
                        newColors = imageF.getpixel((i, j))
                        Colors = [Colors[0] + newColors[0], newColors[1] + Colors[1], Colors[2] + newColors[2]]
                        
            # On fait la moyenne de toutes les sommes en divisant par le nombre de pixel analysé, c'est à dire "pixelValue**2"
            # On obtient alors les valeurs d'un pixel moyen de tous les autres pixels du carré.
            # On utilise int() pour chaque valeur car chaque composante doit être une valeur entière.
            middleColors = [int(Colors[0]/(pixelValue**2)), int(Colors[1]/(pixelValue**2)), int(Colors[2]/(pixelValue**2))]

            
            # On parcourt chaque pixel du carré précédemment analysé.
            for li2 in range (pixelValue):
                
                for lj2 in range (pixelValue):
                    
                    if (i + li2) < widthF and (j + lj2) < heightF :
                        
                        # On lui assigne la valeur du pixel moyen du carré.
                        # Cela donnera un effet de pixellisation à l'image.
                        newImage.putpixel((i + li2, j + lj2), (middleColors[0], middleColors[1], middleColors[2]))
                    
    
    return newImage




def lum(widthF, heightF, imageF):
    """
        Cette fonction permet d'éclaircir ou d'obscurcir une image selon le choix de l'utilisateur.
    """
    
    # Boucle de vérification d'input. 
    intVerification1 = False
    
    while intVerification1 == False :
        
        choiceString = input("Que Souhaitez - vous ? \n\n1. Eclaircir l'image \n2. Obscurcir l'image \n")
          
        if choiceString.isdigit() == True :
        
            choice = int(choiceString)
            
            if choice <= 2 and choice > 0:
            
                intVerification1 = True
                    
            else:
                    
                print("Je suis désolé chère personne, mais cette valeur ne correspond à rien ^^'.\nRéinitialisation du choix.\n")
            
        elif choiceString == "" :
            
            choice = 1
            intVerification1 = True
            
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")
            
    # Boucle de vérification d'input.
    intVerification2 = False
    
    while intVerification2 == False :
        
        intToAddString = input("Oui, excusez-moi, j'aurai besoin d'une valeur numérique pour ça s'il vous plaît :). \nPlus elle sera grande plus votre image sera modifiée :o. \n")
        
        if intToAddString.isdigit() == True :
        
            intToAdd = int(intToAddString)
            
            if intToAdd <= 255 and intToAdd > 0:
            
                intVerification2 = True
                    
            else:
                
                print("Désolé, mais la valeur maximale est 255. Elle vous donnera une image toute blanche ou toute noire selon vos choix ^^'.\nEt la valeur minipale est 1 :p\nRéinitialisation du choix.\n")
            
        elif intToAddString == "" :
            
            intToAdd = 100
            intVerification2 = True
            
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")

    # Si l'utilisateur a choisi un effet d'obscurcissement, on prendra l'opposé de la valeur qu'il a choisi, ce qui donnera cet effet.
    if choice == 2:
        
        intToAdd = - intToAdd
    
    # On parcout chaque pixel de l'image.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            # On ajoute à chaque composante la valeur d'illumination / d'obscurcissement ce qui donnera l'effet voulu.
            imageF.putpixel((i, j), (Colors[0] + intToAdd, Colors[1] + intToAdd, Colors[2] + intToAdd))
            
    return imageF



def color(widthF, heightF, imageF):
    """
        Cette fonction permet de coloriser une image de la couleur choisie par l'utilisateur.
    """
    
    # Boucle de vérification d'input.
    intVerification2 = False
    
    while intVerification2 == False :
        
        intToAddString = input("Oui, excusez-moi, j'aurai besoin d'une valeur numérique pour ça s'il vous plaît :). \nPlus elle sera grande plus votre image sera teintée d'une couleur :o. \n")
        
        if intToAddString.isdigit() == True :
        
            intToAdd = int(intToAddString)
            
            if intToAdd <= 255 and intToAdd > 0:
            
                intVerification2 = True
                    
            else:
                
                print("Désolé, mais la valeur maximale est 255. Elle vous donnera une image de la couleur choisie ^^'.\nEt la valeur minipale est 1 :p\nRéinitialisation du choix.\n")
            
        elif intToAddString == "" :
            
            intToAdd = 100
            intVerification2 = True
            
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")
    
    
    # Boucle de vérification d'input.
    intVerification1 = False
    
    while intVerification1 == False :
        
        colorToAddString = input("Super ;). Maintenant il vous faut une couleur qui sera mise en avant :o.\nTapez le nombre correspondant à la couleur: \n\n1. - Rouge \n2. - Vert \n3. - Bleu \n4. - Cyan \n5. - Magenta \n6. - Jaune \n\n")
        
        if colorToAddString.isdigit() == True :
        
            colorToAdd = int(colorToAddString) - 1
            
            if colorToAdd <= 6 and colorToAdd > 0:
            
                intVerification1 = True
                    
            else:
                
                print("Désolé, mais cette valeur ne correspond à rien :p\nRéinitialisation du choix.\n")
            
        elif colorToAddString == "" :
            
            colorToAdd = 0
            intVerification1 = True
            
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")


    # On parcout chaque pixel de l'image.    
    for i in range (widthF) :

        for j in range (heightF) :
            
            # On crée un tableau stockant les valeurs des composantes du pixel qu'on modifie.
            rgbValue = imageF.getpixel((i, j))
            Colors = [rgbValue[0], rgbValue[1], rgbValue[2]]
            
            # Si la couleur choisie est une couleur primaire.
            if colorToAdd <= 2 :
                
                for colorIndice in range (3) :
                    
                    # On ajoute la valeur de colorisation à la couleur correspondante
                    if colorIndice == colorToAdd:
                    
                        Colors[colorIndice] = Colors[colorIndice] + intToAdd

                    
                    # Et on soustrait la moitié de la valeur de colorisation aux deux autres composantes.
                    else:
                    
                        Colors[colorIndice] = Colors[colorIndice] - int(intToAdd/2)
            
            # Si la couleur choisie est secondaire.
            else:
                
                # On enlève 3 pour alors obtenir la seule composante à laquelle il ne faudra rien ajouter (la seule pour laquelle il faudra soustraire la moitié de la valeur de colorisation).
                colorToSubtract = colorToAdd - 3
                
                for colorIndice in range (3) :
                    
                    # On soustrait la moitié de la valeur de colorisation à la seule composante ne formant pas la couleur correspondante.
                    if colorIndice == colorToSubtract:
                    
                        Colors[colorIndice] = Colors[colorIndice] - int(intToAdd/2)

                    # On ajoute la valeur de colorisation aux composantes formant la couleur correspondante.
                    else:
                    
                        Colors[colorIndice] = Colors[colorIndice] + intToAdd
            
            # On assigne les valeurs précédentes au pixel.
            imageF.putpixel((i, j), (Colors[0], Colors[1], Colors[2] ))
                

    return imageF



def color512(widthF, heightF, imageF):
    """
        Cette fonction permet de créer une image contenant uniquement un certain nombre de composantes colorimétriques choisis par l'utilisateur.
    """
    
    # Boucle de vérification d'input.
    intVerification1 = False
    
    while intVerification1 == False :
        
        numberOfColorString =input("Vous allez choisir un nombre limité de composantes colorimétriques. Ces composantes seront les seules à apparaître dans l'image. \n")
        
        if numberOfColorString.isdigit() == True :
        
            numberOfColor = int(numberOfColorString) - 1
            
            if numberOfColor <= 254 and numberOfColor > 0:
            
                intVerification1 = True
                    
            else:
                
                print("Désolé, mais cette valeur est soit trop grande (le maximum étant 254 :) soit trop petite ^^'(inférieure à 0).\n")
            
        elif numberOfColorString == "" :
            
            numberOfColor = 8
            intVerification1 = True
            
        else :
            
            print ("Mais... Vous n'avez même pas tapé un nombre T_T \n")
    
    # On calcule la différence entre 2 intervalles. On utilise int() car les valeurs RGB doivent être entières.
    interval = int(255/numberOfColor)
    # On crée un tableau qui contiendra tous les intervalles existants.
    composantList = [0]
    # Cette varirable stocke le nombre d'intervalles déjà crées.
    intervalCreated = 0
    
    # Cette boucle ajoute au tableau tous les intervalles.
    # Pour chaque intervalle:
    for k in range (numberOfColor):
        
        # Il ajoute 1 au nombre d'intervalles crées. Par exemple si on veut 6 intervalles et qu'on est au 3e, il sera ici égal à 3.
        intervalCreated = intervalCreated + 1
        # L'interval à ajouté est détermine par le nombre d'intervallle crée et la différence entre chaque intervalle.
        # Dans l'exemple précédent, puisqu'on à 6 intervalles, la différence d'intervalle est 42. Puisqu'on est au 3e intervalles, alors le 3e intervalles sera 42*3 = 126.
        intervalToAppend = interval*intervalCreated
        
        # Si l'intervalle surpasse 255, ce qui est possible car on utilise des valeurs arrondies, alors il sera remplacé par l'intervalle 255.
        if intervalToAppend > 255:
            
            intervalToAppend = 255
            
        # On ajoute cet intervalle au tableau des intervalles.    
        composantList.append(intervalToAppend)
    
    
    # Pour chaque pixel de l'image.
    for i in range (widthF):
        
        for j in range (heightF):
            
            rgbValue = imageF.getpixel((i, j))
            Colors = [rgbValue[0], rgbValue[1], rgbValue[2]]
                
                
            # Cette boucle permet de vérifier l'intervalle inférieur le plus proche de la valeur colorimùétrique en cours de test.
            # Elle s'effectue pour chaque composante colorimétrique.
            for colorToTest in range (3):
                
                # On affecte la valeur minimum néf=gative qu'il peut exister entre 2 intervalles.
                maximumNegativeValue = -255
                # Par défaut, l'intervalle à assigner à la composante colorimétrique est à 0.
                intervalToAssign = 0
                
                # Pour chaque intervalle dans le tableau composantList:
                for intervalToTest in range (numberOfColor):
                    
                    # On prend la valeur à tester correspondant à l'élément ayant l'indice numberOfColor du tableau composantList.
                    # C'est à dire la valeur de l'intervalle à tester.
                    # valueToTest est la différence entre cette valeur, et la valeur de la composante colorimétrique originelle du tableau.
                    valueToTest = composantList[intervalToTest] - Colors[colorToTest]
                    
                    # Si cette différence est plus grande que la valeur précédente, tout en restant positive, alors l'intervalle actuel est sauvegardé comme étant le plus proche jusqu'au prochain test.
                    # La différence est également sauvegardé pour la prochaine valeur à tester.
                    if maximumNegativeValue < valueToTest and valueToTest <= 0:
                            
                        intervalToAssign = composantList[intervalToTest]
                        maximumNegativeValue = valueToTest
                
                # On a donc obtenu l'intervalle le plus proche.
                # On l'assigne à la composante colorimétrique en cours de modification.
                Colors[colorToTest] = intervalToAssign
            
            # On assigne chaque composante colorimétrique obtenue au pixel que l'on était en train de tester.
            imageF.putpixel((i, j), (Colors[0], Colors[1], Colors[2] ))
                
    return imageF
  
  
                    
def negativeColors(widthF, heightF, imageF):
    """
        Cette fonction fournie le négatif de l'image fournie.
    """
    
    # Pour chaque pixel de l'image.
    for i in range (widthF) :

        for j in range (heightF) :
        
            Colors = imageF.getpixel((i, j))
            # On soustrait à chaque composante colorimétrique 255, ce qui aura poureffet de donner le négatif du pixel.
            # On ajoute un - devant chaque composante colorimétrique pour obtenir une valeur positive.
            Colors = [-(Colors[0] - 255), -(Colors[1] - 255), -(Colors[2] - 255)]
            imageF.putpixel((i, j), (Colors[0], Colors[1], Colors[2]))
            
    return imageF



menu()
