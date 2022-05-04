import os
from time import sleep

timeout = 60

# 엑셀 파일이 있는지 체크
# Timeout 동안 파일이 있으면 [엑셀 파일 이름] 전달, 시간 제한 끝나면 False
def check_file(filename, upload_path):
    print('File checking test!')
    
    # 시간동안 파일 체크
    for i in range(1, timeout) :
        file_list = os.listdir(upload_path)
        if filename in str(file_list) :
            return filename
        if i == (timeout - 5) :
            print('Warning! File Checking Error Comming!')
        sleep(1)
    
    return False