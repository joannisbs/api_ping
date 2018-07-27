#import de ferramentas
import hashlib


# Trasnforma a data em MD5
def Cripto_md5 (data): 
    encryptedData = hashlib.md5()
    encryptedData.update(data)
    encryptedData = encryptedData.hexdigest()
    return str(encryptedData)
      
# Trasnforma a data em SHA256
def Cripto_sha256 (data): 
    encryptedData = hashlib.sha256()
    encryptedData.update(data)
    encryptedData = encryptedData.hexdigest()
    return str(encryptedData)
      
