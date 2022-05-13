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

    # a , b 데이터 나눠 보기
    # print('읽기')
    # test = str(df.iloc[1, 0])
    # print(type(test))
    # print(test)

    print(type(len(df.index))) # 마지막 인덱스 + 1
    try:
        for i in range(0, len(df.index) - 1) :
            source_of_index = str(df.iloc[i, 0])
            print('source is {}'.format(source_of_index))

            # Exclude Dates 바꿔야함
            if 'Excluded Dates' in source_of_index:
                print()

            # Backup Selection
            if 'Include' in source_of_index :
                
                j = i + 1
                while(True):
                    
                    print(str(df.iloc[j, 0]))
                    if 'Schedule:' in str(df.iloc[j, 0]):
                        break
                    
                    source_of_index += '\n' + str(df.iloc[j, 0])

                    j = j + 1
                
                print(source_of_index)

            # HW/OS/Client
            if 'HW/OS/Client' in source_of_index :
                divided_of_source = source_of_index.split(":")
                if len(divided_of_source) == 2 :
                    # print('if Test!')
                    df.iloc[i, 0] = divided_of_source[0]
                    # print(divided_of_source[1])
                    space_divied_of_div = divided_of_source[1].split()                    
                    # print(space_divied_of_div)
                    # print('error test')
                    df.iloc[i, 1] = space_divied_of_div[0] # HW
                    df.iloc[i, 2] = space_divied_of_div[1] # OS
                    df.iloc[i, 3] = space_divied_of_div[2] # Client
                    continue

            # Daily Windows 바꿔야함
            if 'Daily Windows' in source_of_index :
                print("daily test")

            
            # 빈공간
            # if source_of_index in 'nan' :
            #     source_of_index = '--'

            divided_of_source = source_of_index.split(":")
            if len(divided_of_source) == 2 :
                df.iloc[i, 0] = divided_of_source[0]
                df.iloc[i, 1] = divided_of_source[1]
                
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