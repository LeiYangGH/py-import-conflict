import sys
sys.path.append(r'../A')
from foo_a import foo_a #error: ImportError: cannot import name 'echo_a'
from utils import echo_b

if __name__ == '__main__':
    echo_b()
