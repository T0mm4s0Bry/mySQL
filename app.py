from flask import Flask, render_template, jsonify
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)

# Configura la connessione al database MySQL
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='mysql',  # Usa il nome del servizio MySQL nel tuo docker-compose (se usi Docker)
            user='root',   # Sostituisci con l'utente corretto
            password='',  # Sostituisci con la password corretta
            database='mydatabase'  # Sostituisci con il nome del tuo database
        )
        return connection
    except Error as e:
        print(f"Errore di connessione: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/environment')
def env():
    return jsonify(
            {"env":[
                {"MYSQL_DATABASE": os.environ["MYSQL_DATABASE"]},
                {"MYSQL_USER": os.environ["MYSQL_USER"]},
                {"MYSQL_ROOT_PASSWORD": os.environ["MYSQL_ROOT_PASSWORD"]}
            ]})

@app.route('/simple_json')
def simple_json():
    return jsonify('{saluto:ciao}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
