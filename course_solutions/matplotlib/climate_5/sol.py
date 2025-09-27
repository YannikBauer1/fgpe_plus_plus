import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(df):
    # TODO this is what you need to complete
    plt.hist(df['2044'], bins=20)
    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'matplotlib_climate_5.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return file_path

if __name__ == '__main__':
    inp = "emissions.csv"
    df = pd.read_csv(inp)
    build_plot(df)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
