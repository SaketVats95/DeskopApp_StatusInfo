import requests
import urllib.request
from bs4 import BeautifulSoup

class Jio_DataInfo():
    def __init__(self):
        self.url = 'http://jiofi.local.html/cgi-bin/en-jio/mStatus.html'
    
    def sendRequest(self):
        #url = 
        self.response = requests.get(self.url)
    
    def ifResponseOk(self):
        return True if self.response.status_code == 200 else False

    def createBeautifulSoupObj(self):
        self.soup_jio_ResData = BeautifulSoup(self.response.text, 'html.parser') 
    
    def getSelectedData(self, validIdList):
        validData = []
        if self.ifResponseOk():
            self.createBeautifulSoupObj()
            labels = self.soup_jio_ResData.findAll('label')
            for label in labels:
                if label.has_attr('id') and label['id'] in validIdList:
                    tempData = (label['id'], label.decode_contents())
                    validData.append(tempData)
        
        return validData