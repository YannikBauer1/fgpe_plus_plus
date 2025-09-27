import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(df):
    # TODO this is what you need to complete
    plt.pie(df['2040'], labels=df['country'])
    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'matplotlib_climate_3.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return file_path

if __name__ == '__main__':
    inp = "emissions.csv"
    df = pd.read_csv(inp)
    top_countries = df.nlargest(10, '2040')
    build_plot(top_countries)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
