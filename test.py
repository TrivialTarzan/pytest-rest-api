from config.config_loader import load_config
from api_client import ApiClient

config = load_config()

def endpoint():
    return config['ContactList']['endpoints']['login_user']

def email():
    return config['ContactList']['first_user']['first_name']

def password():
    return config['ContactList']['first_user']['password']


print(endpoint())
print(email())
print(password())
