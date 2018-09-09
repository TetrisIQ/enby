from tcpRequest import log
from tcpRequest import requests


class EmbyAPI:
    HEADER = {'Authorization' : 'Emby', 'Client':'Android', 'Device':'Enigma2', 'Version' : '1.0.0.0', 'X-Emby-Token': '928cb992239d475e9a5e5be243d60a0c', }

    def __init__(self, **kwargs):
        self.serverAdress = "http://192.168.178.23:8096"
        self.userId = "ef50e90b79294dec9663876108771f90"
        self.serverName = "EmbyServer"
        self.tcp = requests(HEADER=self.HEADER)
        # init tcpRequest

    def findServer(self):
        print ""
        #u = UDPSocket('255.255.255.255')
        #u.send("who is EmbyServer?")
        #json = u.reciveJson()
        #return json

    def browseDashboard(self):
        api_url = self.serverAdress + "/Users/{}/Views".format(self.userId)
        return self.tcp.get(api_url)

    def browseIntoFolder(self, parentId):
        api_url = self.serverAdress + '/Users/{}/Items?parentId={}'.format(self.userId, parentId)
        return self.tcp.get(url=api_url)

    def displayAllMovies(self):
        api_url = self.serverAdress + '/Users/{}/Items?Recursive=true&IncludeItemTypes=Movie'.format(
            self.userId)
        return self.tcp.get(url=api_url)

    def displayLastMovies(self, amount):
        # api_url = self.serverAdress + '/Users/{}/Items/Latest?IncludeItemTypes=Movie&Limit={}&IsPlayed=false'.format(
        #   self.serverId, amount)
        print "TODO: !!!!!"
        return "TODO: !!!!!"

    def downloadImg(self, id, type, index, direcotryItemName, **kwargs):
        paramString = ''
        if kwargs:
            for key, value in kwargs.items():
                paramString += str(key) + '=' + str(value) + '&'
        api_url = self.serverAdress + '/Items/{}/Images/{}/{}?{}'.format(id, type, index, paramString[:len(paramString)-1])
        #try:
        #    self.request.download(api_url, direcotryItemName)
        #except urllib.error.HTTPError as error:
         #   print(str(error) + "\t\tPicture not Found")

    def test(self, amount, parentId):
        api_url = self.serverAdress + '/Users/{}/Items/Latest?parentId={}'.format(
            self.userId, parentId)
        return self.tcp.get(url=api_url)

    def streamClip(self, id):
        api_url = self.serverAdress + '/Videos/{}/stream?'.format(id)
        log('[Debug:\t\t ' + api_url + 'api_key=0b2c3d535f184b82b77e28bff4dbd729')  # debug



