import hashlib

def GeraTokenRetorno(psw,time):
    string = psw + time
    token = hashlib.sha256()
    token.update(string)
    token = str(token.hexdigest())
    return token

def GeraTokenSession(token,nivel,user):
    pass
    