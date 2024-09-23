import pandas as pd
import numpy as np
from IPython.display import display

class info_data:
    ''' Information and showing datatypes , null , missing values'''
    df = None
    
    def __init__(self,dsa):
        self.df=dsa
    #2.describing data and checking data types 
    def describe_data(self):
        display(self.df.head())
        display(self.df.describe())
    def datatypes(self):
        display(self.df.info())
    def datatypes_time(self,):
        
        self.df["date_added_y"] = pd.to_datetime(self.df['date_added_y'])
        self.df['year_added_y'] = self.df['date_added_y'].dt.year
        self.df['month_added_y'] = self.df['date_added_y'].dt.month
        self.df["date_added_x"] = pd.to_datetime(self.df['date_added_x'])
        self.df['year_added_x'] = self.df['date_added_x'].dt.year
        self.df['month_added_x'] = self.df['date_added_x'].dt.month
    #3.null value   
    def nulls(self):
        
        display(self.isnull())
        
        display(self.notnull())
    def removenull(self):
        try:
            self.df.dropna(inplace=True)
            
            display(self.df.info())
        except:
            print("Error: unable to remove null values from the list")
        
    
    def isnull(self):
        return self.df.isnull().sum()
    
    def notnull(self):
        return self.df.notnull().sum()
        
    #4.duplicate values   
    def duplicate(self):
        duplicates = self.df.duplicated()
        print(duplicates.sum())
        self.df = self.df.drop_duplicates()
    #3.unwanted column
    def unwantedcolumn(self,*argv):
        for arg in argv:
            self.df = self.df.drop(arg,axis=1)
            display(self.df)
    def show_missing(self, *argv):
        for arg in argv:
            display(self.show_missing_per_column(arg))
    
    def show_missing_per_column(self, column_name):
        return self.df[self.df[column_name].isnull()]
        

    def get_df(self):
        return self.df
    
    def set_df(self, df):
        self.df = df
        return
    #11. matrix form
    def matrix_form(self):
        
        data = np.array([self.df[1:2],self.df[1:3]])
        print(data)
    #12 numerical python
    def numericalpython(self):
        self.df = np.genfromtxt(self.df,delimiter="|")
        return self.df
    #9 Merging dataframes
    def merge_dataframe(self,df2,column):
        '''Merging dataframes'''
        try:
            self.df = pd.merge(self.df,df2,on=column)
            return self.df
        except:
            print('Merge dataframes not possible')
        

