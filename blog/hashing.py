from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def getBcryptPassword(password):
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword

    def verify(hashedPassword, plainPassword):
        return pwd_cxt.verify(plainPassword, hashedPassword)
