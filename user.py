import random


class User:
    def __init__(self, arrows_count=5, maze_len=20):
        self.arrows_count = arrows_count
        self.current_room_number = None
        self.is_dead = False
        self.is_win = False
        # Костыль для переноса пользователя в рандомную комнату
        self._maze_len = maze_len

    def set_room_number(self, room_number) -> None:
        """ Сохранение положения пользователя в лабиринте
        """
        self.current_room_number = room_number

    def is_in_room(self, room_number) -> bool:
        return self.current_room_number == room_number

    def move_to_random_room(self):
        room_id = random.randint(0, self._maze_len - 1)
        self.set_room_number(room_id)
