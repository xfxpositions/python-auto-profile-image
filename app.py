import json
from instagrapi import Client
import os
from datetime import datetime
import time
from dotenv import load_dotenv
load_dotenv()
cl = Client()
username = os.environ.get("user")
password = os.environ.get("password")
twofa = input("enter your 2fa code (message not allowed, you should use another 2fa)")
img_dir = dir_path = os.getcwd() + "/ig-pp"
cl.login(username, password,verification_code=twofa)
print("logined!")
while True:

    f = open('data.json')

    data = json.load(f)
    counter = data["counter"]

    last_update = data["lastUpdate"]
    if last_update > 2250:
        last_update = 1
    time_diffrence = last_update = int(datetime.now().timestamp() * 1000)

    def start():
        
        res = []
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                res.append(path)
        my_image = res[counter]

        
        img_location = os.path.join(img_dir, my_image)

        cl.account_change_picture(img_location)
        print("updated!")
        json_to_write = {
            "counter" : counter+1,
            "lastUpdate" : int(datetime.now().timestamp() * 1000)
        }
        json_object = json.dumps(json_to_write, indent=4)
        with open("data.json", "w") as outfile:
            outfile.write(json_object)
        print("writed!" + res["counter"])
    

    
    f.close()
    time.sleep(30)


