import sys

from src.init import Init

if __name__ == '__main__':
    print(sys.version_info)
    if sys.version_info[0:2] != (3, 9):
        raise Exception('Requires python 3.9')

    Init()()

    pass
