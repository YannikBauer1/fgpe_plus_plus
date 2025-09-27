import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(portugal_emissions):
    years = [2040, 2041, 2042, 2043, 2044]
    # TODO this is what you need to complete

    plt.plot(years, portugal_emissions, color='blue')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions (MtCO2e)')
    plt.title('Portugal CO2 Emissions Over Time (2040-2044)')
    plt.grid(True)
    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'matplotlib_climate_7.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return file_path

if __name__ == '__main__':
    inp = "emissions.csv"
    df = pd.read_csv(inp)
    years = ['2040', '2041', '2042', '2043', '2044']
    portugal_data = df[df['country'] == 'Portugal'].iloc[0]
    portugal_emissions = [portugal_data[year] for year in years]
    build_plot(portugal_emissions)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################
