from cryptography.fernet import Fernet
import base64
from os import environ 

def decryptContent(content, key):
    fernetKey = Fernet(base64.b64encode(key.encode('ascii')))
    return fernetKey.decrypt(content.encode()).decode()

def getEncryptedRemoteKey():    
    # read encrypted remote key
    encryptedRemoteKey = None
    for keyPath in environ.get('KONFIDANTEA_REMOTE_KEYS').split(','):
        try:
            with open(keyPath) as f:
                lines = f.readlines()
                encryptedRemoteKey = lines[0]
                break
        except:
            print('%s not found, trying next remote key..' % keyPath)

    return encryptedRemoteKey

def getRemoteKey():
    # read local key (not encrypted)
    localKey = environ.get('KONFIDANTEA_LOCAL_KEY')

    encryptedRemoteKey = getEncryptedRemoteKey()

    if encryptedRemoteKey == None:
        print('Unable to find a remote key!')
        return None
    else:
        # decrypt remote key using local key
        remoteKey = decryptContent(encryptedRemoteKey, localKey)

        return remoteKey


def decrypt(encrypted_secret):
    try:
        remoteKey = getRemoteKey()

        if remoteKey != None:
            # according to the specified index, decrypt, using the remote key, one of the encrypted passwords
            decryptedPassword = decryptContent(encrypted_secret, remoteKey)

            return decryptedPassword
        else:
            return "ERROR-REMOTE-KEY-MISSING"
    except Exception as e:
        # in case anything goes wrong, write ERROR to the temporary password file
        print(e)
        return "ERROR-UNKNOWN"
    
def encrypt_content(content, key):
    fernetKey = Fernet(base64.b64encode(key.encode('ascii')))
    encryptedContent = fernetKey.encrypt(content.encode()).decode()

    return encryptedContent

def encrypt(content):
    remoteKey = getRemoteKey()

    if remoteKey != None:
        # according to the specified index, decrypt, using the remote key, one of the encrypted passwords
        return encrypt_content(content, remoteKey)
    else:
        raise Exception("Remote key missing")
    
def get_rk_alias():
    encryptedRemoteKey = getEncryptedRemoteKey()

    return "****%s" % (encryptedRemoteKey[-4:])
