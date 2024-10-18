import tkinter as tk
from tkinter import messagebox

# Créer la fenêtre principale
root = tk.Tk()
root.title("Interface Graphique en Tkinter")
root.geometry("400x300")

# Fonction appelée lorsqu'on clique sur le bouton
def on_button_click():
    user_input = text_entry.get()
    if user_input:
        messagebox.showinfo("Message", f"Vous avez entré : {user_input}")
    else:
        messagebox.showwarning("Avertissement", "Veuillez entrer un texte")

# Ajouter un label
label = tk.Label(root, text="Entrez quelque chose :")
label.pack(pady=10)

# Ajouter une entrée de texte
text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=10)

# Ajouter un bouton
button = tk.Button(root, text="Soumettre", command=on_button_click)
button.pack(pady=10)

# Ajouter un autre bouton pour quitter
quit_button = tk.Button(root, text="Quitter", command=root.quit)
quit_button.pack(pady=10)

# Lancer la boucle principale
root.mainloop()
