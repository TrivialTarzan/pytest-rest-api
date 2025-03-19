import yaml
import os


class ConfigLoader:
    def __init__(self):
        self.config = self.load()
        self.config_protected = self.load_protected()
        
    @classmethod
    def load(cls):
        config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
        with open(config_path, "r") as file:
            return yaml.safe_load(file)    
    
    @classmethod
    def load_protected(cls):
        config_path = os.path.join(os.path.dirname(__file__), "protected.yaml")
        with open(config_path, "r") as file:
            return yaml.safe_load(file) 
    
    def email(self) -> str:
        return self.config_protected['my_user']['email']
    
    def password(self) -> str:
        return self.config_protected['my_user']['password']
    
    def first_name(self) -> str:
        return self.config_protected['my_user']['first_name']
    
    def last_name(self) -> str:
        return self.config_protected['my_user']['last_name']
    
    def id(self) -> str:
        return self.config_protected['my_user']['_id']
    
    def token(self) -> str:
        return self.config_protected['my_user']['token']
    
    def endpoint_login(self) -> str:
        return self.config['ContactList']['endpoints']['login_user']
    
    def endpoint_logout(self) -> str:
        return self.config['ContactList']['endpoints']['logout_user']
    
    def endpoint_delete_contact(self) -> str:
        return self.config['ContactList']['endpoints']['delete_contact']
    
    def endpoint_add_contact(self) -> str:
        return self.config['ContactList']['endpoints']['add_contact']
    
    def endpoint_add_user(self) -> str:
        return self.config['ContactList']['endpoints']['add_user']
    
    def endpoint_update_user(self) -> str:
        return self.config['ContactList']['endpoints']['update_user']
    
    def endpoint_get_contact_list(self) -> str:
        return self.config['ContactList']['endpoints']['get_contact_list']
    
    def contact1_first_name(self) -> str:
        return self.config['ContactList']['contact1']['first_name']
    
    def contact1_last_name(self) -> str:
        return self.config['ContactList']['contact1']['last_name']
    
    def contact1_birthdate(self) -> str:
        return self.config['ContactList']['contact1']['birthdate']
    
    def contact1_email(self) -> str:
        return self.config['ContactList']['contact1']['email']
    
    def contact1_phone(self) -> str:
        return self.config['ContactList']['contact1']['phone']
    
    def contact1_street1(self) -> str:
        return self.config['ContactList']['contact1']['street1']
    
    def contact1_street2(self) -> str:
        return self.config['ContactList']['contact1']['street2']
    
    def contact1_city(self) -> str:
        return self.config['ContactList']['contact1']['city']
    
    def contact1_state(self) -> str:
        return self.config['ContactList']['contact1']['stateProvince']
    
    def contact1_postal_code(self) -> str:
        return self.config['ContactList']['contact1']['postalCode']
    
    def contact1_country(self) -> str:
        return self.config['ContactList']['contact1']['country']
    
    def contact2_first_name(self) -> str:
        return self.config['ContactList']['contact2']['first_name']
    
    def contact2_last_name(self) -> str:
        return self.config['ContactList']['contact2']['last_name']
    
    def contact2_birthdate(self) -> str:
        return self.config['ContactList']['contact2']['birthdate']
    
    def contact2_email(self) -> str:
        return self.config['ContactList']['contact2']['email']
    
    def contact2_phone(self) -> str:
        return self.config['ContactList']['contact2']['phone']
    
    def contact2_street1(self) -> str:
        return self.config['ContactList']['contact2']['street1']
    
    def contact2_street2(self) -> str:
        return self.config['ContactList']['contact2']['street2']
    
    def contact2_city(self) -> str:
        return self.config['ContactList']['contact2']['city']
    
    def contact2_state(self) -> str:
        return self.config['ContactList']['contact2']['stateProvince']
    
    def contact2_postal_code(self) -> str:
        return self.config['ContactList']['contact2']['postalCode']
    
    def contact2_country(self) -> str:
        return self.config['ContactList']['contact2']['country']
       
        