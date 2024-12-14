import math 
def tt():
    print("Bienvenue khoya")
    print("1) Calculer pourcentage")
    print("2) Pythagore")
    print("3) Thales")
    print("4) Calculer Ratio    ")
    print("5) Programme simple")
    ans = input("jveux: ")
    if (ans == "1"):
        def calculer_pourcentage(valeur, total):
            if total == 0:
                return "Le total ne peut pas être zéro."
            pourcentage = (valeur / total) * 100
            return pourcentage
        valeur = float(input("Entrez la valeur : "))
        total = float(input("Entrez le total : "))
        pourcentage = calculer_pourcentage(valeur, total)
        print("Le pourcentage est : " + str(pourcentage) + " %")
    if (ans == "2"):
        print("1) Théorème")
        print("2) Réciproque")
        print("3) Contraposé")
        askPythagore = input("jveux: ")
        if (askPythagore == "1"):
            def calculer_cote(a=None, b=None, c=None):
                if a is None:  
                    a = math.sqrt(c**2 - b**2)
                    return a
                elif b is None:  
                    b = math.sqrt(c**2 - a**2)
                    return b
                elif c is None:  
                    c = math.sqrt(a**2 + b**2)
                    return c
            choix = input("calculer a, b ou c ?: ")
            if choix == "c":
                a = float(input("Entrez la longueur du côté a : "))
                b = float(input("Entrez la longueur du côté b : "))
                c = calculer_cote(a=a, b=b)
                print("Théorème de Pythagore :")
                print("Si a = " + str(a) + " et b = " + str(b) + ", alors l'hypoténuse c est calculée par la formule c = √(a² + b²).")
                print("Donc c = √(" + str(a) + "² + " + str(b) + "²) = " + str(round(c, 2)))
                print("L'hypoténuse c est : " + str(round(c, 2)))

            elif choix == "a":
                b = float(input("Entrez la longueur du côté b : "))
                c = float(input("Entrez la longueur de l'hypoténuse c : "))
                a = calculer_cote(a=None, b=b, c=c)
                print("Théorème de Pythagore :")
                print("Si b = " + str(b) + " et c = " + str(c) + ", alors le côté a est calculé par la formule a = √(c² - b²).")
                print("Donc a = √(" + str(c) + "² - " + str(b) + "²) = " + str(round(a, 2)))
                print("Le côté a est : " + str(round(a, 2)))

            elif choix == "b":
                a = float(input("Entrez la longueur du côté a : "))
                c = float(input("Entrez la longueur de l'hypoténuse c : "))
                b = calculer_cote(a=a, b=None, c=c)
                print("Théorème de Pythagore :")
                print("Si a = " + str(a) + " et c = " + str(c) + ", alors le côté b est calculé par la formule b = √(c² - a²).")
                print("Donc b = √(" + str(c) + "² - " + str(a) + "²) = " + str(round(b, 2)))
                print("Le côté b est : " + str(round(b, 2)))
        if (askPythagore == "2"):
                def reciproque_pythagore(a, b, c):
                    if a**2 + b**2 == c**2:
                        return True
                    else:
                        return False
                a = float(input("Entrez la longueur du côté a : "))
                b = float(input("Entrez la longueur du côté b : "))
                c = float(input("Entrez la longueur de l'hypoténuse c : "))
                if reciproque_pythagore(a, b, c):
                    print("Réciproque de Pythagore :")
                    print("Si a = " + str(a) + ", b = " + str(b) + " et c = " + str(c) + ", vérifions si la somme des carrés de a et b est égale à c².")
                    print("Nous avons : " + str(a) + "² + " + str(b) + "² = " + str(a**2) + " + " + str(b**2) + " = " + str(a**2 + b**2) + ", et c² = " + str(c**2) + ".")
                    print("D'après le théoreme de pythagore ce triangle est rectangle.")
                else:
                    print("Réciproque de Pythagore :")
                    print("Si a = " + str(a) + ", b = " + str(b) + " et c = " + str(c) + ", vérifions si la somme des carrés de a et b est égale à c².")
                    print("Nous avons : " + str(a) + "² + " + str(b) + "² = " + str(a**2) + " + " + str(b**2) + " = " + str(a**2 + b**2) + ", et c² = " + str(c**2) + ".")
                    print("D'apres la réciproque du théorème de Pythagore le triangle ABC est Rectangle.")

        if (askPythagore == "3"):
                def contrapose_pythagore(a, b, c):
                    if a**2 + b**2 != c**2:
                        return True  
                    else:
                        return False
                a = float(input("Entrez la longueur du côté a : "))
                b = float(input("Entrez la longueur du côté b : "))
                c = float(input("Entrez la longueur de l'hypoténuse c : "))
                if contrapose_pythagore(a, b, c):
                    print("Contraposée de Pythagore :")
                    print("Si a = " + str(a) + ", b = " + str(b) + " et c = " + str(c) + ", vérifions si la somme des carrés de a et b est différente de c².")
                    print("Nous avons : " + str(a) + "² + " + str(b) + "² = " + str(a**2 + b**2) + ", et c² = " + str(c**2) + ".")
                    print("Les valeurs vérifient la contraposée du théorème de Pythagore (c'est un contre-exemple).")
                else:
                    print("Contraposée de Pythagore :")
                    print("Si a = " + str(a) + ", b = " + str(b) + " et c = " + str(c) + ", vérifions si la somme des carrés de a et b est différente de c².")
                    print("Nous avons : " + str(a) + "² + " + str(b) + "² = " + str(a**2 + b**2) + ", et c² = " + str(c**2) + ".")
                    print("Les valeurs ne vérifient pas la contraposée du théorème de Pythagore.")        
    if (ans == "3"):
            def theoreme_thales(a, b, c, d):
                print("Théorème de Thales")
                print("On a les côtés du premier triangle : {} et {}, et les côtés du second triangle : {} et {}.".format(a, b, c, d))
                print("On va maintenant vérifier si le rapport des côtés du premier triangle ({}/{}) est égal au rapport des côtés du second triangle ({}/{}).".format(a, b, c, d))
                if a / b == c / d:
                    print("Les rapports sont égaux : {}/{} = {}/{}. Cela signifie que les triangles sont semblables.".format(a, b, c, d))
                    return True  
                else:
                    print("Les rapports ne sont pas égaux : {}/{} !={}/{}. Les triangles ne sont pas semblables.".format(a, b, c, d))
                    return False  
            def reciproque_thales(a, b, c, d):
                print("Réciproque du Théorème de Thales")
                print("On a les segments de longueur : {}, {}, {}, {}.".format(a, b, c, d))
                print("On va vérifier si les segments {}/{} et {}/{} sont proportionnels.".format(a, b, c, d))
                if a / b == c / d:
                    print("Les segments sont proportionnels : {}/{} = {}/{}. Cela signifie qu'il existe un parallèle qui coupe les deux côtés.".format(a, b, c, d))
                    return True  
                else:
                    print("Les segments ne sont pas proportionnels : {}/{} !={}/{}. Il n'existe pas de parallèle.".format(a, b, c, d))
                    return False  

            def contraposée_thales(a, b, c, d):
                print("\n--- Contraposée du Théorème de Thales ---")
                print("On a les segments de longueur : {}, {}, {}, {}.".format(a, b, c, d))
                print("On va vérifier si les segments {}/{} et {}/{} sont non proportionnels.".format(a, b, c, d))
                if a / b != c / d:
                    print("Les segments sont non proportionnels : {}/{} !={}/{}. Cela signifie qu'il n'existe pas de parallèle.".format(a, b, c, d))
                    return True  
                else:
                    print("Les segments sont proportionnels : {}/{} = {}/{}. Il existe un parallèle.".format(a, b, c, d))
                    return False  
            print("1) Théorème")
            print("2) Réciproque")
            print("3) Contraposé")
            choix = input("jveux: ").lower()
            if choix == "1":
                a = float(input("Entrez la longueur du côté a : "))
                b = float(input("Entrez la longueur du côté b : "))
                c = float(input("Entrez la longueur du côté c : "))
                d = float(input("Entrez la longueur du côté d : "))
                if theoreme_thales(a, b, c, d):
                    print("D'après le theoreme de Thales on a  : Les triangles sont semblables et les rapports des côtés sont égaux.")
                else:
                    print("D'apres la réciproque du theoreme de Thales on a : Les rapports des côtés ne sont pas égaux.")

            elif choix == "2":
                a = float(input("Entrez la longueur du côté a : "))
                b = float(input("Entrez la longueur du côté b : "))
                c = float(input("Entrez la longueur du côté c : "))
                d = float(input("Entrez la longueur du côté d : "))
                if reciproque_thales(a, b, c, d):
                    print("D'apres la réciproque du théoreme de Thales on a  : Un parallèle existe, les segments sont proportionnels.")
                else:
                    print("La réciproque de Thales n'est pas vérifiée : Un parallèle n'existe pas, les segments ne sont pas proportionnels.")

            elif choix == "contraposée":
                a = float(input("Entrez la longueur du côté a : "))
                b = float(input("Entrez la longueur du côté b : "))
                c = float(input("Entrez la longueur du côté c : "))
                d = float(input("Entrez la longueur du côté d : "))
                if contraposée_thales(a, b, c, d):
                    print("La contraposée de Thales est vérifiée : Il n'existe pas de parallèle, les segments ne sont pas proportionnels.")
                else:
                    print("La contraposée de Thales n'est pas vérifiée : Un parallèle existe, les segments sont proportionnels.")
    if (ans == "4"):
        def calculer_ratio(valeur1, valeur2):
            if valeur2 == 0:
                print("Erreur : La valeur2 ne peut pas être zéro, division impossible.")
                return None
            else:
                ratio = valeur1 / valeur2
                print("Nous avons deux valeurs : {} et {}.".format(valeur1, valeur2))
                print("Le calcul du ratio consiste à diviser la première valeur par la deuxième valeur.")
                print("Le ratio est donc : {}/{} = {:.2f}".format(valeur1, valeur2, ratio))
                return ratio
        valeur1 = float(input("Entrez la première valeur : "))
        valeur2 = float(input("Entrez la deuxième valeur : "))
        calculer_ratio(valeur1, valeur2)
    if (ans == "5"):
        nbrInit = int(input("Choisis un nombre: "))
        etapes = []
        print("Ecris pour arreter blud.")
        while True:
            operation = input("Opération : ")
            if operation.lower() == "c":
                break
            etapes.append(operation)
        resultat = nbrInit
        for etape in etapes:
            if etape.startswith("+"):
                resultat += int(etape[1:])
            elif etape.startswith("-"):
                resultat -= int(etape[1:])
            elif etape.startswith("*"):
                resultat *= int(etape[1:])
            elif etape.startswith("/"):
                resultat //= int(etape[1:])
        print("Réponse : " + str(resultat))
tt()