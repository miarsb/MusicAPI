import reddit
import spotify

subreddit = '/r/listentothis'
interval  = 'day'
username  = 'Branden Miars'

#TO DO: python arg parse

if __name__ == '__main__':
    playlistTitle = '{} playlist - {}'.format(subreddit, interval)
    redditList = reddit.RedditAPI('https://www.reddit.com{}/top/.json?t={}'.format(subreddit, interval))
    titles = redditList.getTitles()


    #print(redditList.formattedTitles)

    #TODO spotify should not need reddlit list. limit what spotify knows about reddit Class
    spotify = spotify.Spotify(titles, playlistTitle, username)

    # username is required to authorize developer api account for playlist creation on personal account.
    # call the auth method to run a test call to confirm whether we're authorized and if not, reauthorize




    # creating the list with the spotify track URLs we got in lookUpList()
    spotify.playlistCreation()