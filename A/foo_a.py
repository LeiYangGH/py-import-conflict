from utils_module.utils import echo_a #when run B: ImportError: cannot import name 'echo_a'
# from .utils_module.utils import echo_a #if use relative import, when run A: ModuleNotFoundError: No module named '__main__.utils_module'; '__main__' is not a package

def foo_a():
    echo_a()


if __name__ == '__main__':
    echo_a()
