import reddit
import spotify

class Main:

    def __init__(self, subreddit, interval, username):
        self.playlistTitle = subreddit+" playlist - "+interval
        self.redditList = reddit.RedditAPI('https://www.reddit.com'+subreddit+'/top/.json?t='+interval)
        #print(self.redditList.formattedTitles)
        spotify.Spotify(self.redditList, self.playlistTitle, username)

Main('/r/listentothis', 'day', 'Branden Miars')