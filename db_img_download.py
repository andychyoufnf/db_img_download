import concurrent.futures
import requests
import csv
import os
import re
import pandas as pd
import time


pattern = re.compile(r"""['"#%&{}\\/]""")
error_cnt = 0
global_cnt = 0

def download_image(brand, cat, line, output_folder):
    global error_cnt
    url = line[6]
    if line[4]  in ['SET', '?']:
        return
    try:
        response = requests.get(url)
        response.raise_for_status()  
        if response.status_code == 200:
            output_folder += "{}/{}/{}/{}/{}/".format(brand, cat, line[2],line[3],line[4])
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            filename = "{}_{}_{}_{}_{}_{}.jpg".format(brand, cat, line[2],line[3],line[4],line[5])
            filename = os.path.join(output_folder, filename)
            if not os.path.exists(filename):
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"{output_folder} url : {url} Downloaded ")

 
    except requests.exceptions.RequestException as e:
        print(f"{output_folder}  url : {url} Failed to download {url}. Error: {e} ")
        error_cnt += 1
        # time.sleep(5)
    except Exception as e:
        print(f"{output_folder}  url : {url} Failed to download {url}. Error: {e} ")
        error_cnt += 1
        # time.sleep(5)
    global_cnt += 1
    


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
        if not os.path.exists(new_folder):
                os.makedirs(new_folder)
        line = [brand, cat, row['sesn'],row['part_cd'],row['color_cd'],row['seq'], row['url']]
        lines.append(line)

        

    
    

    

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for line in lines:
            futures.append(executor.submit(download_image, brand, cat, line, output_folder))
            global_cnt += 1
        concurrent.futures.wait(futures)
    


    

if __name__ == "__main__":
    
    excel = "X-kids_shoes"
    main(excel)
    print('ran', excel, 'total error: ', error_cnt)
    