from sys import stdin,stdout
input,print = stdin.readline,stdout.write
def main():
    print("    Bienvenue.\nEntrez ici les temps de recharge de vos attaques... (Exemple : 42769)\n")
    tpsRech = input()
    nbTours = sorted(list(map(int,list(tpsRech.rstrip("\n")))))
    nbAtt = len(nbTours)
    if nbAtt < 6:
        classe = [nbTours[rang] - rang for rang in range(nbAtt) if nbTours[rang] > rang]
        attLong = len(classe)
        if attLong == nbAtt: print("Vos attaques : " + tpsRech + "Sortez vos tomes !\nVous risquez malencontreusement de vous blesser lors d'une Frappe Désespérée ; essayez peut-être de changer l'attaque qui prend " + str(nbTours[classe.index(min(classe))]) + " tours à recharger.")
        else: print("Félicitations !\nVous n'encontrerez jamais la mésaventure d'une Frappe Désespérée.")
    else: print("Vous ne pouvez avoir plus de 5 attaques dans EvoCreo, jeune Padawan !")
main()