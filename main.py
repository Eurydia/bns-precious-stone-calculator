from pts_calculator import PreciousCalculator
from configure import SETTING

def main():
    calc = PreciousCalculator()
    calc.setting = SETTING
    calc.calculate()


if __name__ == '__main__':
    main()