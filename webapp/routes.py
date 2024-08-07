from webapp import app, db, os
from webapp.logger import Logger
from flask import request, render_template
from webapp.db_utils import create_db, add_encrypted_secret, read_all_secrets, find_secret, delete_secret
from webapp.secret_utils import decrypt, encrypt, get_rk_alias, decryptContent, encrypt_content

log_global = Logger("global", app.config['LOGS_LOCATION'])
log_db_utils = Logger("db_utils", app.config['LOGS_LOCATION'])
log_secret_utils = Logger("secret_utils", app.config['LOGS_LOCATION'])

@app.route('/')
def _index():
    log_global.debug("Index page requested")
    return render_template('index.html')

@app.route('/manage')
def _manage():
    log_global.debug("Management page requested")
    return render_template('manage.html', secrets=read_all_secrets(log_db_utils))

@app.route('/decrypt',methods = ['POST'])
def _decrypt():
    log_global.debug("Secret decryption requested")

    secret_id = int(request.form['id'])

    log_global.debug("Reading secret with id=%d..." % secret_id)
    secret = find_secret(secret_id, log_db_utils)
    if secret != None:
        log_global.debug("Secret with id=%d found!" % secret_id)
        return decrypt(secret.content, log_secret_utils)
    else:
        log_global.error("Secret with id=%d not found!" % secret_id)
        return "ERROR-SECRET-NOT-FOUND"

@app.route('/add',methods = ['GET'])
def _add_form():
    log_global.debug("Secret add page requested")
    return render_template('add.html')

@app.route('/add',methods = ['POST'])
def _add():
    log_global.debug("Secret add requested")
    content = encrypt(request.form['content'], log_secret_utils)
    description = request.form['description']
    rk_alias = get_rk_alias()
    add_encrypted_secret(rk_alias, content, description, log_db_utils)

    return render_template('manage.html', secrets=read_all_secrets(log_db_utils))

@app.route('/delete',methods = ['POST'])
def _delete():
    log_global.debug("Secret delete requested")
    id = request.values["id"]

    delete_secret(id, log_db_utils)

    return "OK"

@app.route('/init',methods = ['POST'])
def _init():
    log_global.debug("DB init requested")
    create_db()
    
    return "OK"

@app.route('/tools',methods = ['GET'])
def _tools():
    log_global.debug("Tools page requested")
    return render_template('tools.html')

@app.route('/tools/encrypt',methods = ['POST'])
def _tools_encrypt():
    log_global.debug("Tools/encrypt requested")

    content = request.values["content"]
    key = request.values["key"]

    return encrypt_content(content, key)

@app.route('/tools/decrypt',methods = ['POST'])
def _tools_decrypt():
    log_global.debug("Tools/decrypt requested")

    content = request.values["content"]
    key = request.values["key"]

    return decryptContent(content, key)