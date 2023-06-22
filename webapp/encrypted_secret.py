from webapp import db

class EncryptedSecret(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)