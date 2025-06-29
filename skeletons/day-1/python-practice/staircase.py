import argparse
import re
'import anything else you need'

def staircase(n):
    'write your code here'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='the size of the staircase')
    args = parser.parse_args()
    staircase(args.n)