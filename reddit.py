import requests
import re


class RedditAPI:

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def pull_json_data(self):
        reddit_data = requests.get(self.endpoint, headers = {'User-agent': 'BrandoBot'})
        return reddit_data.json()

    def get_titles(self):
        data = self.pull_json_data()
        titles = []
        formatted_titles = []
        for title in data['data']['children']:
            titles.append(re.split('-|\[', title['data']['title']))

        for i in range(len(titles)):
            remove_empty_strings = (list(filter(None, titles[i])))
            formatted_titles.append("-".join(remove_empty_strings[:2]))
        return formatted_titles

