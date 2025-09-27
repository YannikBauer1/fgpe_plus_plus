import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def sort(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    grp = df.groupby("continent")[["2040", "2041", "2042", "2043", "2044"]].agg(["mean"])
    return grp


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    file_path = 'pandas_climate_6.csv'
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == '__main__':
    inp = "emissions.csv"
    df = sort(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
