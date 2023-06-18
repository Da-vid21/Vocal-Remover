from flask import Flask, request, jsonify, render_template, send_file, make_response
import os
from src import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# This one is to process manual mp3 uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    print("Uploading")
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
        
    file = request.files['file']
    filename = file.filename
    file_ext = os.path.splitext(filename)[1]
    
    if file_ext not in ['.mp3', '.wav']:
        return jsonify({'error': 'Invalid file type, only MP3 and WAV are allowed'}), 400
    
    save_dir = os.path.join(app.root_path, 'uploads')
    
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    save_path = os.path.join(save_dir, filename)
    file.save(save_path)
    links = removeVocals.testConversion(save_path)
    print(links)
    instrumental_path = links[0]
    vocal_path = links[1]
    
    return render_template("preview.html", instrumental_path=instrumental_path, vocals_path=vocal_path)

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

@app.route('/splitted/<path:filename>')
def download_file(filename):
    file_path = os.path.join('splitted', filename)
    return send_file(file_path, as_attachment=False)

@app.route('/uploads/<path:filename>')
def download_video(filename):
    file_path = os.path.join('uploads', filename)
    return send_file(file_path, as_attachment=False)
if __name__ == '__main__':
    app.run(debug=False)
