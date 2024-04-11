import os

import pandas as pd


def load_dataframe(
    dataframe: pd.DataFrame, output_path: str, file_name_output: str
) -> None:
    """
    Receber um dataframe e salvar em uma pasta data/output como excel

    Args:
        dataframe {pd.DataFrame} : dataframe com os dados a serem salvos
        output_path {str} : caminho da pasta de saida

    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    dataframe.to_excel(os.path.join(output_path, file_name_output), index=False)
    print(f"Dataframe salvo com sucesso em {output_path}/{file_name_output}")
