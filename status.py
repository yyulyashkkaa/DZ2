from enum import IntEnum, auto


class Status(IntEnum):
    NEW = auto()
    IN_PROGRESS = auto()
    REVIEW = auto()
    COMPLETED = auto()
    CANCELLED = auto()

    def advance(self):
        return Status(self + 1)

    def retreat(self):
        return Status(self - 1)


if __name__ == '__main__':
    print(Status.NEW.name)
