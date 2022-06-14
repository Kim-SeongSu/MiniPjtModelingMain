import pandas as pd

def load_dataset(csv_name):
   try:
     df = pd.read_csv(csv_name)
   except: 
     raise Exception("csv파일의 위치를 입력하세요!")
   return df
