# from utils import echo_a #when run B.main: ImportError: cannot import name 'echo_a'
from A.utils import echo_a

def foo_a():
    echo_a()

if __name__ == '__main__':
    echo_a()
