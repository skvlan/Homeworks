import decimal

from colorama import Fore, Style, init


class frange(object):
    def __init__(self, *args):

        if len(args) == 1:
            self._left = decimal.Decimal(0)
            self._right = decimal.Decimal(args[0])
            self._step = decimal.Decimal(1)
        elif len(args) == 2:
            self._left = decimal.Decimal(args[0])
            self._right = decimal.Decimal(args[1])
            self._step = decimal.Decimal(1)
        elif len(args) == 3:
            self._left = decimal.Decimal(args[0])
            self._right = decimal.Decimal(args[1])
            self._step = decimal.Decimal(args[2])
        else:
            raise ValueError('Frange expects 1 to 3 arguments, got {}'.format(len(args)))



    def __next__(self):
        if (self._step > 0 and self._left >= self._right) or (self._step < 0 and self._left <= self._right):
            raise StopIteration('FFFF')
        _left = float(self._left)
        self._left += self._step

        return _left

    def __iter__(self):
        return self



assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')





class colorizer:
    def __init__(self, color):
        self.color = color
        self.color_dict = {
            'red': Fore.RED,
            'black': Fore.BLACK,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'blue': Fore.BLUE,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE
        }

    def __enter__(self):
        print(self.color_dict.get(self.color, ''), end='')
        return self

    def __exit__(self, type, value, traceback):
        print(Style.RESET_ALL, end="")


print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with colorizer('red'):
    print('printed in red')
print('printed in default color')

with colorizer('black'):
    print('printed in black')
print('printed in default color')

with colorizer('magenta'):
    print('printed in magenta')
print('printed in default color')

with colorizer('blue'):
    print('printed in blue')
print('printed in default color')