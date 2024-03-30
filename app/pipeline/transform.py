import pandas as pd 

from typing import List 


"""
    Função para transformar uma lista de dataframes em um ùnico dataframe.

    Args:
        dataframe_list {list} : lista de dataframes

    Returns:
        pd.DataFrame: dataframe com os dados concatenados

"""


def transform_dataframe(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dataframe_list, ignore_index=True)
