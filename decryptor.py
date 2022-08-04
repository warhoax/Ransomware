from cryptography.fernet import Fernet

with open("key.key", "rb") as kf:
    key = kf.read()

fernet = Fernet(key)

with open("test.txt","rb") as tf:
    tf_bytes = tf.read()

    tf_bytes_dec = fernet.decrypt(tf_bytes)

with open("test.txt","wb") as tf:
    tf.write(tf_bytes_dec)