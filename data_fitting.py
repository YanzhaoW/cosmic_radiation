from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import odr, stats


class ODR_fitter:
    def __init__(self, dataframe : pd.DataFrame):
        self.dataframe = dataframe
        self.dataframe.replace(0, np.nan, inplace = True)

    def fit(self, fnt : Callable, inits : list[float]):
        self.fnt = fnt
        if self.dataframe.empty:
            raise ValueError("Cannot fit empty data!")
        model = odr.Model(self.fnt)
        data = odr.RealData(x = self.dataframe['x'], y = self.dataframe['y'],
                            sx = self.dataframe['x_err'], sy = self.dataframe['y_err'])
        self.odr_reg = odr.ODR(data, model, beta0 = inits)
        self.res = self.odr_reg.run()
        res_var = self.odr_reg.output.__getattribute__('res_var')
        self.p_value = 1 - stats.chi2.cdf(res_var, df = 1)
        return self.res

    def save_plot(self, filename : str, title : str = ""):
        sns.scatterplot(data = self.dataframe, x= 'x', y = 'y', label = "Data")
        dataframe = self.dataframe.replace(np.nan, 0)
        plt.errorbar(dataframe['x'], dataframe['y'], 
                     xerr = dataframe['x_err'], yerr = dataframe['y_err'], 
                     linestyle = 'None', capsize = 5.0)
        fitted_fun = lambda x: self.fnt(self.res.beta, x)
        x_range = dataframe['x'].iloc[[0, -1]].values
        x = np.linspace(x_range[0], x_range[1], 1000)
        plt.plot(x, fitted_fun(x), color = 'r', label = "Regression line")
        plt.plot([], [], linestyle = 'None'  ,label = "p-value: %2.2f%%" % (self.p_value * 100))
        if title:
            plt.title(title)
        plt.legend(loc = "upper left")
        plt.savefig(filename, dpi = 200)
        plt.close()

    def print(self):
        print("===============fitting result:=================")
        self.res.pprint()
        print("p-value: %.2f%%" % (100 * self.p_value))
        print("===============================================")

if __name__ == "__main__":
    dataframe = pd.read_csv('data.csv')
    linear_fitter = ODR_fitter(dataframe)
    linear_fitter.fit(fnt = lambda p,x : p[0]* x + p[1], inits = [1., 0.])
    linear_fitter.print()
    linear_fitter.save_plot('figs/fitting_plot.png')

    dataframe = pd.read_csv('trig_data.csv')
    trig_fitter = ODR_fitter(dataframe)
    trig_fitter.fit(fnt = lambda p,x : np.power( p[1]* (np.cos( p[0] * x) + 1), 2), inits = [1, 1])
    trig_fitter.print()
    trig_fitter.save_plot('figs/trig_fitting.png', title = "Fitting fun: (p[1] * (cos(p[0]*x) + 1))^2")

    trig_fitter.fit(fnt = lambda p,x : p[0]*x*x + p[1], inits = [-1, 1])
    trig_fitter.print()
    trig_fitter.save_plot('figs/trig_fitting_quadratic.png', title = "Fitting fun: p[0]*x^2 + p[1]")
