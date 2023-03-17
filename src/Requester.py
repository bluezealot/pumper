import requests


# This class is used to get images from Google search engine api with
# user specified search keyword.
class Requester:
    # Constructor
    def __init__(self):
        self.GoogleUrl = 'https://customsearch.googleapis.com/customsearch/v1'
        self.ApiKey = 'Your Key'
        self.EngineID = 'Your engine id'

    # get json data from Google search engine api
    def getdata(self, keyword, startnum):
        params = {
            'key': self.ApiKey,
            'cx': self.EngineID,
            'start': startnum,
            'q': keyword,
            'searchType': 'image'
        }
        ret = requests.get(self.GoogleUrl, params).json()
        return ret
