import os
import pandas as pd

def main(excel):
    brand = excel.split('_')[0]
    cat = excel.split('_')[1]
    output_folder = f'./brand_excel/final/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df = pd.read_excel(f"./brand_excel/{excel}.xlsx")

    chunk_size = 100
    total_rows = df.shape[0]
    num_chunks = (total_rows + chunk_size - 1) // chunk_size

    columns = ['brd_cd', 'cat', 'sesn', 'part_cd', 'color_cd', 'url', 'seq']
    
    for chunk_idx in range(num_chunks):
        start_row = chunk_idx * chunk_size
        end_row = min((chunk_idx + 1) * chunk_size, total_rows)
        chunk_lines = []

        for i in range(start_row, end_row):
            row = df.iloc[i]
            line = [brand, cat, row['sesn'], row['part_cd'], row['color_cd'], row['url'], row['seq']]
            chunk_lines.append(line)

        chunk_df = pd.DataFrame(chunk_lines, columns=columns)
        output_path = os.path.join(output_folder, f"{excel}_final_chunk{chunk_idx + 1}.xlsx")
        chunk_df.to_excel(output_path, index=False)

if __name__ == "__main__":
    excel = "I_acc"
    main(excel)

