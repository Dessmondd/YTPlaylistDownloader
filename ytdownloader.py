from pytube import Playlist
import os

input = input("Please, enter playlist ID: ")
# Replace 'playlist_url' with the URL of the YouTube playlist you want to download
playlist_url = f'https://www.youtube.com/playlist?list={input}'


playlist = Playlist(playlist_url)


os.makedirs('./downloads', exist_ok=True)

for video in playlist.videos:
    print(f"Downloading {video.title}...")
    stream = video.streams.filter(only_audio=True).first()
    stream.download(output_path='./downloads', filename=video.title + ".mp3")
    print(f"{video.title} downloaded successfully!")

print("Playlist downloaded successfully!")