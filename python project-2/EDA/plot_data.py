import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Plot:
    def __init__(self,df):
        self.df=df
    #6. Pair Plot
    def get_pair_plot(self):
        '''Pair Plot'''
        plt.figure()
        sns.pairplot(self.df)
        plt.show()
    #7. Heatmap
    def get_heatmap(self):
        '''heatmap creation'''
        try:
            plt.figure(figsize=(16,12))
            sns.heatmap(self.df.corr(), cmap="YlGnBu",annot=True,fmt=".1f")
            plt.show()
        except:
            print("Error: unable to create histogram")
            
    #5. Outlier   
    def get_outliers_box_plot(self):
        '''Getting outliers'''
        try:
            
            dims = (10, 10)
            fig, ax = plt.subplots(figsize=dims)
            sns.boxplot(ax=ax, data=self.df)
        except NameError as e:
            print("Wrong name of something? Error: ", e)
        return
    def get_outliers_histogram(self,column):
        '''Getting outliers'''
        try:
             
            plt.hist(self.df[column], bins=50)
            plt.title('Outliers')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.show()
        except:
            print("Error: unable to create histogram")
    def plot_hist(self):
        self.df.hist(figsize=(16, 14))
    def null_heatmap(self):
        '''Heatmap of null values'''
        try:
            plt.figure(figsize = (15,8))
            sns.heatmap(self.df.isnull(),cmap = 'Reds')
            plt.title('Null Values Heatmap')
            plt.show()
            
        except:
            print("Error: unable to create heatmap")
    def pie_chart_type(self,column):
        '''type column pie chart'''
        try:
            
            print(self.df[column].value_counts())
            plt.figure(figsize = (15,7))
            plt.pie(self.df[column].value_counts(),
       labels = [ 'Movie', 'TV Show'],
       colors = ['c','r'],
       shadow = True,
        explode = (0,0.08),
        autopct ='%1.1f%%',
        labeldistance = 1.1
       )
            plt.legend(['Movie', 'TV Show'])
            plt.title('Distribution of TV Show to Movie')
            plt.show() 
        except:
            print('Type column not found')
    
    def pie_chart_column(self,column):
        '''Pie chart of country'''
        try:
            plt.figure(figsize=(20,13))
            plt.pie(self.df[column].value_counts()[:10],
        labels = ['United State', 'Indian', 'United Kingdom', 'Japan','South Korea','Canada', 'Spain','France','Egypt','Mexico'],
        shadow = True,
        labeldistance = 1.1,
        startangle = 40,
        explode = (0,0,0.1,0,0,0,0,0,0,0),
        autopct ='%1.1f%%')
            plt.legend(['United State', 'Indian', 'United Kingdom', 'Japan','South Korea','Canada', 'Spain','France','Egypt','Mexico'])
            plt.title('Top countries as contributor to Netflix')
            plt.show()
        except:
            print('Country column not found')
    
    def distribution_type(self,column1,column2):
        '''Distribution of type of movies/tv shows'''
        try:
            print(self.df[column1].value_counts().head())
            plt.figure(figsize=(20,6))
            sns.countplot(x= column1,data= self.df,hue= column2,order = self.df[column1].value_counts().index[0:15])
            plt.xticks(rotation = 45)
            plt.show()
        except:
            print('Distribution not possible')
     
    def distribution_rating_type(self,column1,column2):
        '''Distribution of rating of movies/tv shows'''
        try:
            print(self.df[column1].value_counts().head())
            plt.figure(figsize = (12,8))
            sns.countplot(x=column1, data = self.df, hue=column2)
            plt.xlabel("Column1")
            plt.ylabel("Column2")
            plt.show()
        except:
            print('Distribution not possible')
            

            
        