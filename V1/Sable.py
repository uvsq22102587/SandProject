###########################################
# Autor: Valentin Jacquin
###########################################
import tkinter as tk
import random as rdm
import time as time
import numpy as np

fenetre = tk.Tk()
fenetre.title("Ecoulement sable")
cWidth, cHeight, dataSand, guiSand = 500, 500, [], []
cTableau = tk.Canvas(width=cWidth, height=cHeight, bg="white")
cTableau.grid(column=2, row=0, rowspan=10)
dataSand, nbrValeur, valeurMaxCase, checkPause, configStockage, guiSandConfig = [], 48, 5, False, [], []
configDataSand, guiSandConfig, nConfigSave, checkConfigChoose= [], [], 1, False
colorAssignement = ["#FFFFFF", "#707070", "#606060", "#505050", "#404040", "#303030", "#202020", "#101010", "#000000"]


def clearTableau():
    global guiSand
    print("clearTableau")
    for i in range(0, len(guiSand)):
        for j in range(0, len(guiSand[i])):
            cTableau.delete(guiSand[i][j])
    guiSand = []


def diezFormation():
    global dataSand, guiSand, nbrValeur
    print("diezformation")
    x = 20
    y = 10
    sousListGuiSand = []
    for j in range(0, 2):
        for i in range(0, nbrValeur - 1):
            diez = cTableau.create_text(x, y, text="#")
            x += 10
            sousListGuiSand.append(diez)
        y = 490
        x = 20
        guiSand.append(sousListGuiSand)
        sousListGuiSand = []
    x = 10
    y = 20
    for j in range(0, 2):
        for i in range(0, nbrValeur - 1):
            diez = cTableau.create_text(x, y, text="#")
            y += 10
            sousListGuiSand.append(diez)
        x = 490
        y = 20
        guiSand.append(sousListGuiSand)
        sousListGuiSand = []


def initialisation():
    global dataSand, guiSand, nbrValeur
    print("initialisation")
    sousListGuiSand = []
    diezFormation()
    y = 20
    for i in range(0, nbrValeur - 1):
        x = 10
        for j in range(0, nbrValeur - 1):
            x += 10
            text = cTableau.create_rectangle((x - 5, y - 5), (x + 5, y + 5), fill="White")
            sousListGuiSand.append(text)
        guiSand.append(sousListGuiSand)
        y += 10


def showSand():
    global dataSand, guiSand, colorAssignement
    print("showSand")
    sousListeGuiSand = []
    clearTableau()
    y = 20
    diezFormation()
    for i in range(0, len(dataSand) - 1):
        x = 10
        for j in range(0, len(dataSand[i]) - 1):
            x += 10
            if len(colorAssignement) <= dataSand[i][j]:
                text = cTableau.create_rectangle((x - 5, y - 5), (x + 5, y + 5), fill="black")
                sousListeGuiSand.append(text)
            else:
                text = cTableau.create_rectangle((x - 5, y - 5), (x + 5, y + 5), fill=colorAssignement[dataSand[i][j]])
                sousListeGuiSand.append(text)
        guiSand.append(sousListeGuiSand)
        y += 10


def randomGeneration():
    global dataSand, nbrValeur, valeurMaxCase
    print("randomGeneration")
    dataSand = []
    for i in range(0, nbrValeur):
        sousListdataSand = []
        for j in range(0, nbrValeur):
            bloc = rdm.randint(0, valeurMaxCase)
            sousListdataSand.append(bloc)
        dataSand.append(sousListdataSand)
    showSand()
    return


def diezFormationConfig():
    global guiSandConfig, nbrValeur, cCanevas
    print("diezFormationConfig")
    x = 20
    y = 10
    sousListGuiSandConfig = []
    for j in range(0, 2):
        for i in range(0, nbrValeur - 1):
            diez = cCanevas.create_text(x, y, text="#")
            x += 10
            sousListGuiSandConfig.append(diez)
        y = 490
        x = 20
        guiSandConfig.append(sousListGuiSandConfig)
        sousListGuiSandConfig = []
    x = 10
    y = 20
    for j in range(0, 2):
        for i in range(0, nbrValeur - 1):
            diez = cCanevas.create_text(x, y, text="#")
            y += 10
            sousListGuiSandConfig.append(diez)
        x = 490
        y = 20
        guiSandConfig.append(sousListGuiSandConfig)
        sousListGuiSandConfig = []


def clearTableauConfig():
    global guiSandConfig
    print("clearTableauConfig")
    for i in range(0, len(guiSandConfig)):
        for j in range(0, len(guiSandConfig[i])):
            cCanevas.delete(guiSandConfig[i][j])
    guiSandConfig = []


def showConfig(n:str):
    global guiSandConfig, colorAssignement, cCanevas, configDataSand
    sousListeGuiSandConfig = []
    print("showConfig")
    loadConfig(nConfig=n)
    clearTableauConfig()
    y = 20
    diezFormationConfig()
    for i in range(0, len(configDataSand) - 1):
        x = 10
        for j in range(0, len(configDataSand[i]) - 1):
            x += 10
            text = cCanevas.create_rectangle((x - 5, y - 5), (x + 5, y + 5), fill=colorAssignement[configDataSand[i][j]])
            sousListeGuiSandConfig.append(text)
        guiSandConfig.append(sousListeGuiSandConfig)
        y += 10


