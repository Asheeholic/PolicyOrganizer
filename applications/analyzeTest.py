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
    
    print(df)
    
    df.to_excel(f'{upload_path}{filename}.xlsx',index=True)