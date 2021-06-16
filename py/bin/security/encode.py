from argon2 import PasswordHasher
from security.encrypt import PasswordCipher

class Encode:
    ph = PasswordHasher()
    pc = PasswordCipher()

    def hash_password(self, password):
        password = self.pc.encrypt(password)
        return self.ph.hash(password)

    def verify(self, hash, password):
        try:
            return self.ph.verify(hash, self.pc.encrypt(password))
        except:
            return False
