from webapp import app, db
from flask import request, render_template
from webapp.db_utils import create_db, add_encrypted_secret, read_all_secrets, find_secret, delete_secret
from webapp.secret_utils import decrypt

@app.route('/')
def _index():
    return render_template('index.html')

@app.route('/manage')
def _manage():
    return render_template('manage.html', secrets=read_all_secrets())

@app.route('/decrypt',methods = ['POST'])
def _decrypt():
    secret = find_secret(int(request.form['id']))

    return decrypt(secret.content)

@app.route('/add',methods = ['POST'])
def _add():
    content = request.form['content']
    description = request.form['description']

    add_encrypted_secret(content, description)

    return "OK"

@app.route('/delete',methods = ['POST'])
def _delete():
    id = request.values["id"]

    delete_secret(id)

    return "OK"

@app.route('/init',methods = ['POST'])
def _init():
    create_db()
    
    return "OK"