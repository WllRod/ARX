from keys import key
from src.Password_Hash.hash import get_hashed_password, check_password
import json

hashed_key  = get_hashed_password(key)

def json_read():
    with open(r'C:\Users\TI02\Desktop\Construtora\src\Password_Security\\config.json', 'r') as json_load:
        json_data   = json.load(json_load)
        json_load.close()
    return json_data

def json_write(json_data):
    with open(r'C:\Users\TI02\Desktop\Construtora\src\Password_Security\\config.json', 'w') as w:
        json.dump(json_data, w, indent=4)
    w.close()

public_key  = json_read()
public_key['public_key'] = hashed_key
json_write(public_key)

if(check_password(key, hashed_key)):
    public_key['public_key'] = key
    json_write(public_key)
