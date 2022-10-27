################################################################################
# Projet Sudoku (L1 Semestre 2)
# Matteo Rabache
################################################################################

# Import des libraries:

import tkinter as tk
from tkinter import messagebox
import random
import pickle


# Definition des constantes:

HEIGHT, WIDTH = 500, 750
COTE = 15
ROW, COL = (HEIGHT // COTE), (WIDTH // COTE)
COULEUR_QUADR = 'grey30'
C_WATER = '#ABDAFF'
C_FOREST = '#139235'
C_FIRE = '#FF0000'
C_SHIRE = '#E0ED1D'
C_HOT_ASHES = '#600000'
C_COLD_ASHES = '#525252'
WATER = 0
SHIRE = 1
FOREST = 2
FIRE = 3
HOT_ASHES = 4
COLD_ASHES = 5
TRANSFO = 6
DUREE_CENDRE = 5
DUREE_FEU = 5
END = 1
SPEED_SIMU = 5000


# Definition des variables globales:

case = [[0 for row in range(ROW)] for col in range(COL)]
etat = [[WATER for row in range(ROW)] for col in range(COL)]
step = [[0 for row in range(ROW)] for col in range(COL)]
nb_etape = 0
nb_fire = 0
nb_hot_ashes = 0


# Definition des fonctions:

def LandGrid():
    """Affiche un quadrillage constitué de carrés de côté COTE"""
    y = 0
    while y <= HEIGHT:
        canvas.create_line((0, y), (WIDTH, y), fill=COULEUR_QUADR)
        y += COTE
    x = 0
    while x <= WIDTH:
        canvas.create_line((x, 0), (x, HEIGHT), fill=COULEUR_QUADR)
        x += COTE


def Fire(event):
    """Modifie le type de la case cliquer en "feu" """
    x = event.x // COTE
    y = event.y // COTE
    if etat[x][y] == SHIRE or etat[x][y] == FOREST:
        etat[x][y] = FIRE
        coul = C_FIRE
        canvas.itemconfig(case[x][y], fill=coul)
    pass


def Stop():
    """Interrompt le programme"""
    global END
    END = 0
    pass


def Generate():
    """Fonction du boutton qui permet de générer un nouveau environnement"""
    global nb_etape
    for y in range(ROW):
        for x in range(COL):
            case[x][y] = canvas.create_rectangle(
                (x * COTE, y * COTE, (x + 1) * COTE, (y + 1) * COTE),
                outline=COULEUR_QUADR,
                fill=C_WATER)
            etat[x][y] = WATER
    i = 0
    while i <= (ROW * COL // 2):
        i += 1
        etat[random.randrange(COL)][random.randrange(ROW)] = SHIRE
    i = 0
    while i <= (ROW * COL // 2):
        i += 1
        etat[random.randrange(COL)][random.randrange(ROW)] = FOREST
    nb_etape = 0
    Draw(etat)
    Counting()


def Draw(etat):
    for y in range(HEIGHT // COTE):
        for x in range(WIDTH // COTE):
            if etat[x][y] == WATER:
                coul = C_WATER
                canvas.itemconfig(case[x][y], fill=coul)
            elif etat[x][y] == SHIRE:
                coul = C_SHIRE
                canvas.itemconfig(case[x][y], fill=coul)
            elif etat[x][y] == FOREST:
                coul = C_FOREST
                canvas.itemconfig(case[x][y], fill=coul)
            elif etat[x][y] == FIRE or etat[x][y] == TRANSFO:
                coul = C_FIRE
                canvas.itemconfig(case[x][y], fill=coul)
                etat[x][y] = FIRE
            elif etat[x][y] == HOT_ASHES:
                coul = C_HOT_ASHES
                canvas.itemconfig(case[x][y], fill=coul)
            elif etat[x][y] == COLD_ASHES:
                coul = C_COLD_ASHES
                canvas.itemconfig(case[x][y], fill=coul)


def SaveFich():
    """Sauvgarde dans un ficher l'environement créer."""
    f = open('save.txt', 'wb')
    pickle.dump(etat, f)
    f.close()


def LoadLand():
    """Charge un fichier d'un environement"""
    load = open('save.txt', "rb")
    etat = pickle.load(load)
    load.close()
    Draw(etat)


def Advancement():
    global nb_etape
    cpt1 = 0
    cpt2 = 0
    nb_etape += 1
    StepCounting()
    for i in range(1, len(etat)-1):
        cpt2 = 0
        cpt1 = 0
        for j in range(1, len(etat[i])-1):
            cpt2 = 0
            cpt1 = 0
            if etat[i][j] == HOT_ASHES:
                step[i][j] = step[i][j] + 1
                if step[i][j] == DUREE_CENDRE:
                    etat[i][j] = 5
                    step[i][j] = 5
            if etat[i][j] == FIRE:
                step[i][j] = step[i][j]+1
                if step[i][j] == DUREE_FEU:
                    etat[i][j] = 4
                    step[i][j] = 0
            if etat[i][j] == SHIRE:
                if etat[i-1][j] == FIRE:
                    cpt1 = cpt1 + 1
                if etat[i][j-1] == FIRE:
                    cpt1 = cpt1 + 1
                if etat[i+1][j] == FIRE:
                    cpt1 = cpt1 + 1
                if etat[i][j+1] == FIRE:
                    cpt1 = cpt1 + 1
                if cpt1 >= 1:
                    etat[i][j] = TRANSFO
            if etat[i][j] == FOREST:
                if etat[i-1][j] == FIRE:
                    cpt2 = cpt2 + 1
                if etat[i][j-1] == FIRE:
                    cpt2 = cpt2 + 1
                if etat[i+1][j] == FIRE:
                    cpt2 = cpt2 + 1
                if etat[i][j+1] == FIRE:
                    cpt2 = cpt2 + 1
                if random.random() <= 0.1 * cpt2:
                    etat[i][j] = TRANSFO
    Draw(etat)
    Counting()


def NextStep(event):
    Advancement()


def Simulation():
    global nb_etape, END
    Advancement()
    StepCounting()
    id_Simu = canvas.after(SPEED_SIMU, Simulation)
    if END == 0 or (nb_fire == 0 and nb_hot_ashes == 0):
        canvas.after_cancel(id_Simu)


def Counting():
    """Compte le nombre de case en feu et le nombre d'étape de la simulation"""
    global nb_fire, nb_hot_ashes
    nb_fire = 0
    nb_hot_ashes = 0
    for y in range(ROW):
        for x in range(COL):
            if etat[x][y] == FIRE:
                nb_fire += 1
            if etat[x][y] == HOT_ASHES:
                nb_hot_ashes += 1
    a = "Parcelles en feu :" + str(nb_fire)
    message_FIRE.configure(text=a)
    StepCounting()


def StepCounting():
    """Compte le nombre d'étapes"""
    b = "Nombre d'étapes : " + str(nb_etape)
    message_step.configure(text=b)


# Programme principal:
racine = tk.Tk()
racine.title("Simulation de la propagation d’un incendie")

canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH, bg='white')


button_random_land = tk.Button(racine, text="Terrain au hasard", font=("arial", "10"), command=Generate)
button_save_land = tk.Button(racine, text="Sauvegarder le terrain", font=("arial", "10"), command=SaveFich)
button_load_land = tk.Button(racine, text="Ouvrir un terrain", font=("arial", "10"), command=LoadLand)
button_next_step = tk.Button(racine, text="Etape suivante", font=("arial", "10"), command=Advancement)
button_new_simulation = tk.Button(racine, text="Nouvelle simulation", font=("arial", "10"), command=Counting)
button_start = tk.Button(racine, text="START", font=("arial", "10"), command=Simulation)
button_stop = tk.Button(racine, text="STOP", font=("arial", "10"), command=Stop)
message_FIRE = tk.Label(racine, text="Parcelles en feu : 0", font=("arial", "10"))
message_step = tk.Label(racine, text="Nombre d'étapes : 0", font=("arial", "10"))
message_speed = tk.Label(racine, text="1 étape toutes les 5 secondes", font=("arial", "10"))


canvas.grid(column=0, row=0)
button_random_land.grid(column=0, row=0)
button_save_land.grid(column=0, row=1)
button_load_land.grid(column=0, row=2)
button_new_simulation.grid(column=0, row=3)
button_start.grid(column=0, row=4)
button_next_step.grid(column=0, row=5)
button_stop.grid(column=0, row=6)
message_FIRE.grid(column=0, row=7)
message_step.grid(column=0, row=8)
message_speed.grid(column=0, row=9)
canvas.grid(column=1, row=0, rowspan=10)


LandGrid()
Generate()

canvas.bind("<Button-1>", Fire)
canvas.bind_all('<space>', NextStep)

messagebox.showinfo("Indication des touches de controle", " Clic gauche sur parcelle : mise en feu \n Touche espace : étape suivante")

racine.mainloop()
