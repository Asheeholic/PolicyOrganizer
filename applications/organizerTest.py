from calendar import c
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
    df = pd.read_csv(f'{upload_path}{filename}', 
                    sep='------------------------------------------------------------', 
                    encoding='utf-8')
    print('Before Change')
    print(df)
    
    # Unnamed: 1 제거
    df.drop(['Unnamed: 1'], axis = 1, inplace = True)
    print('Changing 1')
    print(df)

    # Unnamed: 0 에서 처음부터 끝까지 분리 (for 또는 while)

    # 분리 후 데이터를 다시 원하는 곳에 정렬하기 (DataFrame 다시 만들까? 아니면 있는걸 재정렬?)
    
    # 데이터 필요한 것 다듬기(데이터를 다시 계산해서 보이게 하기)

    # 분리는 좀 있다가.

    df.to_excel(f'{upload_path}{filename}.xlsx',index=True)

# 파일 다운로드
def download_test(file):
    print('download Test!!')
    filename = secure_filename(file.filename) + '.xlsx'
    return send_file(path_or_file = f'{upload_path}{filename}', 
                                    attachment_filename = f'{filename}', 
                                    as_attachment = True)