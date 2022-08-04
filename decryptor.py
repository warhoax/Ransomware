from cryptography.fernet import Fernet
import os
import glob

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
    except Exception as e:
        print("error in decrypting file: ", file, "is ", e)
        pass
    with open(file,"wb") as tf:
        tf.write(tf_bytes_dec)

