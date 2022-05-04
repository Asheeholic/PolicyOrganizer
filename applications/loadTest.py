import os
from time import sleep
from flask import send_file
from werkzeug.utils import secure_filename

from applications.analyzeTest import analyze_txt

upload_path = './uploads/'
timeout = 60

def test(file):
    filename = secure_filename(file.filename)
    upload_test(file, filename)
    analyze_txt(filename, upload_path)
    check_file(file)

# 파일 업로드
def upload_test(file, filename):
    print('test upload!!')
    os.makedirs(upload_path, exist_ok=True)
    file.save(os.path.join(upload_path, filename))

# 엑셀 파일이 있는지 체크
# Timeout 동안 파일이 있으면 [엑셀 파일 이름] 전달, 시간 제한 끝나면 False
def check_file(file):
    print('File checking test!')
    
    # 파일 이름
    filename_xlsx = secure_filename(file.filename) + '.xlsx'
    
    # 시간동안 파일 체크
    for i in range(1, timeout) :
        file_list = os.listdir(upload_path)
        if filename_xlsx in str(file_list) :
            return filename_xlsx

        sleep(1)
    
    return False


#파일 다운로드
def download_test(file):
    print('download Test!!')
    filename = secure_filename(file.filename) + '.xlsx'
    return send_file(path_or_file = f'{upload_path}{filename}', 
                                    attachment_filename = f'{filename}', 
                                    as_attachment = True)




