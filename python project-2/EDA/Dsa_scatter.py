import matplotlib.pyplot as plt
#8. Scatter Plot
class ScatterPlot:
    '''Scatter Plot'''
    def __init__(self,df):
        self.df = df
        
    def create_plot(self,x,y):
        try:
            
            plt.scatter(self.df[x], self.df[y])
            plt.xlabel('X axis')
            plt.ylabel('Y-axis')
            plt.title('Scatter Plot')
            plt.show()
        except Exception as e:
            print('Error creating scatter plot:', e)
            

