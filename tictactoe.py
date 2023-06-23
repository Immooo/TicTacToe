import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Initialisation de la fenêtre
fenetre = tk.Tk()
fenetre.title("Jeu de Tic Tac Toe")

# Initialisation du plateau de jeu
plateau = [" "]*9

# Initialisation du tour de jeu
tour_de_X = True
fin_du_jeu = False

# Fonction pour vérifier si un joueur a gagné ou si la partie est terminée
def verifier_victoire():
    combinaisons_gagnantes = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combinaison in combinaisons_gagnantes:
        if plateau[combinaison[0]] == plateau[combinaison[1]] == plateau[combinaison[2]] != " ":
            gagnant = joueur_X if plateau[combinaison[0]] == "X" else joueur_O
            messagebox.showinfo("Fin du jeu", "Le joueur " + gagnant + " a gagné !")
            fenetre.quit()
    # Vérifier si toutes les positions du plateau sont remplies
    if " " not in plateau:
        messagebox.showinfo("Fin du jeu", "Fin de la partie, ex-aequo.")
        if messagebox.askyesno("Nouvelle partie", "Voulez-vous jouer une nouvelle partie ?"):
            fenetre.quit()
            main()
        else:
            fenetre.quit()

# Fonction pour gérer le clic sur un bouton
def clic_bouton(index):
    global tour_de_X
    if plateau[index] == " " and not fin_du_jeu:
        plateau[index] = "X" if tour_de_X else "O"
        labels[index].config(text=plateau[index], fg="red", font=("Helvetica", 24))
        boutons[index].config(state="disabled")  # Disable the button after it's clicked
        verifier_victoire()
        tour_de_X = not tour_de_X

# Création des boutons et des labels
def main():
    global boutons, labels, plateau, tour_de_X, fenetre, joueur_X, joueur_O
    boutons = []
    labels = []
    plateau = [" "]*9
    tour_de_X = True

    # Demande des noms des joueurs
    joueur_X = ""
    while not joueur_X:
        joueur_X = simpledialog.askstring("Input", "Quel est le nom du premier joueur (X) ?", parent=fenetre)

    joueur_O = ""
    while not joueur_O:
        joueur_O = simpledialog.askstring("Input", "Quel est le nom du deuxième joueur (O) ?", parent=fenetre)

    for i in range(9):
        fenetre.grid_rowconfigure(i//3, weight=1)
        fenetre.grid_columnconfigure(i%3, weight=1)
        bouton = tk.Button(fenetre, command=lambda i=i: clic_bouton(i))
        bouton.grid(row=i//3, column=i%3, sticky="nsew")
        boutons.append(bouton)
        label = tk.Label(bouton, text=" ")
        label.pack(expand=True)
        labels.append(label)

    fenetre.mainloop()

main()
