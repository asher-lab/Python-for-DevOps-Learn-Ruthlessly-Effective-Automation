import os

import base64

#generate random password
print(base64.b64encode(os.urandom(64)).decode('utf-8'))
