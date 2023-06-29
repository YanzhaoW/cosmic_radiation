import numpy as np
import pandas as pd
import math
from typing import Callable

def Linear_fun(slope : float, bias: float) -> Callable:
    return lambda x: slope * x + bias

def Trig_fun(power: float, k : float) -> Callable:
    return lambda x : (math.cos(k * x) + 1) ** power

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

    def __call__(self, size : int, x_min: float, x_max: float):
        x_err = self.__generate_xerr(size)
        y_err = self.__generate_yerr(size)
        x_mean = np.linspace(start = x_min, stop = x_max, num = size, dtype = float)
        y_mean = np.array(list(map(self.call_back, x_mean)))

        if np.any(np.iscomplex(y_mean)):
            print(y_mean)
            raise ValueError("Complex error occured!")

        x = self.__generate_random(means = x_mean, errs = x_err)
        y = self.__generate_random(means = y_mean, errs = y_err)
        self.dataframe = pd.DataFrame({'x': x, 'x_err': x_err, 'y': y, 'y_err': y_err})

    def SaveToCsv(self, filename : str):
        self.dataframe.to_csv(filename, index = False, float_format = '%.3f')

if __name__ == "__main__":
    generator = Random_Gen(Linear_fun(2.3, 5.2))
    generator.set_xerror(min = 0.5, max = 1.2)
    generator.set_yerror(min = 4, max = 5)
    generator(size = 20, x_min = 2, x_max = 23)
    generator.SaveToCsv("data.csv")

    period = 3.2
    power = 2
    trig = Random_Gen(Trig_fun(power = power, k = 2 * math.pi / period))
    trig.set_xerror(min = 0.005, max = 0.005)
    trig.set_yerror(min = 0.1, max = 0.1)
    trig(size = 20, x_min = - period / 2, x_max = period / 2)
    trig.SaveToCsv("trig_data.csv")

