from passlib.context import CryptContext

# password encryptionn 
pwd_context = CryptContext(schemes=["bcrypt"])

class Hashing :
    def hash_password(password : str):
        return pwd_context.hash(password)
    
    def verify(hashedPassword : str , plainPassword : str):
        return pwd_context.verify(plainPassword , hashedPassword)