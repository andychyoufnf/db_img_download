import concurrent.futures
import requests
import csv
import os
import re
import pandas as pd
import time



def main(excel):
    global global_cnt
    brand = excel.split('_')[0]
    cat = excel.split('_')[1]
    output_folder = f'./img/'

    

    
    df = pd.read_excel(f"./brand_excel/{excel}.xlsx")
    lines = []
    for i, row in df.iterrows():
        if row['color_cd'] in  ['SET', '?']:
            continue
        new_folder = os.path.join(output_folder, "{}/{}/{}/{}/{}/".format(brand, cat, row['sesn'],row['part_cd'],row['color_cd']))
        new_folder = os.path.join(new_folder, "{}_{}_{}_{}_{}_{}.jpg".format(brand, cat, row['sesn'],row['part_cd'],row['color_cd'],row['seq']))
        if not os.path.exists(new_folder):
                print("no : ", new_folder)
        line = [brand, cat, row['sesn'],row['part_cd'],row['color_cd'],row['seq'], row['url']]
        lines.append(line)

        

    
    

    

   
    

if __name__ == "__main__":
    
    excel = "X-adult_clothes_9"
    main(excel)
