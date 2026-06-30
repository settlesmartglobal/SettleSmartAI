import sys

from app.cli.commands import collect_emirates


def main():

    if len(sys.argv) < 2:

        print()

        print("Usage")

        print("-----")

        print("python3 -m app.main collect")

        return

    command = sys.argv[1]

    if command == "collect":

        collect_emirates()

    else:

        print("Unknown command")


if __name__ == "__main__":
    main()