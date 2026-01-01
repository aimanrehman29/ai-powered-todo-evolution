from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single todo item in memory.
    """

    id: int
    title: str
    description: str
    completed: bool = False

    @property
    def status(self) -> str:
        return "done" if self.completed else "open"
