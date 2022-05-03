import os
from flask import send_file
from werkzeug.utils import secure_filename

from applications.analyzeTest import analyze_txt

upload_path = './uploads/'

def test(file):
    filename = secure_filename(file.filename)
    upload_test(file, filename)
    analyze_txt(filename, upload_path)

# 파일 업로드
def upload_test(file, filename):
    print('test upload!!')
    os.makedirs(upload_path, exist_ok=True)
    file.save(os.path.join(upload_path, filename))

#파일 다운로드
def download_test(file):
    print('download Test!!')
    filename = secure_filename(file.filename) + '.xlsx'
    return send_file(path_or_file = f'{upload_path}{filename}', 
                                    attachment_filename = f'{filename}', 
                                    as_attachment = True)