def loadConfig(nConfig:str):
    global configDataSand, configStockage, dataSand
    print("loadConfig")
    configDataSand = np.loadtxt('config%s.txt'%nConfig, dtype=int)
    print(configDataSand)


def useConfig():
    global checkConfigChoose, fonctionAsk
    if fonctionAsk == "addition":
        add()
    elif fonctionAsk == "soustraction":
        soustraction()
    fenetreConfig.destroy()
    checkConfigChoose = True
    


def chooseConfig():
    global configDataSand, cHeight, cWidth, cCanevas, fenetreConfig
    print("chooseConfig")
    fenetreConfig = tk.Tk()
    fenetreConfig.title("Choisissez votre configuration:")
    cCanevas = tk.Canvas(fenetreConfig, bg="White", height=cHeight, width=cWidth)
    cCanevas.grid(column=1, row=0, rowspan=10)
    bConfig1 = tk.Button(fenetreConfig, text="Configuration 1", command=lambda: showConfig(n="1"))
    bConfig1.grid(column=0, row=0)
    bConfig2 = tk.Button(fenetreConfig, text="Configuration 2", command=lambda: showConfig(n="2"))
    bConfig2.grid(column=0, row=1)
    bConfig3 = tk.Button(fenetreConfig, text="Configuration 3", command=lambda: showConfig(n="3"))
    bConfig3.grid(column=0, row=2)
    bConfig4 = tk.Button(fenetreConfig, text="Configuration 4", command=lambda: showConfig(n="4"))
    bConfig4.grid(column=0, row=3)
    bConfig5 = tk.Button(fenetreConfig, text="Configuration 5", command=lambda: showConfig(n="5"))
    bConfig5.grid(column=0, row=4)
    bConfig6 = tk.Button(fenetreConfig, text="Configuration 6", command=lambda: showConfig(n="6"))
    bConfig6.grid(column=0, row=5)
    bCheckConfig = tk.Button(fenetreConfig, bg="red", text="Choisir cette configuration", command=useConfig)
    bCheckConfig.grid(column=0, row=7)


def lancementFonction(fonction : str):
    global dataSand, configDataSand, checkConfigChoose, fonctionAsk
    fonctionAsk = fonction
    chooseConfig()


def soustraction():
    global configDataSand, dataSand
    print("add")
    for i in range(0, len(dataSand) - 1):
        for j in range(0, len(dataSand[i]) - 1):
            dataSand[i][j] -= configDataSand[i][j]
            if dataSand[i][j] < 0:
                dataSand[i][j] = 0
    showSand()


def automate():
    global checkPause, guiSand, dataSand
    assert checkPause is False, "L'automate est en pause."
    checkFinish = True
    assert dataSand != [], "DataSand is empty"
    for i in range(0, len(dataSand) - 1):
        for j in range(0, len(dataSand) - 1):
            if i == 0 and j == 0:
                checkFinish = True
            if dataSand[i][j] > 4:
                print("o")
                checkFinish = False
                dataSand[i][j] -= 4
                if i != 0:
                    dataSand[i - 1][j] += 1
                if i != (len(dataSand) - 1):    
                    dataSand[i + 1][j] += 1
                if j != (len(dataSand[i]) - 1):
                    dataSand[i][j + 1] += 1
                dataSand[i][j - 1] += 1
    print(checkFinish)
    showSand()
    if checkFinish is True:
        return
    automate()



def pause():
    global checkPause
    if checkPause is True:
        checkPause = False
        bPauseAutomate['text'] = "Pause Automate"
        automate()
    else:
        checkPause = True
        bPauseAutomate['text'] = "Redémarrer Automate"
    


def add():
    global configDataSand, dataSand
    print("add")
    for i in range(0, len(dataSand) - 1):
        for j in range(0, len(dataSand[i]) - 1):
            dataSand[i][j] += configDataSand[i][j]
    showSand()


def saveDataSand():
    """Cette fonction sauvegarde la configuration actuelle affichée sur la fenêtre principale dans un fichier txt grâce à Numpy."""
    global dataSand, nConfigSave
    assert dataSand != [], "dataSand est vide"
    configuration = np.array(dataSand)
    np.savetxt('config%s.txt'%nConfigSave, configuration, fmt='%d')
    print("Configuration as been saved as config%s.txt"%nConfigSave)
    nConfigSave += 1
    if nConfigSave > 6:
        nConfigSave = 1




bSaveDataSand = tk.Button(bg="gray", command=saveDataSand, text="Sauvegarder Configuration")
bSaveDataSand.grid(column=0, row=7)
bRandom = tk.Button(bg="gray", command=randomGeneration, text="Génération aléatoire")
bRandom.grid(column=0, row=2)
bSoustraction = tk.Button(bg="gray", command=lambda: lancementFonction(fonction="soustraction"), text="Soustraction Tableau")
bSoustraction.grid(column=0, row=3)
bAdd = tk.Button(bg="gray", command=lambda: lancementFonction(fonction="addition"), text="Addition Tableau")
bAdd.grid(column=0, row=4)
bAutomate = tk.Button(bg="gray", command=automate, text="Automate")
bAutomate.grid(column=0, row=5)
bEmptySand = tk.Button(bg="gray", command=initialisation, text="Tableau Vide")
bEmptySand.grid(column=0, row=1)
bPauseAutomate = tk.Button(bg="gray", command=pause, text="Pause Automate")
bPauseAutomate.grid(column=0, row=6)
fenetre.mainloop()
