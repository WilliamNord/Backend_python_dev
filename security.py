from cryptography.fernet import Fernet, InvalidToken
import os
from dotenv import load_dotenv

load_dotenv()  # Leser .env-filen
key = os.getenv("FERNET_KEY").encode()
cipher = Fernet(key)

def encrypt(text):
    return cipher.encrypt(text.encode())

def decrypt(data):
    try:
        return cipher.decrypt(data).decode()
    except InvalidToken:
        return None