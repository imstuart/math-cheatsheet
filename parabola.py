def rs():
    print("Selem tu veux quoi ?")
    print("1) Formules Aires figures usuelles")
    print("2) Formules Volumes figures")
    print("3) Formules Trigonométries")
    print("4) Théorèmes")
    print("5) Identité Remarquable")
    print("6) Fonction")
    print("7) Statistiques")
    print("8) Ensemble de nbr")
    Jveux = input("Chiffre: ")
    # Formules figures usuelles askip
    if (Jveux == "1"):
        print("1) Aire Triangle")
        print("2) Aire Triangle Rectangle")
        print("3) Aire Carré")
        print("4) Aire Rectangle")
        print("5) Aire Parallélogramme")
        print("6) Aire Disque")
        JveuxFormulesFigures = input("Quels formules ?")
        if (JveuxFormulesFigures == "1"):
            print("Formules Triangle: b*h / 2 (base * hauteur / 2)")
        if (JveuxFormulesFigures == "2"):
            print("Formules Triangle Rectangle: a * b / 2 (coté * base / 2)")
        if (JveuxFormulesFigures == "3"):
            print("Formules Carré: c*c (coté * coté)")
        if (JveuxFormulesFigures == "4"):
            print("Formules Rectangle: L * l (longeur * largeur)")
        if (JveuxFormulesFigures == "5"):
            print("Formules Parallélogramme: b * h (base * hauteur)")
        if (JveuxFormulesFigures == "6"):
            print("Formules Disque: pi * R^2 (pi * Rayon au carré)")


    if (Jveux == "2"): # Volume
        print("1) Volume Parallélépipède rectangle")
        print("2) Volume Cube")
        print("3) Volume Cylindre") 
        print("4) Volume Prisme")
        print("5) Volume Cone de révolution")
        print("6) Volume Pyramide") ## ok werenoi
        print("7) Volume Boule") ## Gros fiak
        JveuxAireFigures = input("Quels formules ?")
        if (JveuxAireFigures == "1"):
            print("Formules Parallélépipède rectangle: L * l * h (Longueur * largeur * 2)")
        if (JveuxAireFigures == "2"):
            print("Formules Cube: v = c^3 (coté au cube)")
        if (JveuxAireFigures == "3"):
            print("Formules Cylindre: v = aire base * h")
            print("                   v = pi * R^2 * h")
        if (JveuxAireFigures == "4"):
            print("Formules Prisme: v = aire base * h")
        if (JveuxAireFigures == "5"):
            print("Formules Cone de révolution: v = aire base * h /3")
            print("                             v = pi * R^2 * h / 3")
        if (JveuxAireFigures == "6"):
            print("Formules Pyramide: v = aire base * h / 3")
        if (JveuxAireFigures == "7"):
            print("Formules Boule: v = 4/3 * pi * R^3")
    ## Trigo
    if (Jveux == "3"):
        print("1) Cos / Arccos")
        print("2) Sin / Arcsin")
        print("3) Tan / Arctan")
        JveuxFormulesTrigo = input("Quels formules ?")
        if (JveuxFormulesTrigo == "1"):
            print("cos(x) = adjacent / hypoténuse")
            print("arccos(x) (en gros l'inverse)")
        if (JveuxFormulesTrigo == "2"):
            print("sin(x) = opposé / hypoténuse")
            print("arcsin(x) (en gros l'inverse)")
        if (JveuxFormulesTrigo == "3"):
            print("tan(x) = sin(x) / cos(x) = opposé / adjacent")  


    ##Théorème de python ou koi la ahahah aze
    if (Jveux == "4"):
        print("1) Pythagore")
        print("2) Thalès")
        JveuxTheoreme = input("Quel théorème ?")    
        if (JveuxTheoreme == "1"):
            print("1) Théoreme de Pyt")
            print("2) Réciproque de Pyt")
            print("3) Contraposé de pyt")
            jveuxthmpyt = input("Je veux:")
            if (jveuxthmpyt == "1"):
                print("Dans un triangle rectangle, le carré de la longueur de l'hypoténuse est égal à la somme des carrés des longueurs des deux autres côtés")
                print("Formule : h² = a² + b² ,h = hypothénuse ")
            if (jveuxthmpyt == "2"):
                print("Si, dans un triangle, le carré de la longueur d'un côté est égal à la somme des carrés des longueurs des deux autres côtés, alors ce triangle est rectangle.")
                print("Si c² = a² + b², alors le triangle est rectangle")
            if (jveuxthmpyt == "3"):
                print("Si, dans un triangle, le carré de la longueur d'un côté n'est pas égal à la somme des carrés des longueurs des deux autres côtés, alors ce triangle n'est pas rectangle.")
                print("Si c² ≠ a² + b², alors le triangle n'est pas rectangle")    
        if (JveuxTheoreme == "2"):
            print("1) Théoreme de Thal")
            print("2) Réciproque de Thal")
            print("3) Contraposé de Thal")
            jveuxthmthal = input("Je veux: ")
            if (jveuxthmthal == "1"):
                print("Si deux droites sont coupées par deux droites parallèles, alors les longueurs des segments correspondants sont proportionnelles.")
                print("Formule : (AB / A'B') = (AC / A'C') = (BC / B'C').")
            if (jveuxthmthal == "2"):
                print("Si les longueurs des segments sur deux droites coupées par deux droites parallèles sont proportionnelles, alors ces deux droites sont parallèles.")
                print("Condition : Si (AB / A'B') = (AC / A'C'), alors les droites sont parallèles.")
            if (jveuxthmthal == "3"):
                print("Calcul de longueurs inconnues dans des triangles ou des figures géométriques")
                print("Vérification du parallélisme entre deux droites") 
    if (Jveux == "5"):
      print("1ere = (a + b)² = a² + 2ab + b²")
      print("2eme = (a - b)² = a² - 2ab + b²") 
      print("3eme = (a + b)(a - b) = a² - b²")
    if (Jveux == "6"):
        print("1) Definition")
        print("2) Vocabulaire")
        print("3) Type de fonction")
        jveuxFonction = input("Jveux: ")
        if (jveuxFonction == "1"):
            print("Une fonction associe à chaque élément (x) d'un ensemble de départ un unique élément (y) d'un ensemble d'arrivée.")
            print("Notation : f(x)")
        if (jveuxFonction == "2"):
            print("""
Vocabulaire:
- Domaine de définition : Ensemble des valeurs de (x) pour lesquelles f(x) existe.
- Image : Ensemble des valeurs prises par f(x).
- Racines : Valeurs de (x) pour lesquelles f(x = 0).
- Maximum et Minimum : Valeurs extrêmes prises par f(x) sur un intervalle donné.
            """)
        if (jveuxFonction == "3"):
            print("""
Fonctions usuelles :
- Fonction linéaire : f(x) = a*x.
- Fonction affine : f(x) = a*x + b.

            """)
    if (Jveux == "7"):
        print("1) Etendue")
        print("2) Médiane")
        print("3) Moyenne")
        print("4) Quartiles")
        jveuxStat = input("Jveux: ")
        if (jveuxStat == "1"):
            print("Etendue = Max - Min")
        if (jveuxStat == "2"):
            print("Valeur du milieu si impaire")
            print("M= Valeur tot / 2 > prendre la valeur approché")
        if (jveuxStat == "3"):
            print("X= additionne tt les valeurs / effectif total")
        if (jveuxStat == "4"):
            print("Calculer la médiane, diviser par deux pour avoir 4 part égale noté Q1, Q2, Q3 et Q4")
    if (Jveux == "8"):

        print("N < Z < D < Q < R")
        print("1) Nombre Naturel (N)")
        print("2) Nombre Entier (Z)")
        print("3) Nombre Décimaux (D)")
        print("4) Nombre Rationel (Q)")
        print("5) Nombre Réel (R)")
        print("6) Regle (App / Inc.)")
        ensNbr = input("Jveux")
        if (ensNbr == "1"):
            print("Ensemble des entiers positifs à partir de zéro (0, 1, 2, 3 Soleil....)")
        if (ensNbr == "2"):
            print("Ensemble des entiers positifs, négatifs et zéro (-2, -1, 0, 1, 2...)")
        if (ensNbr == "3"): 
            print("Ensemble des nombres flotant (a virgule) (1,69, 0,69, 1/3...) ")
        if (ensNbr == "4"):
            print("Ensemble des nombres qui peuvent être écrits sous forme de fraction")
        if (ensNbr == "5"):
            print("Ensemble des nombres qui inclut les rationnels et les irrationnels (pi, racine carré en gros tt)")
        if (ensNbr == "6"):
            print("Appartient (€)= fait partie d'un ensemble")
            print("Appartient (!€) € barré = ne fait pas partie d'un ensemble")
            print("Inclut (C) = ensemble fait partie d'un autre ensemble ")
            print("N'inclut pas (!C) C barré = ensemble qui ne fait pas partie d'un autre ensemble ")

rs()