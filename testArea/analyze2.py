import os
from time import sleep
from numpy import source
from werkzeug.utils import secure_filename
import pandas as pd
import enums

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

    subject = enums.SUBJECT
    print('subject Test')
    print(subject)
    df_result = pd.DataFrame(columns=subject)
    
    # try:
    whileTurn = True
    i = 0
    while whileTurn :
        # print('first while')
        
        source_of_index = str(df.iloc[i, 0])
        
        # Policy name check
        if 'Policy Name:' not in source_of_index :
            i += 1
            continue

        else :
            if 'Policy Name:' in source_of_index :
                divided_source = source_of_index.split(":")
                policy_name = divided_source[1]
                i += 1
                
                policy_type = ''
                residence = '' # storage unit
                volume_pool = ''
                use_accelerator = ''
                HW_OS_Client = ''
                
                while i < len(df.index):
                    # print('second while')
                    source_of_index = str(df.iloc[i, 0])
                    divided_source = source_of_index.split(":")

                    # print(i)
                    # print(len(df.index))
                    if divided_source[0] in subject :
                        if 'Policy Type' in divided_source[0] :
                            policy_type = divided_source[1]
                        elif 'Residence' in divided_source[0] :
                            residence = divided_source[1]
                        elif 'Volume Pool' in divided_source[0] :
                            volume_pool = divided_source[1]
                        elif 'Use Accelerator' in divided_source[0] :
                            use_accelerator = divided_source[1]
                        # 수정
                        elif 'HW/OS/Client' in divided_source[0] :
                            HW_OS_Client = divided_source[1]
                    
                    if 'Policy Name' in str(df.iloc[i, 0]) :
                        i = i - 1
                        break
                    
                    i += 1
                         
                data = {
                    subject[0] : policy_name,
                    subject[1] : policy_type,
                    subject[2] : residence,
                    subject[3] : volume_pool,
                    subject[4] : use_accelerator,
                    subject[5] : HW_OS_Client,
                }
                # print(data)
                df_result = df_result.append(data, ignore_index=True)
                
        
        # 끝에 도달하거나 오류나면 끝내기
        if i == len(df.index) :
            break
        
        i += 1

    # except:
    #     print('Error Occur!!')

    print('result DataFrame')
    print(df_result)
    # 분리 후 데이터를 다시 원하는 곳에 정렬하기 (DataFrame 다시 만들까? 아니면 있는걸 재정렬?)
    
    # 데이터 필요한 것 다듬기(데이터를 다시 계산해서 보이게 하기)

    # 분리는 좀 있다가.
    df_result.to_excel(f'{upload_path}{filename}.xlsx', index=True) # 마지막에 index=False로

# 다른 데이터 프레임을 만들고 거기에 넣는 방식으로 바꿔야 할 듯 하다.


file = open('c:/git/PolicyOrganizer/testArea/sogang5250_bppllist.txt')
analyze_txt(file.name, '')