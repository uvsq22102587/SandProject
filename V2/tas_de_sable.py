<<<<<<< HEAD
###################################
# groupe LDDBI 1
=======
###############################################
# Groupe LDDBI
>>>>>>> 0ffbf7a8067676ffdc36edf2d657a28cb02e80d6
# Benjamin PREHAUD
# Arthur VINCENS
# Valentin JACQUIN
# https://github.com/uvsq22102587/SandProject
<<<<<<< HEAD
###################################


def chooseConfig():
    boperation.grid_remove()
    bconfig.grid_remove()

bconfig = tk.Button(root, text="Config", command = chooseConfig)
bconfig.grid(column = 0, row = 0)

boperation = tk.Button(root, text="Operation")
boperation.grid(column = 0, row = 1)

bsauvegarde = tk.Button(root, text="Sauvegarder la config")
bsauvegarde.grid(column = 0, row = 2)
=======
###############################################

# import des librairies
import tkinter as tk



root = tk.Tk()
root.title("tas de sable")
cTableau = tk.Canvas(root, height=500, width=500, bg="white")
cTableau.grid()
root.mainloop()




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
    
>>>>>>> 0ffbf7a8067676ffdc36edf2d657a28cb02e80d6
