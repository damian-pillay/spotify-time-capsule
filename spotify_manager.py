from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
import spotipy
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID_SPOTIFY = os.environ["CLIENT_ID_SPOTIFY"]
CLIENT_SECRET_SPOTIFY = os.environ["CLIENT_SECRET_SPOTIFY"]
URL_REDIRECT = os.environ["URL_REDIRECT"]

class SpotifyManager:
    def __init__(self):
        self._client_id = CLIENT_ID_SPOTIFY
        self._secret = CLIENT_SECRET_SPOTIFY
        self._redirect = URL_REDIRECT
        
        auth_manager = SpotifyOAuth(
            client_id=self._client_id, 
            client_secret=self._secret, 
            redirect_uri=URL_REDIRECT, 
            scope="playlist-modify-private", 
            cache_path="./token.txt",
            show_dialog=True,
        )
       
        self.access_token = auth_manager.get_access_token()
        self.sp = spotipy.Spotify(auth_manager=auth_manager)
        self.user_id = self.sp.current_user()["id"]
        self.tracklist = []
        self.tracklist_uri = []
        self.date = None

    def get_top_100(self, date: str):
        self.date = date
        
        response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
        content = response.text.encode("utf-8")

        soup = BeautifulSoup(content, "html.parser")

        songs = soup.find_all("h3", id="title-of-a-story", class_="lrv-u-font-size-16")
        artists = soup.find_all("span", class_="u-letter-spacing-0021")
        song_names = [song.get_text().strip() for song in songs]
        artist_names = [artist.get_text().strip().lower() for artist in artists]
        
        for index, artist in enumerate(artist_names):
            for symbol in ["feat", "ft", "featuring", "&", "(", "and"]:
                if symbol in artist:
                    artist_names[index] = artist.split(symbol)[0].strip()
                    break

        billboard = []

        for artist, song in zip(artist_names, song_names):
            current_track = {
                "song": song,
                "artist": artist,
            }

            billboard.append(current_track)

        self.tracklist = billboard
    
    def get_track_uri(self) -> list: 

        print("\nYour playlist is generating...")
        
        for track in self.tracklist:
            try:
                result = self.sp.search(q=f"track: {track["song"]} artist: {track["artist"]}", limit=1, offset=1, type="track")
                uri = result["tracks"]["items"][0]["uri"]
                self.tracklist_uri.append(uri)
            except IndexError:
                pass
    
    def create_playlist(self):
        name = f"{self.date} Billboard"
        desc = f"The top 100 songs on the week of {self.date}"
        
        playlist = self.sp.user_playlist_create(user=self.user_id, name=name, public=False, description=desc)

        self.sp.user_playlist_add_tracks(self.user_id, playlist_id=playlist["id"], tracks=self.tracklist_uri)

        print("\nYour playlist has been generated!\nPlease open Spotify to view it\n\n")








        