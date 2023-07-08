# importing the module
import youtube_dl
from pytube import YouTube
from moviepy.editor import *
from spleeter.separator import Separator
import os
import subprocess

def splitMusic(filename):
    filePath = filename.split("/")
    filePath = filePath[len(filePath)-1]
    # Replacing spaces with dashes for less web browsing
    filePath = filePath.replace(" ", "_")
    # Only get the filename from the absolute directory
    filePathArray = filePath.rsplit("/")
    fileName = filePathArray[len(filePathArray) - 1]
    musicName = fileName.replace(".mp3", "")
    
    # Create folder if not found
    try:
        os.mkdir(f"../splitted/{musicName}")
    except:
        pass

    #cmd = f'python3 -m spleeter separate -p spleeter:2stems -o splitted/{musicName} -f "{musicName}_{{instrument}}.mp3" uploads/{musicName}.mp3 '
    # Run the command
    #result = subprocess.run(cmd, shell=True)
    # Check the return code to see if the command succeeded
    # if result.returncode != 0:
    #     print(result)

    separator = Separator('spleeter:2stems')
    separator.separate_to_file(f'uploads/{musicName}.mp3', f"splitted/{fileName}", filename_format=f'{musicName}_{{instrument}}.mp3', synchronous=True)

    returnFiles = []
    returnFiles.append(f"uploads/{fileName}.mp4")
    returnFiles.append(f"splitted/{fileName}/{musicName}_accompaniment.mp3")
    returnFiles.append(f"splitted/{fileName}/{musicName}_vocals.mp3")
    return returnFiles


def download_video(video_url):
    
    # where to save
    SAVE_PATH = "uploads"
    yt = YouTube(video_url)
    name = yt.title

    # creating a list for the characters to be replaced
    unwantedCharacters = ["\"", "(", ")", "|"]    
    name = name.replace(" ", "_")
    for char in unwantedCharacters:
    # replace() "returns" an altered string
        name = name.replace(char, "")
    filename = f'{name}.mp4'

    stream = yt.streams.get_highest_resolution()
    try:
        stream.download(SAVE_PATH, filename)
    except:
        return ""

    return SAVE_PATH, name
    
#vid_name doesn't expect file extensions like vid_name.mp4 only pass in vid_name
def extractAudio(vid_path, vid_name):
    returnFiles = []

    videoName = f"{vid_path}/{vid_name}.mp4"
    # Specify the output file name
    audioName = f"{vid_path}/{vid_name}.mp3"

    # Load the video file
    video = VideoFileClip(videoName)

    if(not(os.path.exists(f"{vid_path}/{vid_name}.mp3"))):
        # Extract the audio
        audio = video.audio
        # Write the audio to the output file
        audio.write_audiofile(audioName)
    
    returnFiles = splitMusic(vid_name)
    print(returnFiles)
    return returnFiles


def main(link):

    SAVE_PATH, name = download_video(link)
    returnFiles = extractAudio(SAVE_PATH, name)
    return returnFiles

if __name__ == "__main__":
    main("https://www.youtube.com/watch?v=tEboiVqOWJw")
