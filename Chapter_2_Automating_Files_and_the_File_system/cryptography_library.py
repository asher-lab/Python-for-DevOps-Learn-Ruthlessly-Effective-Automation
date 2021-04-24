from cryptography.fernet import Fernet
key = Fernet.generate_key()

# generating key
print(f"Key : {key}")

# encrypting data
f = Fernet(key)
message = b"This is a confidential ages: 9712sd"
encrypted = f.encrypt(message)

#printing the encrypted message
print(f"Message encrypted: {encrypted}")

#decrypting data
f = Fernet(key)
decrypted = f.decrypt(encrypted)

#printing the decrypted message
print(f"Message decrypted: {decrypted}")
