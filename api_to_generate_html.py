from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Route pour servir la page HTML
@app.route('/')
def index():
    return render_template('index.html')  # Assure-toi que le fichier index.html est dans le dossier templates

# Route pour récupérer les données de la base de données
@app.route('/data')
def get_data():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, valeur FROM capteur")
    rows = cursor.fetchall()
    conn.close()

    # Organiser les données dans un format JSON
    data = {
        "timestamps": [row[0] for row in rows],  # Liste des timestamps
        "values": [row[1] for row in rows]       # Liste des valeurs
    }
    
    return jsonify(data)  # Utilise jsonify pour retourner les données au format JSON

if __name__ == '__main__':
    app.run(debug=True)
