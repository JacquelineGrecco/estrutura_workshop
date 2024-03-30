import glob
import os
from typing import List

import pandas as pd


def extract_from_excel(input_path: str) -> List[pd.DataFrame]:

    """
    Ler arquivos de uma pasta data e retornar uma lista de dataframe
    Args:
        input_path:caminho da pasta com os arquivos
    Returns:
        list:lista de dataframe com os dados
    """

    all_files = glob.glob(os.path.join(input_path, '*.xlsx'))

    dataframe_list = []

    for filename in all_files:
        dataframe_list.append(pd.read_excel(filename))

    return dataframe_list


if __name__ == '__main__':
    input_path = './data/input'
    print(extract_from_excel(input_path))
