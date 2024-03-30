from typing import List

import pandas as pd


def transform_dataframe(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:

    """
    Função para transformar uma lista de dataframes em um ùnico dataframe.

    Args:
        dataframe_list {list} : lista de dataframes

    Returns:
        pd.DataFrame: dataframe com os dados concatenados

    """

    return pd.concat(dataframe_list, ignore_index=True)
