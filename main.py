import reddit
import spotify

subreddit = '/r/listentothis'
interval = 'day'
username = 'Branden Miars'

# TODO: python arg parse

if __name__ == '__main__':
    playlist_title = '{} playlist - {}'.format(subreddit, interval)
    reddit_list = reddit.RedditAPI('https://www.reddit.com{}/top/.json?t={}'.format(subreddit, interval))
    titles = reddit_list.get_titles()
    
    # TODO spotify should not need reddlit list. limit what spotify knows about reddit Class
    spotify = spotify.Spotify(titles, playlist_title, username)
    # creating the list with the spotify track URLs we got in lookUpList()
    spotify.playlist_creation()