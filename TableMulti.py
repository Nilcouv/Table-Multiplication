def table(nb,max=10):
    """Fonction affichant la table de multiplication du nombre entré

    table(nb, max)
    nb - le nombre multiplié
    max - le multiplicateur maximum"""
    #impression de la table
    loop_tm=0
    while loop_tm<max:
        loop_tm+=1
        print(nb,"*",loop_tm,"=", loop_tm * nb)
        

#Message de bienvenu
print("Bienvenu dans Multiplicator Table!")
# boucle maintenant le programme
loop_soft=True
while loop_soft:
    
    #début du programme    
    nb=int(input("entrez le nombre à multiplier : "))
    max=int(input("entrez le multiplicateur maximum : "))
    table(nb,max)

    #Recommencer?
    loop_menu=True
    while loop_menu:
        menuans=str(input("Voulez-vous entrez un nouveau nombre? (O/N) : "))
        if menuans=="O" or menuans=="o":
            loop_menu=False
            loop_soft=True
        elif menuans=="N" or menuans=="n":
            loop_menu=False
            loop_soft=False
        else:
            print("Votre réponse n'est pas valide. Veuillez entrer \"O\" ou \"N\".")

#Fin du programme
print("Bonne journée!")
input("Appuyez sur ENTRÉE pour fermer le programme.")
