import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def missing_values(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)

    num_cols = ['Price', '24h Volume', 'Market Cap', '1h', '24h', '7d', '30d', 'Circulating Supply', 'Total Supply']
    
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df = df.dropna(subset=["Coin Name"])

    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    df['Price_to_MarketCap_Ratio'] = df['Price'] / df['Market Cap']
    df['Volatility_Index'] = (df['1h'] + df['24h']) / 2

    grouped = df.groupby("Coin Name").agg('mean')
    
    grouped = grouped.sort_values("Coin Name").reset_index()
    return grouped


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    file_path = 'ml_crypto_1.csv'
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == '__main__':
    inp = "crypto_currencies.csv"
    df = missing_values(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################


