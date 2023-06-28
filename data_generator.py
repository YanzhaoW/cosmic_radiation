import numpy as np
import pandas as pd
from typing import Callable

def Linear_fun(slope : float, bias: float) -> Callable:
    return lambda x: slope * x + bias

class Random_Gen:
    def __init__(self, call_back : Callable):
        self.call_back = call_back
        self.rng = np.random.default_rng(66666)
        self.dataframe = pd.DataFrame()
        self.xerror_min = 0
        self.xerror_max = 0
        self.yerror_min = 0
        self.yerror_max = 0

    def set_xerror(self, min: float, max: float):
        self.xerror_min = min
        self.xerror_max = max

    def set_yerror(self, min: float, max: float):
        self.yerror_min = min
        self.yerror_max = max

    def __generate_random(self, means: np.ndarray, errs: np.ndarray) -> np.ndarray:
        if len(means) != len(errs):
            raise ValueError("size of mean values is not equal to the size of errors!")
        return np.array([self.rng.normal(loc = mean, scale = err) for mean, err in zip(means, errs)])

    def __generate_xerr(self, num:int) -> np.ndarray:
        errs = self.rng.random(num)
        errs = np.multiply(errs, self.xerror_max - self.xerror_min)
        errs = np.add(errs, self.xerror_min)
        return errs

    def __generate_yerr(self, num:int) -> np.ndarray:
        errs = self.rng.random(num)
        errs = np.multiply(errs, self.yerror_max - self.yerror_min)
        errs = np.add(errs, self.yerror_min)
        return errs

    def __call__(self, num : int, min: float, max: float):
        x_err = self.__generate_xerr(num)
        y_err = self.__generate_yerr(num)
        x_mean = np.arange(start = min, stop = max, step = (max-min)/num, dtype = float)
        y_mean = self.call_back(x_mean)
        x = self.__generate_random(means = x_mean, errs = x_err)
        y = self.__generate_random(means = y_mean, errs = y_err)
        self.dataframe = pd.DataFrame({'x': x, 'x_err': x_err, 'y': y, 'y_err': y_err})

    def SaveToCsv(self, filename : str = "data.csv"):
        self.dataframe.to_csv(filename, index = False, float_format = '%.3f')

if __name__ == "__main__":
    generator = Random_Gen(Linear_fun(2.3, 5.2))
    generator.set_xerror(min = 0.5, max = 1.2)
    generator.set_yerror(min = 4, max = 5)
    generator(num = 20, min = 2, max = 23)
    generator.SaveToCsv()
