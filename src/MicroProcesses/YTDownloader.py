from pytube import YouTube

def download_video(video_url):
    if("&list" in video_url):
        return ""
    
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
        print("An error has occurred")
    print("Download is completed successfully")

    return SAVE_PATH, filename

if __name__ == "__main__":
    save_path, title = download_video("https://www.youtube.com/watch?v=tEboiVqOWJw")
    print(title)