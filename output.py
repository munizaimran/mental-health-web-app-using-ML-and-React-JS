from flask import Flask, render_template, Response


app = Flask(__name__)
@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')

import real_time_video
#os.system('python real_time_video.py')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/your_face')
def your_face():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)
