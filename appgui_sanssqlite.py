import serial
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importation de ttk pour la barre de progression
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Configuration du port série
port = 'COM4'  # Remplace par le bon port
baud_rate = 9600

# Tentative d'ouverture du port série
try:
    ser = serial.Serial(port, baud_rate, timeout=1)
    print("Port ouvert avec succès.")
except serial.SerialException as e:
    print(f"Erreur d'ouverture du port série : {e}")
    ser = None  # Ne pas continuer si le port ne peut pas être ouvert

# Création de la fenêtre principale
root = tk.Tk()
root.title("Données du Capteur")

# Création des widgets
data_label = tk.Label(root, text="Données du capteur :", font=('Helvetica', 16))
data_label.pack(pady=10)

sensor_value = tk.StringVar()
sensor_value_label = tk.Label(root, textvariable=sensor_value, font=('Helvetica', 24))
sensor_value_label.pack(pady=20)

# Création de la barre de progression (jauge)
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", maximum=100)
progress.pack(pady=20)

# Ajout d'un champ pour sélectionner la plage de temps
time_range_label = tk.Label(root, text="Sélectionner la plage de temps (en points):", font=('Helvetica', 12))
time_range_label.pack(pady=10)

# Plages de temps possibles : 50, 100, 200 points, avec un maximum de 2000 points
time_range_var = tk.IntVar(value=100)  # Valeur par défaut : 100 points
time_range_menu = ttk.Spinbox(root, from_=50, to=2000, increment=50, textvariable=time_range_var, width=5)  # Maximum porté à 2000
time_range_menu.pack(pady=10)

# Bouton pour valider et appliquer la plage de temps
apply_button = tk.Button(root, text="Appliquer", command=lambda: adjust_time_range())
apply_button.pack(pady=10)

# Variables pour stocker les données de la courbe
x_data = np.arange(0, 100)  # On affiche les 100 dernières valeurs par défaut
y_data = np.zeros(100)

# Création du graphique
fig, ax = plt.subplots()
line, = ax.plot(x_data, y_data)
ax.set_ylim(0, 1023)
ax.set_title("Valeurs du capteur")
ax.set_xlabel("Temps (échantillons)")
ax.set_ylabel("Valeur (0-1023)")

# Intégrer le graphique dans Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=20)
canvas.draw()

# Fonction pour ajuster la taille des données de la courbe en fonction de la plage de temps sélectionnée
def adjust_time_range():
    global x_data, y_data
    time_range = time_range_var.get()  # Obtenir la plage de temps sélectionnée
    x_data = np.arange(0, time_range)  # Redimensionner x_data
    y_data = np.zeros(time_range)  # Réinitialiser y_data avec des zéros
    ax.set_xlim(0, time_range - 1)  # Ajuster la limite de l'axe X
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    canvas.draw()

# Fonction pour mettre à jour les données et le graphique
def update_data():
    if ser:  # Vérifie si le port série est ouvert
        try:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').rstrip()
                print(f"Data received: {data}")  # Affiche les données reçues pour débogage
                
                try:
                    # Conversion de la donnée en entier (de 0 à 1023)
                    raw_value = int(data)
                    if 0 <= raw_value <= 1023:
                        # Conversion en pourcentage
                        percentage = (raw_value / 1023) * 100
                        sensor_value.set(f"{raw_value} ({percentage:.1f}%)")  # Met à jour la valeur affichée
                        progress['value'] = percentage  # Mise à jour de la barre
                        
                        # Mise à jour des données de la courbe
                        y_data[:-1] = y_data[1:]  # Décaler les anciennes valeurs
                        y_data[-1] = raw_value  # Ajouter la nouvelle valeur
                        line.set_ydata(y_data)
                        canvas.draw()
                    else:
                        # Si la valeur est hors limite, réinitialiser et afficher un message
                        progress['value'] = 0
                        sensor_value.set("Valeur hors limite")
                except ValueError:
                    # Si une valeur non valide est reçue
                    sensor_value.set("Valeur non valide")
                    progress['value'] = 0  # Réinitialiser la barre en cas d'erreur de conversion
        except serial.SerialException as e:
            messagebox.showerror("Erreur", f"Erreur lors de la lecture : {e}")
    else:
        messagebox.showerror("Erreur", "Le port série n'est pas ouvert.")
    
    root.after(100, update_data)  # Appelle cette fonction toutes les 100 ms

# Démarrage de la mise à jour des données
if ser:
    update_data()

# Boucle principale de Tkinter
root.mainloop()

# Ferme le port série à la fermeture de la fenêtre
if ser and ser.is_open:
    ser.close()
    print("Port série fermé.")
