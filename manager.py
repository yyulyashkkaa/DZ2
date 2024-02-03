import json
from dataclasses import asdict

from task import Task


class ManagerLaunchException(RuntimeError):
    pass


class Manager:
    def __init__(self, filename):
        self.data_path = filename
        self.tasks = None
        self._w_file = None

    def __enter__(self):
        try:
            with open(self.data_path, encoding="utf-8") as file:
                self.tasks = [json.loads(s, object_hook=Task.from_dict) for s in file if s.strip()]
        except json.JSONDecodeError:
            raise ManagerLaunchException("данные в указанном файле некорректны")
        except FileNotFoundError:
            self.tasks = []
        except IOError as e:
            raise ManagerLaunchException(e.args[0])

        try:
            self._w_file = open(self.data_path, "w", encoding="utf-8")
        except IOError as e:
            raise ManagerLaunchException(e.args[0])

        return self.tasks

    def __exit__(self, exc_type, exc_val, exc_tb):
        for task in self.tasks:
            json.dump(asdict(task), self._w_file, default=Task.json_serial, ensure_ascii=False)
            self._w_file.write("\n")
        self._w_file.close()


if __name__ == '__main__':
    with Manager("db.jsonl") as tasks:
        tasks.append(Task("kek"))
