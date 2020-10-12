import sys
sys.path.append(r'C:\G\py-import-conflict')
from A.foo_a import foo_a
from utils import echo_b

if __name__ == '__main__':
    foo_a()
    echo_b()
