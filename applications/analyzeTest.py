import os
from time import sleep
from werkzeug.utils import secure_filename
import pandas as pd

# https://rfriend.tistory.com/250
# txt 분석
def analyze_txt(filename, upload_path):
    
    print('analyze Test!!')
    # test
    df = pd.read_csv(f'{upload_path}{filename}', 
                    sep='------------------------------------------------------------', 
                    encoding='utf-8')
    
    print('Before Changing!')
    print(df)

    # Unnamed: 1 제거
    df.drop(['Unnamed: 1'], axis = 1, inplace = True)
    print('Changing 1')
    print(df)

    # Unnamed: 0 에서 처음부터 끝까지 분리 (for 또는 while)

    # 분리 후 데이터를 다시 원하는 곳에 정렬하기 (DataFrame 다시 만들까? 아니면 있는걸 재정렬?)
    
    # 데이터 필요한 것 다듬기(데이터를 다시 계산해서 보이게 하기)

    # 분리는 좀 있다가.
    print('읽어보자')
    df.to_excel(f'{upload_path}{filename}.xlsx',index=True)