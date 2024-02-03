from task import Task
from status import Status


def print_task(i, t):
    print(f"{i}. {t.name}")
    print(f"Описание: {t.description}")
    print(f"Статус: {t.status.name}")
    print(f"Создание: {t.creation_time.isoformat()}")
    print(f"Последнее изменение: {t.change_time.isoformat()}")
    print()


def parse_task_mode(tasks, i):
    command = "help"
    t = tasks[i - 1]

    while True:
        if command == "check":
            print_task(i, t)

        elif t.status != Status.CANCELLED and command == "cancel":
            t.cancel()
            print("Задача отменена")
            print()
        elif t.status == Status.CANCELLED and command == "resume":
            t.status = Status.NEW
            print("Задача возобновлена")
            print()

        elif t.status == Status.NEW and command == "start":
            t.advance()
            print("Задача выполняется")
            print()
        elif t.status == Status.IN_PROGRESS and command == "review":
            t.advance()
            print("Заадача ожидает ревью")
            print()
        elif t.status == Status.REVIEW and command == "accept":
            t.advance()
            print("Задача завершена")
            print()

        elif t.status == Status.IN_PROGRESS and command == "stop":
            t.retreat()
            print("Выполнение задачи остановлено")
            print()
        elif t.status == Status.REVIEW and command == "reject":
            t.retreat()
            print("Задача отправлена на доработку")
            print()
        elif t.status == Status.COMPLETED and command == "revisit":
            t.retreat()
            print("Выполнение задачи будет пересмотрено")
            print()

        elif t.status in (Status.COMPLETED, Status.CANCELLED) and command == "delete":
            print("Задача удалена")
            tasks.pop(i - 1)
            print()
            return parse_main(tasks)

        elif command == "rename":
            t.name = input("Новое имя: ")
            print()

        elif command == "new-description":
            t.description = input("Новое описание: ")
            print()

        elif command == "help":
            print("Доступны следубщие команды:")
            print("check: вывести информацию о выбранной задаче")

            if t.status == Status.NEW:
                print("start: начать выполнение задачи")
            elif t.status == Status.IN_PROGRESS:
                print("review: отправить выполненную задачу на ревью")
                print("stop: прекратить выполнение задачи")
            elif t.status == Status.REVIEW:
                print("accept: принять ревью")
                print("reject: отправить задачуна доработку")
            elif t.status == Status.COMPLETED:
                print("revisit: пересмотреть выполнение задачи, отправив на ревью")
            else:
                print("resume: сделатьзадачу сново доступной для выполнения")

            if t.status != Status.CANCELLED:
                print("cancel: отменить выполнение задачи")

            if t.status in (Status.COMPLETED, Status.CANCELLED):
                print("delete: удалить запись о задаче")

            print("rename: изменить имя задачи")
            print("new-description: изменить описание задачи")

            print("help: вывести это окно ещё раз (команды меняются в зависимости от статуса выбранной задачи")
            print("exit: закончить сессию")
            print()

        elif command == "back":
            print()
            return parse_main(tasks)
        elif command == "exit":
            return
        else:
            print("Неверная команда")
            print()

        command = input()


def parse_main(tasks):
    command = "help"
    while True:
        if command == "list":
            print("Задачи:")
            for i, t in enumerate(tasks, 1):
                print_task(i, t)
            print()

        elif command == "create":
            name = input("Название новой задачи: ")
            description = input("Описание: ")
            tasks.append(Task(name, description))
            print("Задача добавлена")
            print()
        elif command == "choose":
            ind = input("Номер задачи: ")
            try:
                ind = int(ind)
            except ValueError:
                print("Неверный номер задачи")
                print()
            else:
                if ind > len(tasks) or ind <= 0:
                    print("Неверный номер задачи")
                    print()
                else:
                    print()
                    return parse_task_mode(tasks, ind)
        elif command == "help":
            print("Доступны следубщие команды:")
            print("list: вывести список всех задач")
            print("create: создать новую задачу")
            print("choose: перети к настройкам конкретной задачи")
            print("help: вывести это окно ещё раз")
            print("exit: закончить сессию")
            print()
        elif command == "exit":
            return

        else:
            print("Неверная команда")
            print()

        command = input()
