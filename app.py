import os
from flask import *
from werkzeug.utils import secure_filename

# 가지고 있는 파일
import applications.loadFile as loadFile
import applications.fileCheck as fileCheck

# app 구성
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#d ctrl + f5 시작

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/fileupload', methods=['GET', 'POST'])
def file_upload():
    file = request.files['file']
    result = {'result' : loadFile.process(file)}
    return jsonify(result)

# get = request.args["number"] number = name
# post = request.form["file"] file = name
@app.route('/filecheck', methods=['POST'])
def file_check(): 
    filename = request.form["fileNameInput"]
    check_result = fileCheck.check_file(filename)
    result = {'result' : check_result}
    return jsonify(result)

@app.route('/filedownload', methods=['GET', 'POST'])
def file_download():
    file = request.files['file']
    return loadFile.download_file(file) # 리턴해야 파일을 줌..

if __name__=="__main__":
    app.run()
