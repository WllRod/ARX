import bcrypt
import base64

def get_hashed_password(plain_text_password):
    

    return base64.b64encode(bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())).decode('utf-8')

def check_password(plain_text_password, hashed_password):
    
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), base64.b64decode(hashed_password))
