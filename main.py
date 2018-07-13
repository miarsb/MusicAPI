import reddit
import spotify
import argparse


def create_a_playlist(reddit_url, playlist_title):
    reddit_list = reddit.RedditAPI(reddit_url)
    titles = reddit_list.get_titles()

    spot = spotify.Spotify(titles, playlist_title)
    spot.playlist_creation()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Create Spotify playlists.')
    parser.add_argument('--reddit', '-r',
        choices=['day', 'week', 'month'],
        default='day',
        help='toggle to pull from reddit. select an interval' )
    parser.add_argument('--name', '-n',
        nargs='*',
        required=True,
        help='name the playlist')
    args = parser.parse_args()

    subreddit = '/r/listentothis'
    interval = args.reddit
    reddit_url = 'https://www.reddit.com{}/top/.json?t={}'.format(subreddit, interval)

    playlist_title = ' '.join(args.name)

    create_a_playlist(reddit_url, playlist_title)





