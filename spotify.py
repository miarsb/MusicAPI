import spotipy
import spotipy.util as util

class Spotify:

    def __init__(self, redditList, playlistTitle, spotifyUser):
        self.playlistTitle = playlistTitle
        #self.tokenFile = open('./token.txt', 'r')
        #self.token = self.tokenFile.read()
        #self.spot = spotipy.Spotify(auth=self.token)

        self.spotifyUser = spotifyUser
        self.auth(self.spotifyUser)
        self.redditList = redditList

        #username is required to authorize developer api account for playlist creation on personal account.
        #call the auth method to run a test call to confirm whether we're authorized and if not, reauthorize


        #proceeding with track lookup using the reddit list
        self.lookUpList()
        #creating the list with the spotify track URLs we got in lookUpList()
        self.playlistCreation()

    def lookUpList(self):
        self.spotifyLookUp = []
        self.listOfUrls = []
        #search for each "artist - title" in the list from RedditAPI and append the spotify result to new list
        for track in self.redditList.formattedTitles:
            self.spotifyLookUp.append(self.spot.search(q=track, type='track'))

        #breakdown the search results to just the the track url and append to new list
        for item in self.spotifyLookUp:
            #check to see if we got a result
            if item['tracks']['items']:
                #if we got a result then grab the URL for the track from the FIRST result[0] and append to final list
                self.listOfUrls.append(item['tracks']['items'][0]['external_urls']['spotify'])

    def playlistCreation(self):

        new_playlist = self.spot.user_playlist_create("1213766491", self.playlistTitle, public=True)
        playlist_ID = new_playlist['id']
        self.spot.user_playlist_add_tracks('1213766491', playlist_ID, self.listOfUrls)

    def auth(self, username):

        secretFile = open('./secret.txt', 'r')
        secretID = secretFile.read()
        self.tokenFile = open('./token.txt', 'r')
        self.token = self.tokenFile.read()
        self.spot = spotipy.Spotify(auth=self.token)

        try:
            self.spot.search(q='test', type='track')
        except spotipy.client.SpotifyException:
            self.writeToToken = self.tokenFile = open('./token.txt', 'w')
            self.writeToToken.write(util.prompt_for_user_token(username,'playlist-modify-public',client_id='073c1bc21d634eff9a9452850a646cde',client_secret=secretID,redirect_uri='http://www.example.com/'))
            self.auth(self.spotifyUser)

#Spotify()

