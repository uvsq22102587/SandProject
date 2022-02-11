###################################
# groupe LDDBI 1
# Benjamin PREHAUD
# Arthur VINCENS
# https://github.com/uvsq22102587/SandProject
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