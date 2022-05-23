import os
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
    
    # print('Before Changing!')
    # print(df)

    # print(type(len(df.index))) # 마지막 인덱스 + 1
    
    df_result = ''
    # 걍 천천히 할까? 뭐 나오면 뭐 넣어주고 (필요한것만)

    subject = enums.SUBJECT
    # print('subject Test')
    # print(subject)
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
                policy_name = divided_source[1].strip()
                i += 1
                
                # Basic
                policy_type = ''
                residence = '' # storage unit
                volume_pool = ''
                use_accelerator = ''
                HW = ''
                OS = ''
                Client = ''
                Backup_Selection = ''
                

                # Add
                add_data_list = []

                while i < len(df.index):
                    # print('second while')
                    source_of_index = str(df.iloc[i, 0])
                    divided_source = source_of_index.split(":")

                    # print(i)
                    # print(len(df.index))
                    
                    if 'Policy Type' in divided_source[0] :
                        policy_type = divided_source[1].strip()
                    
                    # 중복
                    elif 'Residence' == divided_source[0] :
                        if residence == '' :
                            residence = divided_source[1].strip()
                    
                    # 중복
                    elif 'Volume Pool' in divided_source[0] :
                        if volume_pool == '' :
                            volume_pool = divided_source[1].strip()
                    
                    elif 'Use Accelerator' in divided_source[0] :
                        use_accelerator = divided_source[1].strip()
                    # 수정
                    
                    elif 'HW/OS/Client' in divided_source[0] :
                        HW_OS_Client_divided = divided_source[1].split()
                        HW = HW_OS_Client_divided[0]
                        OS = HW_OS_Client_divided[1]
                        Client = HW_OS_Client_divided[2]
                        # 만약 여러개라면 다음 행에 더 추가 시켜줘야 하지 않을까?
                        
                        if 'Include:' not in str(df.iloc[i+1, 0]):
                            j = 0
                            i += 1
                            while 'Include:' not in str(df.iloc[i, 0]):    
                                source_of_HW_OS_Client = str(df.iloc[i, 0])
                                divided_of_HW_OS_Client = source_of_HW_OS_Client.split()

                                # 기존에 있으면 데이터만 변경하여 추가하고
                                try:
                                    add_data_list[j]['HW'] = divided_of_HW_OS_Client[0]
                                    add_data_list[j]['OS'] = divided_of_HW_OS_Client[1]
                                    add_data_list[j]['Client'] = divided_of_HW_OS_Client[2]
                                
                                # 없으면 행을 더 추가하는 식으로 하기
                                except:
                                    add_data = {
                                        'HW' : divided_of_HW_OS_Client[0],
                                        'OS' : divided_of_HW_OS_Client[1],
                                        'Client' : divided_of_HW_OS_Client[2],
                                    }
                                    add_data_list.append(add_data)

                                j += 1
                                i += 1
                            i -= 1
                    
                    # Include.. (Backup Selection)
                    elif 'Include' == divided_source[0]:
                        # print(divided_source)
                        # print('Include if test')
                        
                        # '\' 넣어주기
                        if len(divided_source) > 2 :
                            if '\\' in divided_source[2] :
                                divided_source[1] += ':'
                                divided_source[1] += divided_source[2]

                        # print(divided_source)
                        # 첫 행
                        Backup_Selection = divided_source[1].strip()
                        
                    
                        # 다음 행들
                        # print(str(df.iloc[i + 1, 0]))
                        if 'Schedule:' not in str(df.iloc[i + 1, 0]):
                            # print('Include2 if test')

                            i += 1
                            j = 0
                            
                            while 'Schedule:' not in str(df.iloc[i, 0]):    
                                source_of_include = str(df.iloc[i, 0])
                                # print('while Test')
                                # print(j)
                                # print(source_of_include)

                                # 기존에 있으면 데이터만 변경하여 추가하고
                                try:
                                    add_data_list[j]['Backup_Selection'] = source_of_include
                                
                                # 없으면 행을 더 추가하는 식으로 하기
                                except:
                                    print(policy_name)
                                    print(source_of_include)
                                    add_data = { 'Backup_Selection' : source_of_include }
                                    add_data_list.append(add_data)

                                j += 1
                                i += 1

                            i -= 1

                    # Schedule...
                    # elif 'Schedule' in divided_source[0]:
                    #     print()

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
                    subject[5] : HW,
                    subject[6] : OS,
                    subject[7] : Client,
                    subject[8] : Backup_Selection,
                }
                # print(data)
                # print(df_result.index)
                df_result = df_result.append(data, ignore_index=True)
                
                # add rest of Policy details
                for k in range(0, len(add_data_list)) :
                    df_result = df_result.append(add_data_list[k], ignore_index=True)
                
        
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
    df_result.to_excel(f'{upload_path}{filename}.xlsx', index=False) # 마지막에 index=False로

# 다른 데이터 프레임을 만들고 거기에 넣는 방식으로 바꿔야 할 듯 하다.

# file = open('c:/git/PolicyOrganizer/testArea/policies.txt')
file = open('c:/git/PolicyOrganizer/testArea/sogang5250_bppllist.txt')
analyze_txt(file.name, '')