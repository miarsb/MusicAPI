import spotipy
import spotipy.util as util
import configparser
import reddit

class Spotify:

    def __init__(self, track_list, playlistTitle):
        self.playlistTitle = playlistTitle
        self.track_list = track_list

    # username is required to authorize developer api account for playlist creation on personal account.
    # call the auth method to run a test call to confirm whether we're authorized and if not, reauthorize
    def auth(self):
        # open config file, read in contents, and assign necessary variables for authentication
        config = configparser.ConfigParser()
        config.read('spotify_config.ini')
        # secret key is constant
        secret_key = config.get('spotify', 'secret')
        token = config.get('spotify', 'token')
        self.spot = spotipy.Spotify(auth=token)



        try:
            self.spot.search(q='test', type='track')
        except spotipy.client.SpotifyException:
            config['spotify']['token'] = util.prompt_for_user_token('BrandoApp','playlist-modify-public',client_id='073c1bc21d634eff9a9452850a646cde',client_secret=secret_key,redirect_uri='http://www.example.com/')
            with open('spotify_config.ini', 'w') as configfile:
                config.write(configfile)
            self.auth()



    def lookup_list(self):
        spotify_lookup = []
        list_of_urls = []
        # search for each "artist - title" in the list from RedditAPI and append the spotify result to new list
        for track in self.track_list:
            spotify_lookup.append(self.spot.search(q=track, type='track'))

        # breakdown the search results to just the the track url and append to new list
        for item in spotify_lookup:
            # check to see if we got a result
            if item['tracks']['items']:
                # if we got a result then grab the URL for the track from the FIRST result[0] and append to final list
                list_of_urls.append(item['tracks']['items'][0]['external_urls']['spotify'])
        return list_of_urls

    def playlist_creation(self):
        self.auth()
        spotify_track_list = self.lookup_list()
        new_playlist = self.spot.user_playlist_create("1213766491", self.playlistTitle, public=True)
        playlist_identification = new_playlist['id']
        self.spot.user_playlist_add_tracks('1213766491', playlist_identification, spotify_track_list)
