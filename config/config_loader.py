import yaml
import os


class ConfigLoader:
    def __init__(self):
        self.config = self.load()
        
    @staticmethod
    def load():
        config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
        with open(config_path, "r") as file:
            return yaml.safe_load(file)       
        
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
    
    def contact1_first_name(self):
        return self.config['ContactList']['contact1']['first_name']
    
    def contact1_last_name(self):
        return self.config['ContactList']['contact1']['last_name']
    
    def contact1_birthdate(self):
        return self.config['ContactList']['contact1']['birthdate']
    
    def contact1_email(self):
        return self.config['ContactList']['contact1']['email']
    
    def contact1_phone(self):
        return self.config['ContactList']['contact1']['phone']
    
    def contact1_street1(self):
        return self.config['ContactList']['contact1']['street1']
    
    def contact1_street2(self):
        return self.config['ContactList']['contact1']['street2']
    
    def contact1_city(self):
        return self.config['ContactList']['contact1']['city']
    
    def contact1_state(self):
        return self.config['ContactList']['contact1']['stateProvince']
    
    def contact1_postal_code(self):
        return self.config['ContactList']['contact1']['postalCode']
    
    def contact1_country(self):
        return self.config['ContactList']['contact1']['country']
    
    def contact2_first_name(self):
        return self.config['ContactList']['contact2']['first_name']
    
    def contact2_last_name(self):
        return self.config['ContactList']['contact2']['last_name']
    
    def contact2_birthdate(self):
        return self.config['ContactList']['contact2']['birthdate']
    
    def contact2_email(self):
        return self.config['ContactList']['contact2']['email']
    
    def contact2_phone(self):
        return self.config['ContactList']['contact2']['phone']
    
    def contact2_street1(self):
        return self.config['ContactList']['contact2']['street1']
    
    def contact2_street2(self):
        return self.config['ContactList']['contact2']['street2']
    
    def contact2_city(self):
        return self.config['ContactList']['contact2']['city']
    
    def contact2_state(self):
        return self.config['ContactList']['contact2']['stateProvince']
    
    def contact2_postal_code(self):
        return self.config['ContactList']['contact2']['postalCode']
    
    def contact2_country(self):
        return self.config['ContactList']['contact2']['country']
       
        