from clize import run

from .shell import launch_shell


def main(directory="."):
    launch_shell(directory)


if __name__ == "__main__":
    run(main)
