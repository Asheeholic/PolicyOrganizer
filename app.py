import os
from flask import Flask, escape, redirect, request, render_template, url_for
from werkzeug.utils import secure_filename

# 가지고 있는 파일
import applications.loadTest as loadTest

app = Flask(__name__)

#d ctrl + f5 시작

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/fileupload', methods=['GET', 'POST'])
def file_upload():
    file = request.files['file']
    loadTest.test(file)
    return loadTest.download_test(file) # 리턴해야 파일을 줌..
    #return render_template('index.html')

if __name__=="__main__":
    app.run()

