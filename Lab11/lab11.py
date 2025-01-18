from dataclasses import dataclass


@dataclass
class Character:
    """ The link class

    Attributes:
    life     -- the character's initial life
    attack   -- the character's initial attack
    position -- the character's initial position
    exit_pos -- the exit's position
    """

    life: int
    attack: int
    position: tuple = (0, 0)
    exit_pos: tuple = (0, 0)

    def condition(self):
        """ Check if link is alive or if he is in the exit's position

        Returns:
        boolean -- if a condition has been fulfilled (True) or if not (False)
        """

        if self.life != 0 and self.position != self.exit_pos:
            return True


@dataclass
class Monster:
    """ The class of the monsters

    Attributes:
    life     -- the monster's initial life
    attack   -- the monster's initial attack
    symbol   -- the monster's symbol (U, D, L or R)
    position -- the monster's initial position
    """

    life: int
    attack: int
    symbol: str
    position: tuple


@dataclass
class Item:
    """ The class of the items

    Attributes:
    name     -- the item's name
    symbol   -- the item's symbol (v or d)
    position -- the item's position
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
    print()


def data_extractor(data) -> tuple:
    """ Extract the data from the input

    Returns:
    tuple -- the data extracted in a tuple
    """

    # There is two ways to receive the data, separate by space (A B)
    # or by comma (A,B)
    separator = "," if "," in data else " "

    return tuple(int(elem) for elem in data.split(separator))


def dungeon_maker(lines: int, columns: int, monsters: list, items: list,
                  link: tuple) -> list[list[str]]:
    """ Make the dungeon

    Parameters:
    lines    -- the number of lines of the matrix
    columns  -- the number of columns of the matrix
    monsters -- the list of monsters
    items    -- the list of items
    link     -- the position of link

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

    # Them we add the items ("v" or "d")
    for item in items:
        i, j = item.position
        dungeon[i][j] = item.symbol

    # Them the monsters ("U", "D", "R" or "L")
    for monster in monsters:
        i, j = monster.position
        dungeon[i][j] = monster.symbol

    # And finally we add Link ("P") and the exit ("*")
    i, j = link.position
    x, y = link.exit_pos
    dungeon[x][y] = "*"
    dungeon[i][j] = "P" if link.life > 0 else "X"

    # Print the dungeon
    print_dungeon(dungeon)
    if link.position == link.exit_pos:
        print("Chegou ao fim!")


def move_monster(lines: int, columns: int, monsters: list):
    """ Move the monsters correctly

    Returns:
    lines    -- the number of lines of the matrix
    columns  -- the number of columns of the matrix
    monsters -- the list of monsters
    """

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


def take_item(items: list, link: tuple):
    """ Take the items

    Parameters:
    items -- the list of items
    link  -- the position of link
    """

    for item in items.copy():
        # Check if the Link's position is the same as item's
        if link.position == item.position:
            print(f"[{item.symbol}]Personagem adquiriu o objeto {item.name}" +
                  f" com status de {item.status}")
            # Check the item's symbol (v or d) and add the status to
            # link's life or attack
            if item.symbol == "v":
                link.life += item.status
                link.life = link.life if link.life > 0 else 0
            elif item.symbol == "d":
                link.attack += item.status
                link.attack = link.attack if link.attack >= 1 else 1
            # Remove the item from the list of items
            items.remove(item)


def combat(monsters: list, link: tuple):
    """ Take the items

    Parameters:
    items -- the list of items
    link  -- the position of link
    """

    if link.position != link.exit_pos:
        # Check if the Link's position is the same as monster's
        for monster in monsters:
            if link.position == monster.position and link.life > 0:
                # Attack the monster
                monster.life -= link.attack
                # Checks if the monster is alive
                if monster.life <= 0:
                    print(f"O Personagem deu {link.attack + monster.life} de" +
                          f" dano ao monstro na posicao {link.position}")
                    # if not, remove it from the list of monsters
                    monsters.remove(monster)
                else:
                    # if so, attacks link
                    damage_taken = monster.attack if link.life - \
                        monster.attack >= 0 else link.life
                    link.life -= monster.attack
                    link.life = link.life if link.life > 0 else 0
                    print(f"O Personagem deu {link.attack} de dano" +
                          f" ao monstro na posicao {link.position}")
                    print(f"O Monstro deu {damage_taken} de dano ao" +
                          f" Personagem. Vida restante = {link.life}")


def move_link(lines: int, columns: int, position: tuple,
              monsters: list, items: list, link: tuple):
    """ Move link within the dungeon

    Parameters:
    lines    -- the number of lines of the matrix
    columns  -- the number of columns of the matrix
    i, j     -- the current position of link
    monsters -- the list of monsters
    items    -- the list of items
    link     -- the character
    """

    take_item(items, link)  # First take the items
    combat(monsters, link)  # Them combat the monster
    dungeon_maker(lines, columns, monsters, items, link)  # Make the dungeon
    if link.position != link.exit_pos:
        link.position = position  # Move link
    move_monster(lines, columns, monsters)  # Move the monsters


def run_game(lines, columns, monsters, items, link, first_move=True):
    """ Run the game

    Parameters:
    lines      -- the number of lines of the matrix
    columns    -- the number of columns of the matrix
    monsters   -- the list of monsters
    items      -- the list of items
    link       -- the character
    first_move -- checks if it's the character's first move
    """

    i, j = link.position

    while link.condition():
        if first_move:
            first_move = False  # It is no longer the first move
            # Make link go down
            while i < lines - 1 and link.condition():
                i += 1
                move_link(lines, columns, (i, j), monsters, items, link)
        else:
            while i >= 0 and link.life != 0:
                # The direction of the movement
                # (left to right or vice versa)
                direction = int((-1)**(i - 1))
                # Make the character to move in the direction
                while columns > j + direction >= 0 and link.condition():
                    j += direction
                    move_link(lines, columns, (i, j), monsters, items, link)
                i -= 1  # Make link go up
                move_link(lines, columns, (i, j), monsters, items, link)


def main():
    """ The main function of the code"""

    link = (lambda data:  # the link's data (life and attack)
            Character(data[0], data[1]))(data_extractor(input()))

    # The number of lines and columns of the matrix (dungeon)
    lines, columns = data_extractor(input())
    link.position = data_extractor(input())  # Define link's initial position
    link.exit_pos = data_extractor(input())  # Define the position of the exit

    monsters = [Monster(*(lambda data:  # the monster's data
                                        # (life, attack, symbol and position)
                          [int(d) for d in data[:2]] +
                          [data[2]] +
                          [data_extractor(data[3])])(input().split()))
                for i in range(int(input()))]

    items = [Item(*(lambda data:  # the item's data
                                  # (life, attack, symbol, position)

                    data[:2] +
                    [data_extractor(data[2])] +
                    [int(data[3])])(input().split()))
             for i in range(int(input()))]

    # Run the game
    run_game(lines, columns, monsters, items, link)


if __name__ == "__main__":
    main()
