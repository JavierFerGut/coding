import os, sys
import pandas as pd
def load(path) :
    df=pd.read_csv( path )
    l = len(df)
    if l==0 :
        return None
    return df
def summary(df,column , top = 5):
    try:
        counts=df[column].value_counts( ).head(top)
    except:
        counts = None
    if counts == None: return {}
    result={ 'column':column,'top':counts.to_dict( ),'total':int(df[column].count()) }
    return result
