from src.Requester import Requester
from src.Downloader import Downloader

if __name__ == '__main__':
    req = Requester()
    req.ApiKey = 'Your api key' # Note: Replace to your api key.
    req.EngineID = 'Your search engine' # Note:  Replace to your search engine.
    start_num = 1
    while start_num < 100:
        res_json = req.getdata('toyota+aqua+front+view', start_num)
        down = Downloader()
        down.download(res_json)
        start_num += 10
