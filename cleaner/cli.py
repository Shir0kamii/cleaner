from clize import run

from .shell import launch_shell


def cleaner(directory="."):
    launch_shell(directory)


def run_cleaner():
    run(cleaner)


if __name__ == "__main__":
    run(cleaner)
