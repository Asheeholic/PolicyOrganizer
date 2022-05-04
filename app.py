import os
from flask import *
from werkzeug.utils import secure_filename

# 가지고 있는 파일
import applications.loadFile as loadFile
import applications.fileCheck as fileCheck

# app 구성
app = Flask(__name__)

#d ctrl + f5 시작

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/fileupload', methods=['GET', 'POST'])
def file_upload():
    file = request.files['file']
    loadFile.process(file)
    # return render_template('index.html')

@app.route('/filecheck/<filename>', methods=['GET'])
def file_check(filename):
    result = {'result' : fileCheck.check_file(filename)}
    return jsonify(result)

@app.route('/filedownload', methods=['GET', 'POST'])
def file_download():
    file = request.files['file']
    return loadFile.download_file(file) # 리턴해야 파일을 줌..

if __name__=="__main__":
    app.run()

## 파일 크기가 크면 다운 실패함
