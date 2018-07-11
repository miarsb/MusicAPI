import requests
import re

class RedditAPI:

    def __init__(self, endpoint):
        self.endpoint = endpoint


    def pullData(self):
        r = requests.get(self.endpoint, headers = {'User-agent': 'BrandoBot'})
        return r.json()


    def getTitles(self):
        data = self.pullData()
        titles = []
        formattedTitles = []
        for title in data['data']['children']:
            titles.append(re.split('-|\[', title['data']['title']))

        for i in range(len(titles)):
            remove_empty_strings = (list(filter(None, titles[i])))
            formattedTitles.append("-".join(remove_empty_strings[:2]))
        return formattedTitles

#RedditAPI('https://www.reddit.com/r/listentothis/top/.json')