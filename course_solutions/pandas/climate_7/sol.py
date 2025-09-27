import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def sort(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    mean_2040 = df["2040"].mean()
    df["2040_flag"] = df["2040"].apply(lambda x: "High" if x > mean_2040 else "Low")
    return df


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    file_path = 'pandas_climate_7.csv'
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == '__main__':
    inp = "emissions.csv"
    df = sort(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
