from flask import Flask, request, jsonify, render_template, send_file, make_response
import os
from src import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# This one is to process youtube Links
@app.route('/YTLink', methods=['POST'])
def processYT():
    # print(request.form.get('youtube-link'))
    link = request.form.get('youtube-link')
    
    links = main.main(link)
    video_link = links[0]
    instrumental_path = links[1]
    vocal_path = links[2]
    
    # Render the template
    return render_template("karaoke.html", video_path=video_link, instrumental_path=instrumental_path, vocals_path=vocal_path)

@app.route('/splitted/<path:filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join('splitted', filename)
    return send_file(file_path, as_attachment=False)

@app.route('/uploads/<path:filename>', methods=['GET'])
def download_video(filename):
    file_path = os.path.join('uploads', filename)
    return send_file(file_path, as_attachment=False)
if __name__ == '__main__':
    app.run(debug=False)
