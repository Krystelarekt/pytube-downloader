import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import threading
from pytube import YouTube

# Set up Spotify API credentials
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

def get_playlist_tracks(playlist_url):
    playlist_id = playlist_url.split('/')[-1]  # Extract playlist ID from URL
    playlist = sp.playlist_tracks(playlist_id)

    songs = []
    for track in playlist['items']:
        song_name = track['track']['name']
        songs.append(song_name)
    return songs

def download_song(song_name):
    query = f"{song_name} audio"
    video = YouTube(query).streams.filter(only_audio=True).first()
    video.download(output_path='downloads', filename=song_name)

def download_songs_from_list(song_list):
    threads = []
    for song_name in song_list:
        thread = threading.Thread(target=download_song, args=(song_name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def main():
    print("Choose an option:")
    print("1. Enter a Spotify playlist link")
    print("2. Enter a song name")
    print("3. Select a file containing a list of songs")
    
    option = input("Enter your choice: ")

    if option == '1':
        playlist_url = input("Enter Spotify playlist URL: ")
        songs = get_playlist_tracks(playlist_url)
        download_songs_from_list(songs)
    elif option == '2':
        song_name = input("Enter song name: ")
        download_song(song_name)
    elif option == '3':
        file_path = input("Enter file path: ")
        with open(file_path, 'r') as file:
            song_list = [line.strip() for line in file]
            download_songs_from_list(song_list)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
