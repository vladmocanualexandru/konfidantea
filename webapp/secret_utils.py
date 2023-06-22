from cryptography.fernet import Fernet
import base64
from os import environ 

def decryptString(str, key):
    fernetKey = Fernet(base64.b64encode(key.encode('ascii')))
    return fernetKey.decrypt(str.encode()).decode()

def decrypt(encrypted_secret):
    try:
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
            return "ERROR-REMOTE-KEYS"


        # decrypt remote key using local key
        remoteKey = decryptString(encryptedRemoteKey, localKey)

        # according to the specified index, decrypt, using the remote key, one of the encrypted passwords
        decryptedPassword = decryptString(encrypted_secret, remoteKey)

        return decryptedPassword
    except Exception as e:
        # in case anything goes wrong, write ERROR to the temporary password file
        print(e)
        return "ERROR-UNKNOWN"

# def encrypt():
#     return ""