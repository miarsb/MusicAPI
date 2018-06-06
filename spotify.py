import spotipy
import spotipy.util as util

class Spotify:

    def __init__(self, redditList, playlistTitle):
        self.playlistTitle = playlistTitle
        self.tokenFile = open('./token.txt', 'r')
        self.token = self.tokenFile.read()
        # print(self.token)
        self.spot = spotipy.Spotify(auth=self.token)

        self.redditList = redditList

        self.auth('Branden Miars')
        self.lookUpList()
        self.playlistCreation()

    def lookUpList(self):
        self.spotifyLookUp = []
        self.listOfUrls = []
        #search for each "artist - title" in the list from RedditAPI and append the search result to new list
        for track in self.redditList.formattedTitles:
            self.spotifyLookUp.append(self.spot.search(q=track, type='track'))
        #breakdown the search results to just the the track url and append to new list
        for item in self.spotifyLookUp:
            #check to see if we got a result
            if item['tracks']['items']:
                #if we got a result then grab the URL for the track from the FIRST result[0] and append to final list
                self.listOfUrls.append(item['tracks']['items'][0]['external_urls']['spotify'])
        #print(self.listOfUrls)



    def playlistCreation(self):
        self.spot.user_playlist_create("1213766491", self.playlistTitle, public=True)
        user_playlists = self.spot.user_playlists("1213766491", limit=50, offset=0)
        playlist_ID = ''
        for i in range(len(user_playlists["items"])):
            if user_playlists["items"][i]["name"] == self.playlistTitle:
                playlist_ID = user_playlists["items"][i]["id"]
        self.spot.user_playlist_add_tracks('1213766491', playlist_ID, self.listOfUrls)

    def auth(self, username):
        try:
            self.spot.search(q='test', type='track')
        except Exception as e:
            self.writeToToken = self.tokenFile = open('./token.txt', 'w')
            self.writeToToken.write(util.prompt_for_user_token(username,'playlist-modify-public',client_id='073c1bc21d634eff9a9452850a646cde',client_secret='7b695fca861842e8bf54f3b38dd81563',redirect_uri='http://www.example.com/'))

#Spotify()

#util.prompt_for_user_token('Branden Miars','playlist-modify-public',client_id='073c1bc21d634eff9a9452850a646cde',client_secret='7b695fca861842e8bf54f3b38dd81563',redirect_uri='http://www.example.com/')