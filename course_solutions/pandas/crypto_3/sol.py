import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def filtering(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    
    # Calculate statistical summary of the High column
    mean_high = df["High"].mean()
    median_high = df["High"].median()
    min_high = df["High"].min()
    max_high = df["High"].max()
    
    # Return all results as a dictionary
    return  mean_high, median_high, min_high, max_high


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = "crypto.csv"
    mean, median, mi, ma = filtering(inp)
    print(mean, median, mi, ma)
############## DO NOT TOUCH AREA: END ###################
