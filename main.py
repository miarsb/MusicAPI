import reddit
import spotify

class Main:

    def __init__(self, subreddit, interval):
        self.playlistTitle = subreddit+" playlist - "+interval
        self.redditList = reddit.RedditAPI('https://www.reddit.com'+subreddit+'/top/.json?t='+interval)
        spotify.Spotify(self.redditList, self.playlistTitle)

Main('/r/listentothis', 'day')