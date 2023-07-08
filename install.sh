sudo apt install ffmpeg
python3 -m venv venv
source venv/bin/activate
pip install -r requirments.txt
pip install git+https://github.com/ytdl-org/youtube-dl
# Please change this your python version virtual environment
cp cipher.py venv/lib/python3.8/site-packages/pytube