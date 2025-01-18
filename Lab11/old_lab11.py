from dataclasses import dataclass


@dataclass
class Character:
    """ The link class

    Attributes:
    life   -- the initial life of the character
    attack -- the initial attack of the character
    """

    life: int
    attack: int
    position: tuple


@dataclass
class Monster:
    """ The class of the monsters

    Attributes:
    life     -- the initial life of the monster
    attack   -- the initial attack of the monster
    symbol   -- the symbol of the monster (U, D, L or R)
    position -- the initial position of the monster
    """

    life: int
    attack: int
    symbol: str
    position: tuple


@dataclass
class Item:
    """ The class of the items

    Attributes:
    name     -- the name of the item
    symbol   -- the symbol of the item (v or d)
    position -- the initial position of the monster
    status   -- how much it adds to the life or attack of link
    """

    name: str
    symbol: str
    position: tuple
    status: int


def print_dungeon(dungeon: list[list[str]]):
    """ Print the dungeon

    Parameters:
    area -- the dungeon that will be printed
    """

    for line in dungeon:
        print(" ".join(line))


def no_vanish(items: list, monsters: list, exit_pos: tuple,
              link: tuple, dungeon: list[list[str]]):
    """ Make sure things don't disappear"""
    def reappear(symbol: str, pos: tuple):
        if dungeon[i][j] not in [symbol, "P"]:
            move((i, j), (i, j), symbol, items, link, monsters,
                 exit_pos, dungeon)

    for item in items:
        symbol = item.symbol
        i, j = item.position
        reappear(symbol, (i, j))

    for monster in monsters:
        symbol = monster.symbol
        i, j = monster.position
        reappear(symbol, (i, j))

    i, j = exit_pos
    reappear("*", (i, j))


def data_extractor() -> tuple:
    """ Extract the data from the input

    Returns:
    tuple -- the data extracted in a tuple
    """

    data = input()
    # There is two ways to receive the data, separate by space (A B)
    # or by comma (A,B)
    separator = "," if "," in data else " "
    return tuple(int(elem) for elem in data.split(separator))


def monster_data() -> list:
    """ Extract the data from the input

    Returns:
    list -- the data extracted in a list
    """

    data = input().split()
    data[:2] = map(int, data[:2])  # Make sure life and damage are integers
    # Correct the position to a tuple
    data[3] = tuple(int(elem) for elem in data[3].split(","))
    return data


def item_data() -> list:
    """ Extract the data from the input

    Returns:
    list -- the data extracted in a list
    """

    data = input().split()
    # Correct the position to a tuple
    data[2] = tuple(int(elem) for elem in data[2].split(","))
    data[3] = int(data[3])  # Make sure the status is a integer
    return data


def character_definer() -> tuple:
    """ Defines link

    Returns:
    tuple -- the information about link
    """

    link_data = data_extractor()

    return Character(link_data[0], link_data[1], (0, 0))


def monsters_definer() -> list:
    """ Append the monsters to the list of monsters"""

    monsters = []
    for i in range(int(input())):
        monsters.append(Monster(*monster_data()))

    return monsters


def items_definer() -> list:
    """ Append the items to the list of items"""

    items = []
    for i in range(int(input())):
        items.append(Item(*item_data()))

    return items


def dungeon_maker(lines: int, columns: int, monsters: list, items: list,
                  link_pos: tuple, exit_pos: tuple) -> list[list[str]]:
    """ Make the dungeon

    Parameters:
    lines           -- the number of lines of the matrix
    columns         -- the number of columns of the matrix
    monsters        -- the list of monsters
    items           -- the list of items
    link_pos        -- the position of link
    exit_pos        -- the position of the exit

    Returns:
    list[list[str]] -- the dungeon matrix
    """

    dungeon = []
    # First we define the dungeon as a matrix ixj of dots "."
    for i in range(lines):
        line = []
        for j in range(columns):
            line.append(".")
        dungeon.append(line)

    # Them we add the monsters ("U", "D", "R" or "L")
    for monster in monsters:
        pos = monster.position
        dungeon[pos[0]][pos[1]] = monster.symbol

    # Them the items ("v" or "d")
    for item in items:
        pos = item.position
        dungeon[pos[0]][pos[1]] = item.symbol

    # And finally we add Link ("P") and the exit ("*")
    dungeon[link_pos[0]][link_pos[1]] = "P"
    dungeon[exit_pos[0]][exit_pos[1]] = "*"

    return dungeon


