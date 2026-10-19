import pandas as pd


def calc(df, n=252):
    df2 = df.pct_change().dropna()
    m = df2.mean() * n
    s = df2.std() * n ** 0.5
    res = m / s
    return res[res > 1]
