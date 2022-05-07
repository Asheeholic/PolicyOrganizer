import os
from time import sleep
from flask import send_file
from werkzeug.utils import secure_filename

from applications.analyze import analyze_txt

upload_path = './uploads/'
timeout = 60

# 전체 프로세스 진행
def process(file):
    filename = secure_filename(file.filename)
    upload_file(file, filename)
    analyze_txt(filename, upload_path)

# 파일 업로드
def upload_file(file, filename):
    print('test upload!!')
    os.makedirs(upload_path, exist_ok=True)
    file.save(os.path.join(upload_path, filename))

# 파일 업로드 자체 체크 필수
# https://ash84.io/2018/09/10/flask-upload-limit/

#파일 다운로드
def download_file(file):
    print('download Test!!')
    filename = secure_filename(file.filename) + '.xlsx'
    return send_file(path_or_file = f'{upload_path}{filename}', 
                                    attachment_filename = f'{filename}', 
                                    as_attachment = True)




