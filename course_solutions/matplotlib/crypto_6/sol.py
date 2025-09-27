import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(bitcoin_data, ethereum_data):
    # TODO this is what you need to complete
    plt.boxplot([bitcoin_data['High'], ethereum_data['High']], labels=['Bitcoin', 'Ethereum'])


    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'matplotlib_crypto_6.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return file_path

if __name__ == '__main__':
    inp = "crypto.csv"
    df = pd.read_csv(inp)
    ethereum_data = df[df["Name"] == "Ethereum"]
    bitcoin_data = df[df["Name"] == "Bitcoin"]
    build_plot(bitcoin_data, ethereum_data)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
