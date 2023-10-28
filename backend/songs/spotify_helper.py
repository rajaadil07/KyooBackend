import requests
import base64
from decouple import config

from .models import Song

SPOTIFY_CLIENT_ID = config('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')

def get_access_token():
    encoded = base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {encoded}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return response.json().get('access_token')

def create_song_instance_from_spotify(data):
    """
    Creates a Song instance from the provided Spotify data without saving to database.
    """
    song = Song(
        title=data['name'],
        artist=', '.join([artist['name'] for artist in data['artists']]),
        album=data['album']['name'],
        album_cover=data['album']['images'][0]['url'] if data['album']['images'] else None,
        spotify_url=data['external_urls']['spotify']
    )
    return song

def search_track(query):
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f"https://api.spotify.com/v1/search?q={query}&type=track", headers=headers)
    spotify_data = response.json()

    songs = [create_song_instance_from_spotify(item) for item in spotify_data['tracks']['items']]
    
    return songs
