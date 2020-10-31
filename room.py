from typing import List

from dangers import BaseDanger
from user import User


class Room:
    """ Объект комнаты, из множества которых состоит лабиринт
    """

    def __init__(self, number):
        self.number = number
        self._danger = None
        self._next_rooms = []

    def add_connection(self, room) -> None:
        """ Добавляет комнату, в которую можно осуществить переход
        """
        self._next_rooms.append(room)

    def connected_rooms(self) -> List[int]:
        """ Возвращает список связанных комнат
        """
        return [r.number for r in self._next_rooms]

    def add_danger(self, danger: BaseDanger) -> None:
        """ Добавить существо в комнату
        """
        self._danger = danger

    def is_danger_exists(self):
        """ Есть ли что-то в этой комнате
        """
        return self._danger is not None

    def danger_sign(self):
        """ Признаки опасности в этой комнате
        """
        if not self.is_danger_exists():
            return None
        return self._danger.sign

    def danger_action(self, user: User):
        """ Действие, выполняемое над пользователем, в случае, если тот оказался в комнате
        """
        if not self.is_danger_exists():
            return None
        self._danger.action_description()
        return self._danger.action(user)

    def create_shoot(self, user: User):
        if not self.is_danger_exists():
            print('Вы выстрелили, но в комнате пусто')
            return None
        self._danger.on_shoot_description()
        return self._danger.on_shoot(user)


def create_rooms() -> List[Room]:
    """ Создать комнаты со всеми возможными переходами
    """
    rooms = [Room(number=x) for x in range(0, 20)]
    for room in rooms:
        for n in room_connections[room.number]:
            room.add_connection(rooms[n])
    return rooms


# Возможные переходы между комнат
room_connections = {
    0: (5, 1, 4),
    1: (0, 2, 10),
    2: (1, 3, 8),
    3: (2, 4, 7),
    4: (0, 6, 3),
    5: (0, 17, 18),
    6: (4, 9, 17),
    7: (3, 9, 16),
    8: (2, 16, 19),
    9: (6, 7, 11),
    10: (1, 18, 19),
    11: (9, 12, 15),
    12: (11, 13, 17),
    13: (12, 14, 18),
    14: (13, 15, 19),
    15: (11, 14, 16),
    16: (7, 8, 15),
    17: (5, 6, 12),
    18: (5, 10, 13),
    19: (8, 10, 14),
}
