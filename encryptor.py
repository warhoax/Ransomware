from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.key", "wb") as keyFile:
    keyFile.write(key)

fernet = Fernet(key)

with open("test.txt", "rb") as tf:
    tf_byte = tf.read()

tf_bytes_enc = fernet.encrypt(tf_byte)

with open("test.txt", "wb") as tf:
     tf.write(tf_bytes_enc)

