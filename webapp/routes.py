from webapp import app, db
from flask import request, render_template
from webapp.db_utils import create_db, add_encrypted_secret, read_all_secrets, find_secret
from webapp.secret_utils import decrypt

@app.route('/')
def _index():
    return render_template('index.html', secrets=read_all_secrets())

@app.route('/decrypt',methods = ['POST'])
def _decrypt():
    secret = find_secret(int(request.form['id']))

    return decrypt(secret.content)

@app.route('/add_secret',methods = ['POST'])
def _add_secret():
    content = request.form['content']
    description = request.form['description']

    add_encrypted_secret(content, description)

    return "Secret added"

@app.route('/read_all_secrets',methods = ['POST'])
def _read_all_secrets():
    result = ""
    for entry in read_all_secrets():
        result+="%d %s %s\n"%(entry.id, entry.content, entry.description)

    return result

@app.route('/init',methods = ['POST'])
def _init():
    create_db()
    return "Database created"