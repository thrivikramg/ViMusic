import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from youtubesearchpython import VideosSearch
import os
client_id = '****' #enter ur spotify client id
client_secret = '*****' #enter ur spotify client secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)  #check the tutorial from spotify developer website

playlist_url = input('Add link: ')
playlist_id = playlist_url.split('/')[-1].split('?')[0] 
playlist_uri = 'spotify:playlist:' + playlist_id
print("Playlist URI:", playlist_uri)
results = sp.playlist_tracks(playlist_uri)

def download_songs(song_name):
    search_results = VideosSearch(song_name + " audio", limit=1)
    video_url = search_results.result()['result'][0]['link']

    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file_path = audio_stream.download(output_path='downloads/', filename=song_name) #saves as .file


    file_path = f"downloads/{song_name}.mp3"#saves as .mp3
    os.rename(audio_file_path, file_path)
songs = []
for track in results['items']:
    songs.append(track['track']['name'])

i=0
for song_name in songs:
    print(i, song_name)
    download_songs(song_name)
    i += 1
