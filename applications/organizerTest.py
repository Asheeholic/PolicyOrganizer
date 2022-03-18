import os
from time import sleep
from flask import Flask, escape, request, render_template, send_file
from werkzeug.utils import secure_filename
import pandas as pd


upload_path = './uploads/'

def test(file):
    filename = secure_filename(file.filename)
    upload_test(file, filename)
    analyze_txt(filename)


# 파일 업로드
def upload_test(file, filename):
    print('test upload!!')
    os.makedirs(upload_path, exist_ok=True)
    file.save(os.path.join(upload_path, filename))

# https://rfriend.tistory.com/250
# txt 분석
def analyze_txt(filename):
    
    print('analyze Test!!')
    # test
    df = pd.read_csv(f'{upload_path}{filename}', encoding='utf-8')
    
    print(df)
    
    df.to_excel(f'{upload_path}{filename}.xlsx',index=True)

# 파일 다운로드
def download_test(file):
    print('download Test!!')
    filename = secure_filename(file.filename) + '.xlsx'
    return send_file(path_or_file = f'{upload_path}{filename}', 
                                    attachment_filename = f'{filename}', 
                                    as_attachment = True)




