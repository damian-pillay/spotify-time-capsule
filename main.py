from date_manager import DateManager
from spotify_manager import SpotifyManager

# ------------- GET DATE ------------- #

date_manager = DateManager()
date = date_manager.get_date()

# ---------- SPOTIFY SETUP ----------- #

spotify = SpotifyManager()

# -------- WEBSCRAPE TOP 100 --------- #

spotify.get_top_100(date)

# ---------- MAKE PLAYLIST ----------- #

spotify.get_track_uri()
spotify.create_playlist()