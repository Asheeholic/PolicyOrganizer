import os
import pandas as pd

# https://rfriend.tistory.com/250
# txt 분석

def analyze_txt(filename, upload_path):
    
    print('analyze Test!!')
    # test
    df = pd.read_csv(f'{upload_path}{filename}', 
                    sep='------------------------------------------------------------',
                    encoding='utf-8', 
                    engine='python')
    
    print("테스트 시작")
    print(df)
    print('------')
    print(df.info)
    print('------')

    # unnamed 0을 살리고 1은 없앤다
    # 그 뒤 unnamed 0 에서의 NaN을 기준으로 정책을 나누게 한다.
    print('------')

    print(df.head(10))
    print("테스트 끝")
    
    df.to_excel(f'{upload_path}{filename}.xlsx',index=False, engine='openpyxl')

analyze_txt('c:/dev/PolicyOrganizer/testArea/policies.txt', '')