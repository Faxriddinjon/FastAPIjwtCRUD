from passlib.context import CryptContext


pwd_cxd=CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxd.hash(password)
    
    def verify(plain_password, hashed_password):
        return pwd_cxd.verify(plain_password, hashed_password)