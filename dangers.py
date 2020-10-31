import abc
from typing import List

from user import User


class BaseDanger(abc.ABC):
    """ Базовый класс для всех опасностей
    """

    @property
    @abc.abstractmethod
    def sign(self) -> str:
        """ Знак, который подает создание, когда находится в соседней комнате
        """

    @abc.abstractmethod
    def action(self, user: User) -> None:
        """ Действие опасности на пользователя
        """

    @abc.abstractmethod
    def action_description(self) -> None:
        """ Описание перед действием
        """

    @abc.abstractmethod
    def on_shoot(self, user: User) -> None:
        """ Триггерится в случаях, когда пользователь попадает в создание из арбалета
        """

    @abc.abstractmethod
    def on_shoot_description(self) -> None:
        """ Описание при попадании
        """


class Pit(BaseDanger):
    """ Яма. Создает сквозняк в соседних комнатах.
        Если пользователь заходит в комнату с ямой, то умирает, и на этом заканчивается игра.
    """

    @property
    def sign(self) -> str:
        return 'Откуда-то дует ветер - поблизости яма'

    def action(self, user: User) -> None:
        user.is_dead = True

    def action_description(self) -> None:
        print('Вы упали в яму')

    def on_shoot(self, user: User) -> None:
        pass

    def on_shoot_description(self) -> None:
        print('Вы попали в яму. Но зачем?')


class Bats(BaseDanger):
    """ Стая летучих мышей. Производят шум, когда находятся в соседней комнате.
        Если пользователь находится в комнате с мышами, то его переносят в случайную комнату подземелья.
    """

    @property
    def sign(self) -> str:
        return 'Подозрительно шумно вокруг. Может, летучие мыши?'

    def action(self, user: User) -> None:
        user.move_to_random_room()

    def action_description(self) -> None:
        print('Вас уносят летучие мыши')

    def on_shoot(self, user: User) -> None:
        pass

    def on_shoot_description(self) -> None:
        print('Мыши увернулись от выстрелов, но испытали дискомфрот')


class Wumpus(BaseDanger):
    """ Вумпус. Отвратительно пахнет, когда находится в соседней от пользователя комнате.
        Если игрок окажется с ним в одной комнате, он умирает, и игра заканчивается.
    """

    @property
    def sign(self) -> str:
        return 'Невероятная вонь ударила Вам в ноздри - Вумпус рядом.'

    def action(self, user: User) -> None:
        user.is_dead = True

    def action_description(self) -> None:
        print('Вумпус убил вас, и это печально')

    def on_shoot(self, user: User) -> None:
        user.is_win = True

    def on_shoot_description(self) -> None:
        print('Вумпус повержен, вы победили!!!')


def create_dangers(pit_count=2, bats_count=2) -> List[BaseDanger]:
    """ Создание списка опасностей.
    """
    creatures = list()
    creatures += [Pit() for _ in range(pit_count)]
    creatures += [Bats() for _ in range(bats_count)]
    creatures.append(Wumpus())
    return creatures
