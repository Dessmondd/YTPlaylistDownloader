from pytube import Playlist
import os
import re
import ffmpeg

# Function to remove special characters from a string
def remove_special_characters(string):
    return re.sub(r'[\\/:"*?<>|]', '', string)

# Prompt the user to enter the playlist ID
input_id = input("Enter the playlist ID: ")

# Construct the playlist URL
playlist_url = f'https://www.youtube.com/playlist?list={input_id}'

# Create a Playlist object
playlist = Playlist(playlist_url)

# Create a directory to save the MP3 files
output_dir = os.path.join('.', 'downloads')
os.makedirs(output_dir, exist_ok=True)

for video in playlist.videos:
    print(f"Downloading {video.title}...")
    stream = video.streams.filter(file_extension='mp4', only_video=True).first()
    
    # Remove special characters from the video title for the filename
    sanitized_title = remove_special_characters(video.title + '.mp3')
    
    stream.download(output_path=output_dir, filename=sanitized_title)
    print(f"{video.title} downloaded successfully!")

for mp4_file in os.listdir(output_dir):
    if mp4_file.endswith('.mp4'):
        mp4_path = os.path.join(output_dir, mp4_file)
        mp3_file = mp4_file.replace('.mp4', '.mp3')
        mp3_path = os.path.join(output_dir, mp3_file)

        input_file = ffmpeg.input(mp4_path)
        output_file = ffmpeg.output(input_file, mp3_path)
        ffmpeg.run(output_file)

        os.remove(mp4_path)
        print(f"Converted {mp4_file} to {mp3_file}")

print("Playlist downloaded and converted to MP3 successfully!")