###############################################
# Groupe LDDBI
# Benjamin PREHAUD
# Arthur VINCENS
# Valentin JACQUIN
# https://github.com/uvsq22102587/SandProject
###############################################
# Importation des librairies
import tkinter as tk
import random as rdm
###############################################
# Initialisation des variables
guiSable = []
dataSand = [[0 for i in range(0, 47)]for i in range(0, 47)]
couleur = ["white", "yellow", "green", "blue", "purple"]
###############################################
# initialisation de la fenêtre
root = tk.Tk()
root.title("tas de sable")
cTableau = tk.Canvas(root, height=499, width=499, bg="white")
cTableau.grid(column=1, row=1, rowspan=10)
###############################################
# Définition fonction gestion interface


def affichePage(page, op=True):
    """"Cette fonction enlève les boutons de bases pour mettre à la place
    les autres bouttons à propos des configurations.
    De plus elle permet de stocker le type d'opération choisi."""
    global lAffichePage, operationType
    print("Affiche page")
    enleverGrid()
    if op is not True:
        operationType = str(op)
    lAffichePage = tk.Label(text=page)
    lAffichePage.grid(column=1, row=0)
    if page == "Config pour Affichage":
        brandom.grid(column=0, row=1)
        bidentity.grid(column=0, row=2)
        bmaxstable.grid(column=0, row=3)
        bpilecentree.grid(column=0, row=4)
        bRetour.grid(column=0, row=5)
    elif page == "Operation":
        bAddition.grid(column=0, row=1)
        bSoustraction.grid(column=0, row=2)
        bAutomateEtape.grid(column=0, row=3)
        bAutomateComplet.grid(column=0, row=4)
        bRetour.grid(column=0, row=5)
    elif page == "Config pour Operation":
        brandomOp.grid(column=0, row=1)
        bidentityOp.grid(column=0, row=2)
        bmaxstableOp.grid(column=0, row=3)
        bpilecentreeOp.grid(column=0, row=4)
        bConfirmerOp.grid(column=0, row=5)
        bRetourOp.grid(column=0, row=6)
    elif page == "Principale":
        bconfig.grid(column=0, row=1)
        boperation.grid(column=0, row=2)
        bsauvegarde.grid(column=0, row=3)


def enleverGrid():
    print("EnleverGrid")
    lAffichePage.grid_remove()
    boperation.grid_remove()
    bconfig.grid_remove()
    bsauvegarde.grid_remove()
    brandom.grid_remove()
    bidentity.grid_remove()
    bmaxstable.grid_remove()
    bpilecentree.grid_remove()
    brandomOp.grid_remove()
    bidentityOp.grid_remove()
    bmaxstableOp.grid_remove()
    bpilecentreeOp.grid_remove()
    bRetour.grid_remove()
    bRetourOp.grid_remove()
    bAddition.grid_remove()
    bSoustraction.grid_remove()
    bAutomateEtape.grid_remove()
    bAutomateComplet.grid_remove()
    bConfirmerOp.grid_remove()


###############################################
# Définition des fonctions gestion de données:
def random():
    """Créée une matrice de 48*48 avec des nombres rdm entre 0 et 3"""
    print("random")
    matrice = [[rdm.randint(0, 3) for i in range(0, 47)]for i in range(0, 47)]
    return matrice


def operation(mat):
    """Fait une opération entre dataSand et la matrice donnée en argument.
    Elle récupère le type d'opération via une variable globale initié avant."""
    print("operation")
    if operationType == "Addition":
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                dataSand[i][j] += mat[i][j]
    elif operationType == "Soustraction":
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                if dataSand[i][j] - mat[i][j] < 0:
                    dataSand[i][j] = 0
                else:
                    dataSand[i][j] -= mat[i][j]
    showSable(dataSand)
    affichePage("Principale")


def setConfig(config: str, op=False):
    """Fonction qui crée une matrice en fonction du paramètre donné et qui
    stocke la matrice dans matrice. Si op est False (alors c'est uniquement
    une initialisation de la matrice par un type), elle remplace dataSand
    par la matrice."""
    global dataSand, matrice
    print("setConfig")
    if config == "rdm":
        matrice = random()
    elif True:
        pass
    if op is False:
        dataSand = matrice
    showSable(matrice)


