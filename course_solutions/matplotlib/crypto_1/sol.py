import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(df):
    # TODO this is what you need to complete
    plt.plot(df["Date"], df["High"])
    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'matplotlib_crypto_1.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return file_path

if __name__ == '__main__':
    inp = "crypto.csv"
    df = pd.read_csv(inp)
    df = df[df["Name"] == "Bitcoin"]
    if not np.issubdtype(df["Date"].dtype, np.datetime64):
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    build_plot(df)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
