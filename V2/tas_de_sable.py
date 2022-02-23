###############################################
# Groupe LDDBI
# Benjamin PREHAUD
# Arthur VINCENS
# Valentin JACQUIN
# https://github.com/uvsq22102587/SandProject
###############################################
# import des librairies
import tkinter as tk
###############################################
# Initialisation des variables
nombreCarreaux, guiSable = 49, []
###############################################
# initialisation de la fenêtre
root = tk.Tk()
root.title("tas de sable")
cTableau = tk.Canvas(root, height=500, width=500, bg="white")
cTableau.grid(column=1, row=0, rowspan=10)
###############################################

def chooseConfig(page):
    """"Cette fonction eneleve les boutons de bases pour mettre a la place les autres bouttons
    a propos des configurations"""
    boperation.grid_remove()
    bconfig.grid_remove()
    bsauvegarde.grid_remove()
    if page == "Config":
        brandom.grid(column=0,row=0)
        bidentity.grid(column=0,row=1)
        bmaxstable.grid(column=0,row=2)
        bpilecentree.grid(column=0,row=3)
        bRetour.grid(column=0, row=4)
    elif True:
        pass
    
def retour():
    brandom.grid_remove()
    bidentity.grid_remove()
    bmaxstable.grid_remove()
    bpilecentree.grid_remove()
    bRetour.grid_remove()
    boperation.grid(column=0, row=1)
    bconfig.grid(column=0, row=0)
    bsauvegarde.grid(column=0, row=2)
    
###############################################
# Création des Boutons
bconfig = tk.Button(root, text="Charger Config", command = lambda : chooseConfig(page="Config"))
bconfig.grid(column = 0, row = 0)

brandom = tk.Button(root, text="Aléatoire")

bpilecentree = tk.Button(root, text="Pile centree")

bmaxstable = tk.Button(root, text="Max Stable")

bidentity = tk.Button(root, text="Identity")

boperation = tk.Button(root, text="Operation")
boperation.grid(column=0, row=1)

bRetour = tk.Button(root, text="retour", command=retour, background="red")

bsauvegarde = tk.Button(root, text="Sauvegarder la config")
bsauvegarde.grid(column = 0, row = 2)
###############################################


###############################################
def tableauVide():
    """Cette fonction affiche un tableau vide en utilisant des rectangle vide
    et des diez pour le délimiter. La longueur des carreaux s'adapte en
    fonction du nombre de carreaux demandé par l'utilisateur en amont."""
    global nombreCarreaux, guiSable
    longueurCarreaux = (500 / nombreCarreaux) / 2
    espacement = 500 - (longueurCarreaux * nombreCarreaux * 2)
    print(espacement)
    while espacement < 20:
        longueurCarreaux -= 0.0001
        espacement = 500 - (longueurCarreaux * nombreCarreaux * 2)
    print(espacement)
    x = espacement
    y = 0
    # assert x - longueurCarreaux > 0 or y - longueurCarreaux > 0, "Il n'y a pas assez de carreaux dans la grille pour qu'elle soit affichée"
    sousListeGuiSable = []
    for i in range(0, nombreCarreaux):
        y += longueurCarreaux * 2
        x = espacement
        for j in range(0, nombreCarreaux):
            Sable = cTableau.create_rectangle((x + longueurCarreaux, y + longueurCarreaux), (x - longueurCarreaux, y - longueurCarreaux))
            sousListeGuiSable.append(Sable)
            x += longueurCarreaux * 2
        guiSable.append(sousListeGuiSable)
        sousListeGuiSable = []

# Boucle Principale
tableauVide()
root.mainloop()