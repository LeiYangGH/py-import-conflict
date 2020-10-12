from utils_module.utils import \
    echo_a  # ModuleNotFoundError: No module named '__main__.utils_module'; '__main__' is not a package


def foo_a():
    echo_a()


if __name__ == '__main__':
    echo_a()
