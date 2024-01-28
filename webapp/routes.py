from webapp import app, db
from flask import request, render_template
from webapp.db_utils import create_db, add_encrypted_secret, read_all_secrets, find_secret, delete_secret
from webapp.secret_utils import decrypt, encrypt, get_rk_alias, decryptContent, encrypt_content

@app.route('/')
def _index():
    return render_template('index.html')

@app.route('/manage')
def _manage():
    return render_template('manage.html', secrets=read_all_secrets())

@app.route('/decrypt',methods = ['POST'])
def _decrypt():
    secret = find_secret(int(request.form['id']))
    if secret != None:
        return decrypt(secret.content)
    else:
        return "ERROR-SECRET-NOT-FOUND"

@app.route('/add',methods = ['GET'])
def _add_form():
    return render_template('add.html')

@app.route('/add',methods = ['POST'])
def _add():
    content = encrypt(request.form['content'])
    description = request.form['description']
    rk_alias = get_rk_alias()
    add_encrypted_secret(rk_alias, content, description)

    return render_template('manage.html', secrets=read_all_secrets())

@app.route('/delete',methods = ['POST'])
def _delete():
    id = request.values["id"]

    delete_secret(id)

    return "OK"

@app.route('/init',methods = ['POST'])
def _init():
    create_db()
    
    return "OK"

@app.route('/tools',methods = ['GET'])
def _tools():
    return render_template('tools.html')

@app.route('/tools/encrypt',methods = ['POST'])
def _tools_encrypt():
    content = request.values["content"]
    key = request.values["key"]

    return encrypt_content(content, key)

@app.route('/tools/decrypt',methods = ['POST'])
def _tools_decrypt():
    content = request.values["content"]
    key = request.values["key"]

    return decryptContent(content, key)