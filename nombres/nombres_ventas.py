import pandas as pd


def proc(df, n=7):
    df2 = df.groupby("date")["amount"].sum()
    m = df2.rolling(n).mean()
    res = df2 / m - 1
    return res[res > 0.2]
