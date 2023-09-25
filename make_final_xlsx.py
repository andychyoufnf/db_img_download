import concurrent.futures
import requests
import csv
import os
import re
import pandas as pd

cnt = 1
row_count = 0

pattern = re.compile(r"""['"#%&{}\\/]""")

def download_image(url, filename, output_dir, split_index):
    filename = pattern.sub("", filename)
    global cnt
    try:
        response = requests.get(url)
        response.raise_for_status()  
        if response.status_code == 200:
            filename = os.path.join(output_dir, filename)
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"index : {split_index} cnt {cnt}/{row_count} Downloaded {filename}")

    except requests.exceptions.RequestException as e:
        print(f"index : {split_index} cnt : {cnt}/{row_count} Failed to download {url}. Error: {e}")
    except Exception as e:
        print(f"index : {split_index} cnt : {cnt}/{row_count} An unexpected error occurred while downloading {url}. Error: {e}")

    
    cnt+=1



def main(excel):
    
    df = pd.read_excel(f"./brand_excel/{excel}.xlsx")
    
    sesn_dict = {'22S': 0, '22F': 0, '23S': 0}
    # sesn_dict = {'22N': 0, '23N': 0}
    final_list = []
    final_excel = f"{excel}_final.xlsx"
    for i, row in df.iterrows():
        
        if row['sesn'] == '22S' and sesn_dict['22S'] < (280)  :
            sesn_dict['22S'] += 1
            final_list.append("{}|{}|{}|{}".format(row['sesn'], row['prdt_cd'], row['seq'], row['url']))
        elif row['sesn'] == '22F' and sesn_dict['22F'] < (280)  :
            sesn_dict['22F'] += 1
            final_list.append("{}|{}|{}|{}".format(row['sesn'], row['prdt_cd'], row['seq'], row['url']))
        elif row['sesn'] == '23S' and sesn_dict['23S'] < 280 :
            sesn_dict['23S'] += 1
            final_list.append("{}|{}|{}|{}".format(row['sesn'], row['prdt_cd'], row['seq'], row['url']))

                
        # if row['sesn'] == '22N' and sesn_dict['22N'] < (420)  :
        #     sesn_dict['22N'] += 1
        #     final_list.append("{}|{}|{}|{}".format(row['sesn'], row['prdt_cd'], row['seq'], row['url']))
        # elif row['sesn'] == '23N' and sesn_dict['23N'] < (900)  :
        #     sesn_dict['23N'] += 1
        #     final_list.append("{}|{}|{}|{}".format(row['sesn'], row['prdt_cd'], row['seq'], row['url']))
        


    columns = ['sesn',	'prdt_cd',	'seq', 'url']

    data = [row.split('|') for row in final_list]
    dw = pd.DataFrame(data, columns=columns)
    dw.to_excel(f"./brand_excel/final/{excel}_final.xlsx", index=False)
    
    print("success : ", excel, sesn_dict)


if __name__ == "__main__":
    
    excel = "V_clothes"
    main(excel)
    