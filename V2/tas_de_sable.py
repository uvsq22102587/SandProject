###############################################
# Groupe LDDBI
# Benjamin PREHAUD
# Arthur VINCENS
# Valentin JACQUIN
# https://github.com/uvsq22102587/SandProject
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
    
