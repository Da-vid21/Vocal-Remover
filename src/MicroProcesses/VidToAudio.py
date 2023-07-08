from moviepy.editor import *
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
if __name__ == "__main__":
    extractAudio("uploads", "teddy")