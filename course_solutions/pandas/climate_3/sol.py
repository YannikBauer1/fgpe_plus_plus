import pandas as pd

def average(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    mean_co2 = df["2040"].mean()
    median_co2 = df["2040"].median()
    min_co2 = df["2040"].min()
    max_co2 = df["2040"].max()
    return mean_co2, median_co2, min_co2, max_co2


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = "emissions.csv"
    mean, median, min, max = average(inp)
    print(mean, median, min, max)
############## DO NOT TOUCH AREA: END ###################