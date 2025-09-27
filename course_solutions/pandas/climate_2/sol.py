import pandas as pd

def high_emission(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)
    filtered = df[df["2040"] > 100]
    return filtered


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    df.to_csv("pandas_climate_2.csv", index=False)
    return "pandas_climate_2.csv"

if __name__ == '__main__':
    inp = "emissions.csv"
    df = high_emission(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
