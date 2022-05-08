import os
from time import sleep
from flask import send_file
from werkzeug.utils import secure_filename

from applications.analyze import analyze_txt

UPLOAD_PATH = './uploads/'
timeout = 60

## 파일 업로드 과정

# 텍스트 파일 체크
ALLOWED_FILE_TYPE_MAPPING = {
    'txt': 'text/plain'
}

ALLOWED_EXTENSIONS = set(ALLOWED_FILE_TYPE_MAPPING.keys())
ALLOWED_MIME_TYPES = set(ALLOWED_FILE_TYPE_MAPPING.values())

# 파일 마임 체크
def allowed_mime(mime_type):
    return mime_type in ALLOWED_MIME_TYPES

# 파일 확장자 체크
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 파일 업로드
def upload_file(file, filename):

    if not file or not filename:
        return "NOT EXIST FILE"
    
    if upload_file and allowed_file(filename):
        os.makedirs(UPLOAD_PATH, exist_ok=True)
        file_save_path = os.path.join(UPLOAD_PATH, filename)
        print('file_save_path : {}'.format(file_save_path))
        file.save(file_save_path)

        mime_type = file.mimetype
        content_type = file.content_type
        
        if mime_type and allowed_mime(mime_type) and allowed_mime(content_type) :
            return "Saved : {}".format(filename)
        else:
            os.remove(file_save_path)
            return "INVALID MIMETYPE : {}".format(mime_type)

    else:
        return 'INVALID FILE'


# 파일 업로드 자체 체크 필수
# https://ash84.io/2018/09/10/flask-upload-limit/

# 전체 프로세스 진행
def process(file):
    filename = secure_filename(file.filename)
    result = upload_file(file, filename)

    if 'INVALID' in result or 'NOT EXIST FILE' in result:
        return result
    else:
        analyze_txt(filename, UPLOAD_PATH)
        return result

# 파일 다운로드 (import 전용)
def download_file(file):
    print('download Test!!')
    filename = secure_filename(file.filename) + '.xlsx'
    return send_file(path_or_file = f'{UPLOAD_PATH}{filename}', 
                                    attachment_filename = f'{filename}', 
                                    as_attachment = True)




