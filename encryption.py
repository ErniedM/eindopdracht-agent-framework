from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key_path):
        with open(key_path, "rb") as file:
            key = file.read()
        self.fernet = Fernet(key)

    def encrypt_file(self, file_path):
        with open(file_path, "rb") as file:
            data = file.read()
        encrypted_data = self.fernet.encrypt(data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path, output_path):
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = self.fernet.decrypt(encrypted_data)
        with open(output_path, "wb") as file:
            file.write(decrypted_data)
    
    # def __init__(self, key_path):
    #     with open(key_path, "rb") as file:
    #         key = file.read()
    #     self.fernet = Fernet(key)

    # def encrypt(self, data):
    #     encrypted_data = self.fernet.encrypt(data.encode())
    #     return encrypted_data

    # def decrypt(self, encrypted_data):
    #     decrypted_data = self.fernet.decrypt(encrypted_data)
    #     return decrypted_data.decode()
