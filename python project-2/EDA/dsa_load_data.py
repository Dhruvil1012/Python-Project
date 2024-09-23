import pandas as pd
#1. loading the data
df = None
def load_data(position):
    '''Loading data'''
    df = pd.read_csv(position)
    return(df)




