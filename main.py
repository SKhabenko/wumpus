from dangers import create_dangers
from maze import Maze
from room import create_rooms
from user import User

ACTION_SHOOT = 'в'
ACTION_MOVE = 'и'
ACTION_DEFAULT = 'default'


def action_shoot(user: User, maze: Maze) -> None:
    room_number = int(input('Куда стрелять? : '))
    success_shot = maze.user_shoot(room_number)
    if success_shot:
        user.arrows_count -= 1


def action_move(user: User, maze: Maze) -> None:
    room_number = int(input('В какую комнату? : '))
    maze.user_move(room_number)


def action_default(user: User, maze: Maze) -> None:
    print('---\nНепонятно. Попробуем еще раз?')


actions_mapper = {
    ACTION_SHOOT: action_shoot,
    ACTION_MOVE: action_move,
    ACTION_DEFAULT: action_default,
}


def current_room_info(user: User, maze: Maze) -> str:
    res = f'---\nВы находитесь в комнате номер {user.current_room_number}.\n'
    creature_signs = maze.signs_in_current_room()
    if creature_signs:
        res += f'В соседних комнатах что-то происходит: \n'
        for sign in creature_signs:
            res += sign + "\n"
    res += f'Отсюда можно перейти в комнаты {", ".join([str(x) for x in maze.available_user_moves()])} \n'
    return res


if __name__ == '__main__':
    print('---\nДобро пожаловать в игру "Охота на Вампуса!"')

    user = User()
    rooms = create_rooms()
    dangers = create_dangers()
    maze = Maze(user, rooms, dangers)

    while True:
        maze.dangers_actions_in_user_room()
        if user.is_dead or user.is_win or user.arrows_count == 0:
            print('Вот и все!')
            break
        print(current_room_info(user, maze))

        action = input('Выстрелить или идти? (в-и) : ')
        actions_mapper.get(action.lower() if action.isalpha() else ACTION_DEFAULT, action_default)(user, maze)
