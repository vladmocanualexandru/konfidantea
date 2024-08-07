from webapp import db
from webapp.encrypted_secret import EncryptedSecret

def create_db():
    db.create_all()

def add_encrypted_secret(rk_alias, content, description, logger):
    logger.debug("Adding new secret ...")
    new_entry = EncryptedSecret(
        remote_key_alias = rk_alias,
        content = content,
        description = description
    )

    try:
        db.session.add(new_entry)
        db.session.commit()
        logger.debug("Created encrypted secret with id=%s" % new_entry.id)
    except Exception as e:
        logger.error("Error occured while adding new secret - %s" % str(e))
        raise e

def delete_secret(id, logger):
    logger.debug("Deleting secret with id=%s ..." % id)
    try:
        db.session.delete(EncryptedSecret.query.get_or_404(id))
        db.session.commit()
    except Exception as e:
        logger.error("Error occured while deleting secret - %s" % str(e))
        raise e

def read_all_secrets(logger):
    logger.debug("Reading all secrets ...")
    try:
        return EncryptedSecret.query.all()
    except Exception as e:
        logger.error("Error occured while reading all secrets - %s" % str(e))
        raise e

def find_secret(id, logger):
    logger.debug("Searching for secret with id=%s ..." % id)
    try:
        return EncryptedSecret.query.filter_by(id=id).first()
    except Exception as e:
        logger.error("Error occured while searching for secret - %s" % str(e))
        raise e
    