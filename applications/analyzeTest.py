import os
from time import sleep
from werkzeug.utils import secure_filename
import pandas as pd

# https://rfriend.tistory.com/250
# txt 분석
async def analyze_txt(filename, upload_path):
    
    print('analyze Test!!')
    # test
    df = pd.read_csv(f'{upload_path}{filename}', 
                    sep='------------------------------------------------------------', 
                    encoding='utf-8',
                    header=None, names=['a','b','c','d','f','g','h','i'])
    
    print('Before Changing!')
    print(df)

    # a , b 데이터 나눠 보기
    # print('읽기')
    # test = str(df.iloc[1, 0])
    # print(type(test))
    # print(test)

    print(type(len(df.index))) # 마지막 인덱스 + 1
    try:
        for i in range(0, len(df.index) - 1) :
            source_of_index = str(df.iloc[i, 0])
            divided_of_source = source_of_index.split(":")
            if len(divided_of_source) == 2 :
                df.iloc[i, 0] = divided_of_source[0]
                df.iloc[i, 1] = divided_of_source[1]
        
        sleep(3)
    except:
        print('Error Occur!! ')
    
    print('Changing 1')
    print(df)

    # 분리 후 데이터를 다시 원하는 곳에 정렬하기 (DataFrame 다시 만들까? 아니면 있는걸 재정렬?)
    
    # 데이터 필요한 것 다듬기(데이터를 다시 계산해서 보이게 하기)

    # 분리는 좀 있다가.
    df.to_excel(f'{upload_path}{filename}.xlsx', index=True) # 마지막에 index=False로