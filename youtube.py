import requests
import configparser


class YoutubeAPI:

    def __init__(self, endpoint):
        self.video_id = endpoint.split('=')[1]

        config = configparser.ConfigParser()
        config.read('music_config.ini')
        self.api_key = config.get('youtube', 'key')

    def pulljsondata(self):

        youtube_data = requests.get('https://www.googleapis.com/youtube/v3/videos?id={}&key={}&part=snippet'
                                    .format(self.video_id, self.api_key))
        return youtube_data.json()

    def get_titles(self):

        youtube_json = self.pulljsondata()
        title = youtube_json['items'][0]['snippet']['title']
        return(title)
