from email import header
import os
from time import sleep
from numpy import source
from werkzeug.utils import secure_filename
import pandas as pd

# https://rfriend.tistory.com/250
# txt 분석
def analyze_txt(filename, upload_path):
    
    print('analyze Test!!')
    # test
    df = pd.read_csv(f'{upload_path}{filename}', 
                    sep='------------------------------------------------------------', 
                    encoding='utf-8',
                    header=None, names=['a','b', 'c', 'd'])
    
    print('Before Changing!')
    print(df)

    print(type(len(df.index))) # 마지막 인덱스 + 1

    df2 = pd.DataFrame(header=None, names=[])

    try:
        for i in range(0, len(df.index) - 1) :
            source_of_index = str(df.iloc[i, 0])
            print('source is {}'.format(source_of_index))
            divided_of_source = source_of_index.split(":")
            
            print(divided_of_source[1])
    except:
        print('Error Occur!!')
    
    print('Changing 1')
    print(df)

    # 분리 후 데이터를 다시 원하는 곳에 정렬하기 (DataFrame 다시 만들까? 아니면 있는걸 재정렬?)
    
    # 데이터 필요한 것 다듬기(데이터를 다시 계산해서 보이게 하기)

    # 분리는 좀 있다가.
    df.to_excel(f'{upload_path}{filename}.xlsx', index=True) # 마지막에 index=False로

# 다른 데이터 프레임을 만들고 거기에 넣는 방식으로 바꿔야 할 듯 하다.


file = open('c:/git/PolicyOrganizer/testArea/sogang5250_bppllist.txt')
analyze_txt(file.name, '')