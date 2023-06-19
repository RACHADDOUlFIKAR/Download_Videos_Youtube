from pytube import YouTube
from flask import Flask ,render_template,request
import os
app= Flask(__name__)
@app.route('/',methods=['GET'])
def hellow():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    value = request.form.get('select')
    DOWNLOAD_PATH = "c:/Users/LENOVO/Desktop/rachadm/videos"
    video_link=[request.form['text']]
    if value=="MP4":
        for i in video_link:
            try:
                yt = YouTube(i)
            except:
                print("Connection Error")
            stream = yt.streams.get_highest_resolution()
            try:
                stream.download(DOWNLOAD_PATH)
            except:
                print("There is some Error!")
        print('Videos Download Successfully!')
    else:
        for i in video_link:
            try:
                yt = YouTube(i)
            except:
                print("Connection Error")
            stream =  yt.streams.filter(only_audio=True).first()
            try:
                out_file=stream.download(DOWNLOAD_PATH)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
            except:
                print("There is some Error!")
        print('Audio Download Successfully!')

    return render_template('index.html',stream=stream)

if __name__ == '__main__':
    app.run(port=2000,debug=True)