import torch
from abc import ABC
import numpy as np

class complex_numbers(ABC):
    def __init__(self, real_part, imag_part):
        self.real = real_part
        self.imag = imag_part

    def print(self):
        print('the number is :{} + {}i'.format(self.real,self.imag))

class norm(complex_numbers):
    def __init__(self, *Args, **Kwargs):
        super().__init__(*Args, **Kwargs)


    def compute_norm(self):
        return np.sqrt( self.real**2 + self.imag**2 )

class argument(complex_numbers):
    def __init__(self, *Args, **Kwargs):
        super().__init__(*Args, **Kwargs)

    def compute_argument(self):
        return np.arctan(self.imag/ self.real)

if __name__ == '__main__':
    number = argument( 1,2 )
    number.print()

    print('the norm is :{}'.format( number.compute_norm() ))