import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def group(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    
    # Create SpreadPct column using .apply() to measure intraday volatility as percentage of open price
    df["SpreadPct"] = df.apply(lambda row: ((row["High"] - row["Low"]) / row["Open"]) * 100, axis=1)
    
    return df


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    file_path = 'pandas_crypto_7.csv'
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == '__main__':
    inp = "crypto.csv"
    df = group(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
