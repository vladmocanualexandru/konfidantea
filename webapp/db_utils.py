from webapp import db
from webapp.encrypted_secret import EncryptedSecret

def create_db():
    db.create_all()

def add_encrypted_secret(content, description):
    new_entry = EncryptedSecret(
        content = content,
        description = description
    )

    db.session.add(new_entry)
    db.session.commit()

    print("Created encrypted secret with id ", new_entry.id)

def delete_secret(id):
    db.session.delete(EncryptedSecret.query.get_or_404(id))
    db.session.commit()

def read_all_secrets():
    return EncryptedSecret.query.all()

def find_secret(id):
    return EncryptedSecret.query.filter_by(id=id).first()