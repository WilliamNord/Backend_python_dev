from cryptography.fernet import Fernet
import os

key = b'Z_iFTXZ67d-zapz-_0_kj9Pmhc8DM41KNgwqm8V9MCI='
cipher = Fernet(key)

def encrypt(text):
    return cipher.encrypt(text.encode())

def decrypt(data):
    return cipher.decrypt(data).decode()