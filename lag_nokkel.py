from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Din nye Fernet-nøkkel:")
print(key.decode())