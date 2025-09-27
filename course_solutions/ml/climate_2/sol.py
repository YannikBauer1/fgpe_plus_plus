import os
import numpy as np
import pandas as pd
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"
import matplotlib.pyplot as plt
    
def build_plot(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    
    # Filter data for multiple countries
    countries = ["USA", "China", "India"]
    
    # Plot each country as a separate line
    for country in countries:
        country_data = df[df["Country"] == country]
        plt.plot(country_data["Year"], country_data["CO2 Emissions (Tons/Capita)"], 
                label=country, marker='o')
    
    # Add labels and legend
    plt.title("CO2 Emissions per Capita Over Time")
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions (Tons/Capita)")
    plt.legend()  # This shows the country names
    

############## DO NOT TOUCH AREA: START #################
def save_boxplot():
    # Save plot
    file_path = 'ml_climate_2.png'
    plt.savefig(file_path)
    plt.close()  # Close the figure to free memory
    return file_path

if __name__ == '__main__':
    inp = "climate_change_2.csv"
    build_plot(inp)
    path = save_boxplot()
    print(path)
############## DO NOT TOUCH AREA: END ###################

