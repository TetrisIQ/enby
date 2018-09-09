from urllib2 import Request, urlopen
import json

debug = True

class requests:

    HEADER = {'User-Agent': 'Python client'}

    def __init__(self, HEADER):
        self.HEADER = HEADER

    def get(self, url):
        if debug:
            log('[Debug:\t\t '+url + '&api_key=0b2c3d535f184b82b77e28bff4dbd729')    # debug
        q = Request(url)
        for key, val in self.HEADER.items():
            q.headers
            q.add_header(key, val)
        return bty(urlopen(q).read())

    def post(self, url, payload):
        log("TODO: !!!!!!!")

def bty(byte):
    my_json = byte.decode('utf8')
    try:
        return json.loads(my_json)
    except json.decoder.JSONDecodeError:
        log("Json Decode Failed - please contract https://github.com/tetrisiq")


def log(msg):
    with open('log.txt', 'a') as log:
        log.write(msg+'\n')
    print msg
