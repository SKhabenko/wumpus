import random

from typing import List, Optional

from dangers import BaseDanger
from room import Room
from user import User


class Maze:
    """ Лабиринт.
        Является центральной сущностью сервиса.
    """

    def __init__(self, user: User, rooms: List[Room], dangers: List[BaseDanger]):
        self._user = user
        self._rooms = rooms

        self._user.set_room_number(random.randint(0, len(self._rooms)))
        self._set_dangers_to_rooms(dangers)

    def _set_dangers_to_rooms(self, dangers: List[BaseDanger]) -> None:
        """ Размещает созданий по случайным пустым комнатам лабиринта
        """
        i = 0
        while i < len(dangers):
            random_room = self._rooms[random.randint(0, len(self._rooms) - 1)]
            if self._user.is_in_room(random_room.number) or random_room.is_danger_exists():
                continue
            random_room.add_danger(dangers[i])
            i += 1

    def available_user_moves(self) -> List[int]:
        """ Возвращает комнаты, в которые может перейти пользователь
        """
        current_user_room = self._rooms[self._user.current_room_number]
        return current_user_room.connected_rooms()

    def user_move(self, room_number: int) -> None:
        """ Переход пользователя в одну из допустимых позиций
        """
        if room_number not in self.available_user_moves():
            print('---\nЧитерство( Остаемся в той же комнате')
            return
        self._user.set_room_number(room_number)

    def user_shoot(self, room_number: int) -> None:
        """ Выстрел пользователя в одну из ближайших комнат
        """
        if room_number not in self.available_user_moves():
            print('---\nДо туда стрела не доберется')
            return
        shooting_room = self._rooms[room_number]
        shooting_room.create_shoot(self._user)

    def signs_in_current_room(self) -> Optional[list]:
        """ Возвращает список событий, которые триггерятся окружающими комнатами
        """
        res = set()
        for room_id in self.available_user_moves():
            room = self._rooms[room_id]
            if room.danger_sign():
                res.add(room.danger_sign())
        return res or None

    def dangers_actions_in_user_room(self) -> None:
        """ Действие, которое триггерится, когда игрок оказывается в одной комнате с опасностью
        """
        user_room = self._rooms[self._user.current_room_number]
        user_room.danger_action(self._user)
