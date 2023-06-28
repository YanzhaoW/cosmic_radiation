import pandas as pd
from typing import Callable
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import odr

class Fitter:
    def __init__(self, dataframe : pd.DataFrame):
        self.dataframe = dataframe

    def linear(self, fnt : Callable):
        if self.dataframe.empty:
            raise ValueError("Cannot fit empty data!")
        model = odr.Model(fnt)
        data = odr.RealData(x = self.dataframe['x'], y = self.dataframe['y'], sx = self.dataframe['x_err'], sy = self.dataframe['y_err'])
        ODR_reg = odr.ODR(data, model, beta0 = [1., 0.])
        self.res = ODR_reg.run()

    def save_plot(self):
        sns.scatterplot(data = self.dataframe, x= 'x', y = 'y', label = "Data")
        plt.errorbar(self.dataframe['x'], self.dataframe['y'], 
                     xerr = self.dataframe['x_err'], yerr = self.dataframe['y_err'], 
                     linestyle = 'None', capsize = 5.0)
        slope = self.res.beta[0]
        offset = self.res.beta[1]
        fitted_fun = lambda x: slope*x + offset
        x = self.dataframe['x'].iloc[[0, -1]]
        plt.plot(x, fitted_fun(x), color = 'r', label = "Regression line")
        plt.legend(loc = "upper left")
        plt.savefig('fitting_plot.png', dpi = 200)

    def print(self):
        self.res.pprint()

if __name__ == "__main__":
    dataframe = pd.read_csv('data.csv')
    fitter = Fitter(dataframe)
    fitter.linear(fnt = lambda p,x : p[0]* x + p[1])
    fitter.print()
    fitter.save_plot()
