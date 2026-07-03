import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json
#print(json.dumps(NOW_PLAYING["item"], indent=2))
load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv ("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope="user-read-playback-state"))


NOW_PLAYING = sp.currently_playing()
print(NOW_PLAYING["item"]["name"])
print(json.dumps(NOW_PLAYING["item"], indent=2))

#Importeer os (ingebouwd in Python)
#2. Importeer load_dotenv uit de dotenv package
#3. Roep load_dotenv() aan zodat de waarden uit .env geladen worden
