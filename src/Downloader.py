import requests


# Download image files with specified json data
# which is retrieved from Google search engine api.
class Downloader:
    # Download image method.
    def download(self, json_data):
        for item in json_data['items']:
            self.__downloadafile(item['link'])

    def __downloadafile(self, link):
        slashindex = link.rindex('/')
        questionindex = len(link)
        try:
            questionindex = link.index('?')
        except Exception as e:
            print(e)
        filename = link[slashindex + 1: questionindex]
        try:
            response = requests.get(link, timeout=5)
            open('/home/username/work/git/pumper/aqua/' + filename, 'wb').write(response.content) # Note: Replace to your folder.
        except Exception as e:
            print(e)
