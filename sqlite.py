import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()

# Requête SQL pour récupérer toutes les données
c.execute('SELECT * FROM capteur')

# Récupération de toutes les lignes
rows = c.fetchall()

# Affichage des données récupérées
for row in rows:
    print(f"ID: {row[0]}, Valeur: {row[1]}, Timestamp: {row[2]}")

# Fermeture de la connexion à la base de données
conn.close()
