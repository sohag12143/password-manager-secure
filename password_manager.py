#!/usr/bin/env python3
from cryptography.fernet import Fernet
import bcrypt
import json
from datetime import datetime

class SecurePasswordManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.credentials = {}
    
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def encrypt_credential(self, username, password):
        encrypted = self.cipher.encrypt(password.encode())
        self.credentials[username] = {
            'password': encrypted.decode(),
            'created': datetime.now().isoformat()
        }
        return True
    
    def decrypt_credential(self, username):
        if username in self.credentials:
            encrypted = self.credentials[username]['password']
            decrypted = self.cipher.decrypt(encrypted.encode()).decode()
            return decrypted
        return None
    
    def check_strength(self, password):
        score = 0
        if len(password) >= 8: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.islower() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in '!@#$%^&*' for c in password): score += 1
        
        strength = {0: 'Weak', 1: 'Fair', 2: 'Good', 3: 'Strong', 4: 'Very Strong', 5: 'Military Grade'}
        return strength.get(score, 'Unknown')
    
    def save_credentials(self, filename='creds.json'):
        with open(filename, 'w') as f:
            json.dump(self.credentials, f, indent=4)

if __name__ == '__main__':
    pm = SecurePasswordManager()
    pm.encrypt_credential('gmail', 'MySecure123!@#')
    pm.encrypt_credential('github', 'GitHub456$%^')
    print("Strength:", pm.check_strength('MySecure123!@#'))
    pm.save_credentials()
    print("[+] Credentials saved securely")
