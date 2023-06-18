# importing the module
from pytube import YouTube
from moviepy.editor import *
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

    # cmd = f'python3 -m spleeter separate -p spleeter:2stems -o splitted/{musicName} -f "{musicName}_{{instrument}}.mp3" {filename}'
    # cmd = f'python3 -m spleeter separate -p spleeter:2stems -o uploads/{musicName} -f "{musicName}_{{instrument}}.mp3" {filename}'
    cmd = f'python3 -m spleeter separate -p spleeter:2stems -o splitted/{musicName} -f "{musicName}_{{instrument}}.mp3" uploads/{musicName}.mp3 '
    # Run the command
    result = subprocess.run(cmd, shell=True)

    # Check the return code to see if the command succeeded
    if result.returncode != 0:
        print(result)
    # If command executed succesfully
    else:
        returnFiles = []
        returnFiles.append(f"uploads/{fileName}.mp4")
        returnFiles.append(f"splitted/{fileName}/{musicName}_accompaniment.mp3")
        returnFiles.append(f"splitted/{fileName}/{musicName}_vocals.mp3")
        return returnFiles


def download_video(link):
    # where to save
    SAVE_PATH = "uploads"

    yt = YouTube(link)
    # creating a list for the characters to be replaced
    unwantedCharacters = ["\"", "(", ")", "|"]    

    name = yt.title
    name = name.replace(" ", "_")
    for char in unwantedCharacters:
    # replace() "returns" an altered string
        name = name.replace(char, "")
    filename = f"{name}.mp4"


    if (not(os.path.exists(f"{SAVE_PATH}/filename"))):
        stream = yt.streams.get_by_itag(22)
        stream.download(SAVE_PATH, filename)
        #print(f"\n{SAVE_PATH}/{filename}")

    return SAVE_PATH, name
    

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
    main("https://www.youtube.com/watch?v=tEboiVqOWJw&list=RDtEboiVqOWJw")
