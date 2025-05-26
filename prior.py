import torch
from abc import ABC

class complex_numbers(ABC):
    def __init__(self, real_part, imag_part):
        self.real = real_part
        self.imag = imag_part

    def print(self):
        print('{} + {}i'.format(self.real,self.imag))

class norm(complex_numbers):
    def __init__(self, *Args, **Kwargs):
        super().__init__(*Args, **Kwargs)

if __name__ == '__main__':
    number = norm( 1,2 )
    number.print()
