from cryptography.fernet import Fernet
import os
import glob

#key = Fernet.generate_key()

#with open("key.key", "wb") as keyFile:
 #   keyFile.write(key)

#fernet = Fernet(key)

#with open("test.txt", "rb") as tf:
 #   tf_byte = tf.read()

#tf_bytes_enc = fernet.encrypt(tf_byte)

#with open("test.txt", "wb") as tf:
 #    tf.write(tf_bytes_enc)

home_dir =  os.path.expanduser("~")
#print(home_dir)
files = glob.glob(f'{home_dir}\\creds\\**\\*.*', recursive=True)

for file in files:
    print(file)