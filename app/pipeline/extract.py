import os 
import glob

import pandas as pd

from typing import List


""""
Função para ler arquivos de uma pasta data/input e retornar uma lista de dataframe

Args:
    input_path {str} : caminho da pasta com os arquivos

Returns:
    list: lista de dataframe com os dados do arquivo

"""

def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    
    all_files = glob.glob(os.path.join(input_path, "*.xlsx"))
    
    dataframe_list = []
    
    for filename in all_files:
        dataframe_list.append(pd.read_excel(filename))
        
    return dataframe_list



if __name__ == "__main__":
    input_path = './data/input'
    print(extract_from_excel(input_path))