import sys

from cryptography.fernet import Fernet
import os
import glob
from cryptography.fernet import InvalidToken

home_dir =  os.path.expanduser("~")
with open("key.key", "rb") as kf:
    key = kf.read()

fernet = Fernet(key)

files = glob.glob(f'{home_dir}\\creds\\**\\*.*', recursive=True)

for file in files:
    try:
        with open(file,"rb") as tf:
            tf_bytes = tf.read()
    except:
        pass
    try:
        tf_bytes_dec = fernet.decrypt(tf_bytes)
    except InvalidToken:
        print(" Error Decrption")
        sys.exit()

    with open(file,"wb") as tf:
        tf.write(tf_bytes_dec)