def move_monster(monsters: list, items: list, lines: int, columns: int,
                 link: tuple, exit_pos: tuple, dungeon: list[list[str]]):

    for monster in monsters:
        symbol = monster.symbol  # Discover the type of monster
        i, j = monster.position  # The initial position of the monster
        # Make it move correctly
        if symbol == "U" and (lines > i - 1 >= 0):
            monster.position = (i - 1, j)
        elif symbol == "D" and (lines > i + 1 >= 0):
            monster.position = (i + 1, j)
        elif symbol == "L" and (columns > j - 1 >= 0):
            monster.position = (i, j - 1)
        elif symbol == "R" and (columns > j + 1 >= 0):
            monster.position = (i, j + 1)


def take_item(items: list, link: tuple, dungeon: list[list[str]]):
    for item in items.copy():
        if link.position == item.position:
            print(f"[{item.symbol}]Personagem adquiriu o objeto {item.name}" +
                  f" com status de {item.status}")
            if item.symbol == "v":
                link.life += item.status
                link.life = link.life if link.life > 0 else 0
            elif item.symbol == "d":
                link.attack += item.status
                link.attack = link.attack if link.attack >= 1 else 1
            items.remove(item)


def combat(monsters: list, link: tuple, dungeon: list[list[str]]):
    for monster in monsters:
        if link.position == monster.position and link.life > 0:
            monster.life -= link.attack
            if monster.life <= 0:
                print(f"O Personagem deu {link.attack + monster.life} de" +
                      f" dano ao monstro na {link.position}")
                monsters.remove(monster)
            else:
                damage_taken = monster.attack if link.life - \
                    monster.attack >= 0 else link.life
                link.life -= monster.attack
                link.life = link.life if link.life > 0 else 0
                print(f"O Personagem deu {link.attack} de dano" +
                      f" ao monstro na {link.position}")
                print(f"O Monstro deu {damage_taken} de dano ao" +
                      f" Personagem. Vida restante = {link.life}")


def move(origin: tuple, destiny: tuple, symbol: str, items: list, link: tuple,
         monsters: list, exit_pos: tuple, dungeon: list[list[str]]):
    """ Move the entity and print it

    Parameters:
    origin  -- where the entity is
    destiny -- where the entity will go
    entity  -- the entity that will move
    dungeon -- the matrix that the entity will move through
    """

    i, j = origin
    x, y = destiny
    # Move the entity from origin to destiny
    if symbol == "P" and link.life > 0:
        link.position = (x, y)
        no_vanish(items, monsters, exit_pos, link, dungeon)
        print_dungeon(dungeon)
        print()

    if (i, j) != link.position:
        dungeon[i][j] = "."
    if dungeon[x][y] != "P":
        dungeon[x][y] = symbol


def run_game(origin, destiny, items, link, monsters, exit_pos, dungeon,
             lines, columns):

    take_item(items, link, dungeon)
    combat(monsters, link, dungeon)
    move(origin, destiny, "P", items, link, monsters, exit_pos, dungeon)
    move_monster(monsters, items, lines, columns, link,
                 exit_pos, dungeon)


def main(first_move=True):
    link = character_definer()
    lines, columns = data_extractor()
    link_pos, exit_pos = data_extractor(), data_extractor()
    link.position = link_pos
    monsters, items = monsters_definer(), items_definer()
    dungeon = dungeon_maker(lines, columns, monsters, items,
                            link_pos, exit_pos)

    i, j = link.position
    for k in range(len(dungeon)):
        if first_move:
            first_move = False
            while i < lines - 1 and link.life != 0 and \
                    link.position != exit_pos:
                run_game((i, j), (i + 1, j), items, link, monsters, exit_pos,
                         dungeon, lines, columns)
                i += 1
        else:
            while i >= 0 and link.life != 0 and link.position != exit_pos:
                direction = int((-1)**(i - 1))
                while columns > j + direction >= 0 and \
                        link.life != 0 and link.position != exit_pos:
                    run_game((i, j), (i, j + direction), items, link, monsters,
                             exit_pos, dungeon, lines, columns)
                    j += direction
                if i <= 0:
                    break
                run_game((i, j), (i - 1, j), items, link, monsters,
                         exit_pos, dungeon, lines, columns)
                if link.life == 0:
                    dungeon[i][j] = "X"
                    print_dungeon(dungeon)
                    print()
                    break
                i -= 1
            if link.position == exit_pos:
                print_dungeon(dungeon)
                print("\nChegou ao fim!")
                break


if __name__ == "__main__":
    main()
