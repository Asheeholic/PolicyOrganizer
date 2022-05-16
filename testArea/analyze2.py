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
    
    df_result = ''
    # 걍 천천히 할까? 뭐 나오면 뭐 넣어주고 (필요한것만)

    subject = []
    
    # 요일
    DAYS = ['Sunday', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday']

    try:
        for i in range(0, len(df.index) - 1) :
            print()
            # source_of_index = str(df.iloc[i, 0])
            # print('source is {}'.format(source_of_index))
            
            # # 일단 ':' 로 나누고
            # divided_of_source = source_of_index.split(":")

            # if (divided_of_source not in subject) \
            #     and (DAYS not in divided_of_source) :
            #     subject.append(divided_of_source[0])

            # if ':' in source_of_index :
            #     divided_of_source = source_of_index.split(":")
                
            #     print(divided_of_source[0])

            #     # 스케줄 또는 except 스케줄, include
            #     if len(divided_of_source) > 2 :
            #         print()        

            #     if len(divided_of_source) == 2 :
            #         df_result.iloc[i, 0] = divided_of_source[0]
            #         df_result.iloc[i, 1] = divided_of_source[1]
        

    except:
        print('Error Occur!!')
    
    print(subject)
    df_result = pd.DataFrame(columns=subject)
    
    print('Changing 1')
    print(df)

    print('result DataFrame')
    print(df_result)
    # 분리 후 데이터를 다시 원하는 곳에 정렬하기 (DataFrame 다시 만들까? 아니면 있는걸 재정렬?)
    
    # 데이터 필요한 것 다듬기(데이터를 다시 계산해서 보이게 하기)

    # 분리는 좀 있다가.
    df_result.to_excel(f'{upload_path}{filename}.xlsx', index=True) # 마지막에 index=False로

# 다른 데이터 프레임을 만들고 거기에 넣는 방식으로 바꿔야 할 듯 하다.


file = open('c:/git/PolicyOrganizer/testArea/policies.txt')
analyze_txt(file.name, '')