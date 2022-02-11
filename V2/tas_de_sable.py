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

###############################################
# initialisation de la fenêtre
root = tk.Tk()
root.title("tas de sable")
cTableau = tk.Canvas(root, height=500, width=500, bg="white")
cTableau.grid()
###############################################

def chooseConfig():
    """"Cette fonction eneleve les boutons de bases pour mettre a la place les autres bouttons
    a propos des configurations"""
    boperation.grid_remove()
    bconfig.grid_remove()
    bsauvegarde.grid_remove()
    


###############################################
# Création des Boutons
bconfig = tk.Button(root, text="Config", command = chooseConfig)
bconfig.grid(column = 0, row = 0)

brandom = tk.Button(root, text="Random")

bpilecentree = tk.Button(root, text="Pile centree")

bmaxstable = tk.Button(root, text="Max Stable")

bidentity = tk.Button(root, text="Identity")

boperation = tk.Button(root, text="Operation")
boperation.grid(column = 0, row = 1)

bsauvegarde = tk.Button(root, text="Sauvegarder la config")
bsauvegarde.grid(column = 0, row = 2)
###############################################


###############################################
def tableauVide():
    """Cette fonction affiche un tableau vide en utilisant des rectangle vide
    et des diez pour le délimiter. La longueur des carreaux s'adapte en
    fonction du nombre de carreaux demandé par l'utilisateur en amont."""
    global nombreCarreaux, guiSable
    longueurCarreaux = (int(480 // nombreCarreaux)) / 2 
    x = 10
    y = 10
    sousListeGuiSable = []
    for i in range(0, nombreCarreaux):
        for j in range(0, nombreCarreaux):
            Sable = cTableau.create_rectangle((x + longueurCarreaux, y + longueurCarreaux) (x - longueurCarreaux, y - longueurCarreaux))
            sousListeGuiSable.append(Sable)
        guiSable.append(sousListeGuiSable)
        sousListeGuiSable = []


# Boucle Principale
root.mainloop()