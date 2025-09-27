import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(china_emissions):
    years = [2040, 2041, 2042, 2043, 2044]
    # TODO this is what you need to complete
    plt.plot(years, china_emissions)

    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'matplotlib_climate_1.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return file_path

if __name__ == '__main__':
    inp = "emissions.csv"
    df = pd.read_csv(inp)
    years = ['2040', '2041', '2042', '2043', '2044']
    china_data = df[df['country'] == 'China'].iloc[0]
    china_emissions = [china_data[year] for year in years]
    build_plot(china_emissions)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
