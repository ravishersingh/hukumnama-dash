
import json
import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_queries():
    with open('queries.json') as f:
        return json.load(f)

def get_settings():
    with open('settings.json') as f:
        return json.load(f)

def save_settings(settings):
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    settings = get_settings()
    conn = get_db_connection()
    queries = get_queries()
    
    transliterations = {}
    for lang in settings.get('transliteration', []):
        transliterations[lang] = conn.execute(queries['transliteration'][lang], [page]).fetchall()

    translations = {}
    for lang in settings.get('translation', []):
        translations[lang] = conn.execute(queries['translation'][lang], [page]).fetchall()

    conn.close()

    return render_template('index.html', 
                           transliterations=transliterations, 
                           translations=translations,
                           settings=settings)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        new_settings = request.get_json()
        save_settings(new_settings)
        return jsonify({'status': 'success'})
    else:
        return jsonify(get_settings())

if __name__ == '__main__':
    app.run(debug=True)