def stabiliserCase(x, y):
    print("Stabilisation Case")
    if dataSand[y][x] >= 5:
        # on vérifie que la case voisine n'est pas hors champ.
        if (len(dataSand) - 1) > (y + 1):
            dataSand[y + 1][x] += 1
        if (len(dataSand) - 1) > (y - 1):
            dataSand[y - 1][x] += 1
        if (len(dataSand) - 1) > (x + 1):
            dataSand[y][x + 1] += 1
        if (len(dataSand) - 1) > (x - 1):
            dataSand[y][x - 1] += 1
        dataSand[y][x] -= 4
        if dataSand[y][x] >= len(couleur):
            cTableau.itemconfigure(
                guiSable[y][x],
                fill="black")
        else:
            cTableau.itemconfigure(
                guiSable[y][x],
                fill=couleur[dataSand[y][x]])


def automate(auto=False):
    for i in range(0, len(dataSand)):
        for j in range(0, len(dataSand)):
            stabiliserCase(x=j, y=i)
    if auto is True:
        cTableau.after(20, automate)


###############################################
# Création des Boutons
bconfig = tk.Button(
    root,
    text="Charger Config",
    command=lambda: affichePage("Config pour Affichage"))
bconfig.grid(column=0, row=1)

brandom = tk.Button(
    root,
    text="Aléatoire",
    command=lambda: setConfig("rdm"))
brandomOp = tk.Button(
    root,
    text="Aléatoire",
    command=lambda: setConfig("rdm", op=True))

bpilecentree = tk.Button(
    root,
    text="Pile centree",
    command=lambda: setConfig("pile"))
bpilecentreeOp = tk.Button(
    root,
    text="Pile centree",
    command=lambda: setConfig("pile", op=True))

bmaxstable = tk.Button(
    root,
    text="Max Stable",
    command=lambda: setConfig("max stable"))
bmaxstableOp = tk.Button(
    root,
    text="Max Stable",
    command=lambda: setConfig("max stable", op=True))

bidentity = tk.Button(
    root,
    text="Identity",
    command=lambda: setConfig("identity"))

bidentityOp = tk.Button(
    root,
    text="Identity",
    command=lambda: setConfig("identity", op=True))

boperation = tk.Button(
    root,
    text="Operation",
    command=lambda: affichePage("Operation"))
boperation.grid(column=0, row=2)

bRetour = tk.Button(
    root,
    text="retour",
    command=lambda: affichePage("Principale"),
    background="red")
bRetourOp = tk.Button(
    root,
    text="retour",
    command=lambda: affichePage("Operation"),
    background="red")

bsauvegarde = tk.Button(
    root,
    text="Sauvegarder la config")
bsauvegarde.grid(column=0, row=3)

bAddition = tk.Button(
    root,
    text="Addition",
    command=lambda: affichePage("Config pour Operation", op="Addition"))

bSoustraction = tk.Button(
    root,
    text="Soustraction",
    command=lambda: affichePage("Config pour Operation", op="Soustraction"))

bAutomateEtape = tk.Button(
    root,
    text="Automate",
    command=automate)

bAutomateComplet = tk.Button(
    root,
    text="Stabilisation",
    command=lambda: automate(True))

bConfirmerOp = tk.Button(
    root,
    text="Confirmer", bg="green", command=lambda: operation(matrice))
###############################################
# Création label affichage page
lAffichePage = tk.Label(text="Page Principale")
lAffichePage.grid(column=1, row=0)
###############################################
# Définition des fonctions graphiques:


def diezFormation():
    """Crée les diez qui délimite la grille de rectangle"""
    print("diezformation")
    x = 20
    y = 10
    for j in range(0, 2):
        for i in range(0, 47):
            cTableau.create_text(x, y, text="#")
            x += 10
        y = 490
        x = 20
    x = 10
    y = 20
    for j in range(0, 2):
        for i in range(0, 47):
            cTableau.create_text(x, y, text="#")
            y += 10
        x = 490
        y = 20


def initialisation():
    """Crée la matrice de carré 48*48 et stocke les objets graphique
    dans guiSable"""
    global guiSable
    print("initialisation")
    sousListguiSable = []
    diezFormation()
    y = 20
    for i in range(0, 47):
        x = 10
        for j in range(0, 47):
            x += 10
            rectangle = cTableau.create_rectangle(
                (x - 5, y - 5),
                (x + 5, y + 5),
                fill="White")
            sousListguiSable.append(rectangle)
        guiSable.append(sousListguiSable)
        sousListguiSable = []
        y += 10


def showSable(config: list):
    """Change tout les objets graphique rectangle de GuiSable en la couleur
    indiqué par le fichier config"""
    print("ShowSable")
    for i in range(0, len(config)):
        for j in range(0, len(config[i])):
            if config[i][j] >= len(couleur):
                cTableau.itemconfigure(guiSable[i][j], fill="black")
            else:
                cTableau.itemconfigure(guiSable[i][j], fill=couleur[config[i][j]])
                


##############################################


##############################################












# Boucle Principale
initialisation()
root.mainloop()
# Boucle Principale
