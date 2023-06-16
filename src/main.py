# importing the module
from pytube import YouTube
from moviepy.editor import *
from src import removeVocals

def download_video(link):
    # where to save
    SAVE_PATH = "uploads"

    yt = YouTube(link)

    name = yt.title
    name = name.replace("\"", "")
    filename = f"{name}.mp4"


    if (not(os.path.exists(f"{SAVE_PATH}/filename"))):
        stream = yt.streams.get_by_itag(22)

        stream.download(SAVE_PATH, filename)
        print(f"\n{SAVE_PATH}/{filename}")

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


    returnFiles.append(videoName)
    returnFiles += removeVocals.testConversion(vid_name)
    print(returnFiles)
    return returnFiles
def main(link):

    SAVE_PATH, name = download_video(link)
    returnFiles = extractAudio(SAVE_PATH, name)
    return returnFiles
if __name__ == "__main__":
    main("https://www.youtube.com/watch?v=7Dhg44Wtidw")
