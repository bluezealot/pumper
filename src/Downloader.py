import requests


# Download image files with specified json data
# which is retrieved from Google search engine api.
class Downloader:
    # Download image method.
    def download(self, json_data):
        for item in json_data['items']:
            item['link']

    def __downloadafile(self, link):
        response = requests.get(link)
