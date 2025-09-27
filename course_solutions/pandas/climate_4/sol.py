import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def sort(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    sorted_df = df.sort_values(by="2040", ascending=False)
    return sorted_df


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    df.to_csv("pandas_climate_4.csv", index=False)
    return "pandas_climate_4.csv"

if __name__ == '__main__':
    inp = "emissions.csv"
    df = sort(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
