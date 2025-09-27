import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def filtering(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    sorted_df = df.sort_values(by="High", ascending=False)
    return sorted_df


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    file_path = 'pandas_crypto_4.csv'
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == '__main__':
    inp = "crypto.csv"
    df = filtering(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
