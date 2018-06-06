import requests
import re

class RedditAPI:

    def __init__(self, endpoint):
        self.pullData(endpoint)
        self.getTitles()
        #print(self.formattedTitles)
            #print(track)

    def pullData(self, endpoint):
        r = requests.get(endpoint, headers = {'User-agent': 'BrandoBot'})
        self.data = r.json()
        self.titles = []

    def getTitles(self):
        self.formattedTitles = []
        for title in self.data['data']['children']:
            self.titles.append(re.split('-|\[', title['data']['title']))

        for i in range(len(self.titles)):
            remove_empty_strings = (list(filter(None, self.titles[i])))
            self.formattedTitles.append("-".join(remove_empty_strings[:2]))


#RedditAPI('https://www.reddit.com/r/listentothis/top/.json')