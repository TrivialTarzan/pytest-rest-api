import yaml
import os

# def load():
#     config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
#     with open(config_path, "r") as file:
#         return yaml.safe_load(file)

class ConfigLoader:
    def __init__(self):
        self.config = self.load()
        
    def endpoint(self):
        return self.config['ContactList']['endpoints']['login_user']
    
    def email(self):
        return self.config['ContactList']['first_user']['email']
    
    def password(self):
        return self.config['ContactList']['first_user']['password']
    
    def first_name(self):
        return self.config['ContactList']['first_user']['first_name']
    
    def last_name(self):
        return self.config['ContactList']['first_user']['last_name']
    
    def id(self):
        return self.config['ContactList']['first_user']['id']
    
    def token(self):
        return self.config['ContactList']['first_user']['token']
    
    @staticmethod
    def load():
        config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
        with open(config_path, "r") as file:
            return yaml.safe_load(file)      
        