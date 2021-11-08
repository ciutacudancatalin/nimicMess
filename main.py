
from cryptography.fernet import Fernet

class nimicClass():
    def __init__(self):
        self.key = self.load_key()

    def generate_key(self):
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        """
        Loads the key named `secret.key` from the current directory.
        """
        return open("secret.key", "rb").read()

    def encryptMessage(self, message):
        encodedMessage = message.encode()
        f = Fernet(self.key)
        return f.encrypt(encodedMessage)

    def decryptMessage(self, encryptedMessage):
        """
        Decrypts an encrypted message
        """

        f = Fernet(self.key)
        decryptedMessage = f.decrypt(encryptedMessage)


print(nimicClass().decryptMessage(nimicClass().encryptMessage("mesaj inc riptat lol")))
print('asdf1')