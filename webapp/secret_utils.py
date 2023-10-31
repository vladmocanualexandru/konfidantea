from cryptography.fernet import Fernet
import base64
from os import environ 

def decryptString(str, key):
    fernetKey = Fernet(base64.b64encode(key.encode('ascii')))
    return fernetKey.decrypt(str.encode()).decode()

def getRemoteKey():
    # read local key (not encrypted)
    localKey = environ.get('KONFIDANTEA_LOCAL_KEY')
    
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

    if encryptedRemoteKey == None:
        print('Unable to find a remote key!')
        return None
    else:
        # decrypt remote key using local key
        remoteKey = decryptString(encryptedRemoteKey, localKey)

        return remoteKey


def decrypt(encrypted_secret):
    try:
        remoteKey = getRemoteKey()

        if remoteKey != None:
            # according to the specified index, decrypt, using the remote key, one of the encrypted passwords
            decryptedPassword = decryptString(encrypted_secret, remoteKey)

            return decryptedPassword
        else:
            return "ERROR-REMOTE-KEY-MISSING"
    except Exception as e:
        # in case anything goes wrong, write ERROR to the temporary password file
        print(e)
        return "ERROR-UNKNOWN"
    
def encrypt(content):
    remoteKey = getRemoteKey()

    if remoteKey != None:
        # according to the specified index, decrypt, using the remote key, one of the encrypted passwords
        fernetKey = Fernet(base64.b64encode(remoteKey.encode('ascii')))
        encryptedContent = fernetKey.encrypt(content.encode()).decode()

        return encryptedContent
    else:
        raise Exception("Remote key missing")