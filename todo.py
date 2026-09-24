from pprint import pprint
from dataclasses import dataclass


@dataclass
class Todo:
    id: int = 0
    title: str = ""
    completed: bool = False

    def truc(self):
        pass

def main():
    t = Todo(1,"Python",False)

    print(t)


if __name__ == '__main__':
    main()
