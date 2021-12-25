import argparse


def echo_func(*args, **kwargs):
    for arg in args:
        print(f"arg = {arg}")

    for key, value in kwargs.items():
        print(f"key = {key}, value = {value}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Check the options.")

    parser.add_argument(
        "numbers",
        metavar="N",
        type=int,
        nargs="+",
        help="""The numbers to check.""",
    )

    parser.add_argument(
        "-e",
        "--even",
        dest="even",
        action="store_true",
        help="Only check even numbers.",
    )

    parser.add_argument(
        "-l",
        "--level",
        dest="level",
        type=str,
        default="INFO",
        help="The logging level.",
    )

    arguments = parser.parse_args()

    echo_func(*arguments.numbers, even=arguments.even, level=arguments.level)
