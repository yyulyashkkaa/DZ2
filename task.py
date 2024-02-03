from dataclasses import dataclass, field
from datetime import datetime

from status import Status


@dataclass
class Task:
    name: str
    description: str = field(default="")
    status: Status = field(default=Status.NEW)
    creation_time: datetime = field(default_factory=datetime.now)
    change_time: datetime = field(default_factory=datetime.now)

    @classmethod
    def from_dict(cls, dct):
        return Task(dct["name"], dct["description"], Status(dct["status"]),
                    datetime.fromisoformat(dct["creation_time"]), datetime.fromisoformat(dct["change_time"]))

    def advance(self):
        self.status = self.status.advance()
        self.change_time = datetime.now()

    def retreat(self):
        self.status = self.status.retreat()
        self.change_time = datetime.now()

    def cancel(self):
        self.status = self.status.CANCELLED
        self.change_time = datetime.now()

    @classmethod
    def json_serial(cls, s):
        if isinstance(s, datetime):
            return s.isoformat()

        raise TypeError(f"Type {type(s)} is not serializable")
