import numpy as np
import statistics as stats
class maths_dsa:
    df = None
    def __init__(self,dsa):
        self.df=dsa
    #14.Segregate the data based on value
    def slicing_data(self,col_name,value):
        '''Slcing data by value'''
        try:
            dsa_highslicingdata = self.df[self.df[col_name]>int(value)]
            print(dsa_highslicingdata.head())
            dsa_highslicingdata = self.df[self.df[col_name]<int(value)]
            print(dsa_highslicingdata.head())
            
        except KeyError:
            print("Error: 'year' column not found in dataset.")
    #16. category data 
    def category(self,category,col_name):
        '''Category data'''
        try:
            dsa_category = self.df[self.df[col_name]==int(category)]
            print(dsa_category.head())
        except KeyError:
            print("Error: Category not  found in dataset.")
    #13. slice a part of the data
    def slice_data(self, start=None, end=None):
        '''Slcing part of data'''
        try:
            if start is None:
                start = 0
            if end is None:
                end = len(self.df)
            sliced_data = self.df.iloc[start:end]
            return sliced_data
        except IndexError:
            print("Error: Index out of range.")
            return None
    #10.slicing data of particular column
    def slice_by_year(self,col_name, year):
        '''Slcing by particular column'''
        try:
            sliced_data = self.df[self.df[col_name] == year]
        except KeyError:
            print("Year column not found in the data")
            sliced_data = None
        return sliced_data
   #15. mathematical and statistical data
    def calculate_mean(self, column):
        '''Mathematical and statistical operation'''
        try:
            mean = np.mean(self.df[column])
        except KeyError:
            print(f"{column} column not found in the data")
            mean = None
        except TypeError:
            print(f"{column} column contains non-numeric data")
            mean = None
        return mean
    
    def calculate_median(self, column):
        '''Mathematical and statistical operation'''
        try:
            median = np.median(self.df[column])
        except KeyError:
            print(f"{column} column not found in the data")
            median = None
        except TypeError:
            print(f"{column} column contains non-numeric data")
            median = None
        return median
    
    def calculate_mode(self, column):
        '''Mathematical and statistical operation'''
        try:
            mode = stats.mode(self.df[column])
        except KeyError:
            print(f"{column} column not found in the data")
            mode = None
        except stats.StatisticsError:
            print(f"No mode found for {column} column")
            mode = None
        return mode

            