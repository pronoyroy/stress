import os
import threading

def callurl():
    os.system("curl Kinesistest-env.hcuzc5nyud.us-east-1.elasticbeanstalk.com")

while True:
    t = threading.Thread(target=callurl)
    t.start()


