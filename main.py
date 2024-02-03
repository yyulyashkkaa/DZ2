import sys

from manager import Manager, ManagerLaunchException
from parse import parse_main


if __name__ == '__main__':
    try:
        with Manager(sys.argv[1]) as tasks:
            parse_main(tasks)
    except ManagerLaunchException as e:
        print(f"Ошибка запуска: {e.args[0]}")
