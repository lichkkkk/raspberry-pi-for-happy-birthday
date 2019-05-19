
from __future__ import print_function

import json
import base64
import urllib2

class HTTPClient:

    SERVER_ADDR_ = 'http://192.168.1.154:8080/test'
    
    def get(self):
        raw_response = urllib2.urlopen(self.SERVER_ADDR_)
        msg = json.loads(raw_response.read().decode())
        
        text = msg['text']
        img_encoded = msg['img']
        with open('img', 'wb') as img_file:
          img_file.write(base64.b64decode(img_encoded))
        
        res = {}
        res['text'] = text
        res['img'] = 'img'
        return res


"""
Test
"""
"""
http = HTTPClient()
print(http.get())
"""
