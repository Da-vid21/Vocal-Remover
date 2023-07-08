from spleeter.separator import Separator

def separate_audio(filepath):
    output_path = "splitted/"
    musicName = filepath.replace(".mp4", "")

    separator = Separator('spleeter:2stems')
    separator.separate_to_file(filepath, output_path, filename_format=f'{musicName}_{{instrument}}.mp3', synchronous=True)

if __name__ == '__main__':
    input_file = 'uploads/teddy.mp3'  # Replace with the path to your input audio file

    separate_audio(input_file)