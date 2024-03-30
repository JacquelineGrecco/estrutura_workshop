from app.pipeline.transform import transform_dataframe

import pandas as pd 

from typing import List


df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})


def test_transformation():
    """
        Function to test the concatenetaton of dataframes.
    """
    
    arrange = [df, df2]
    arrange_concat = pd.concat([df, df2], ignore_index=True)
    
    act = transform_dataframe(arrange)
    
    assert act.shape == (4, 2)
    assert arrange_concat.equals(act)