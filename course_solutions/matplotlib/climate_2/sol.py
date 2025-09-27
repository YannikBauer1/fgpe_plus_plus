import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(india_emissions):
    years = [2040, 2041, 2042, 2043, 2044]
    # TODO this is what you need to complete
    plt.bar(years, india_emissions)


    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'matplotlib_climate_2.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return file_path

if __name__ == '__main__':
    inp = "emissions.csv"
    df = pd.read_csv(inp)
    years = ['2040', '2041', '2042', '2043', '2044']
    india_data = df[df['country'] == 'India'].iloc[0]
    india_emissions = [india_data[year] for year in years]
    build_plot(india_emissions)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
