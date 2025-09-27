import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(sizes):
    # TODO this is what you need to complete
    plt.pie(sizes, labels=["Bitcoin", "Ethereum"])
    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'matplotlib_crypto_3.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return file_path

if __name__ == '__main__':
    inp = "crypto.csv"
    df = pd.read_csv(inp)
    volume_share = df.groupby('Name')['Volume'].sum()
    sizes = [volume_share['Bitcoin'], volume_share['Ethereum']]
    build_plot(sizes)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
