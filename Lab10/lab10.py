import math


def character_definer() -> (int, dict, dict):
    """ Define the character

    Returns:
    int  -- the life of the character
    dict -- the arrows in the format {arrow: quantity}
    dict -- the character in the format {"life": int
                                         "arrows": dict}
    """

    arrows = {}
    life, arrows_info = int(input()), input().split()
    types, quantities = arrows_info[0::2], map(int, arrows_info[1::2])

    arrows = {arrow: quant for arrow, quant in zip(types, quantities)}

    return life, arrows, {"life": life,
                          "arrows": arrows}


def monster_generator(monsters: list) -> list:
    """ Generate the monsters and append them to a list

    Parameters:
    monsters -- the empty list of monsters

    Returns:
    list    -- append the monsters list with the new monsters, the monsters are
               dictionaries in the format:
               {"life": int
                "attack": int
                "parts": dict}
               the parts are dictionaries in the format:
               {"name": {"weakness": str
                         "max_damage": int
                         "coordinates": (int, int)
                         "critics": int}}
    """

    parts = {}
    life, attack, num_parts = map(int, input().split())

    for i in range(num_parts):
        name, weakness, max_damage, x, y = input().split(", ")
        parts[name] = {"weakness": weakness,
                       "max_damage": int(max_damage),
                       "coordinates": (int(x), int(y)),
                       "critics": 0}

    monster = {"life": life,
               "attack": attack,
               "parts": parts}

    return monsters.append(monster)


def part_finder(monsters: list, position: int, target: str) -> (str,
                                                                tuple, int):
    """ Get the information about some part

    Parameters:
    monsters -- the list of monsters
    position -- the position of the monster in the monsters list
    target   -- the part of the monster that will be target

    Returns:
    str      -- the name of the weakness
    tuple    -- the critical coordinates of the part
    int      -- the max damage that can be given in that part
    """

    part_info = monsters[int(position)]["parts"][target]

    return part_info["weakness"], part_info["coordinates"],\
        int(part_info["max_damage"])


def damage_calculator(max_damage: int, part_weakness: str, arrow_type: str,
                      cx: int, cy: int, fx: int, fy: int) -> int:
    """ Calculate the damage that the monster will receive

    Parameters:
    max_damage    -- the max damage that can be given in this part
    part_weakness -- the name of the weakness of this part
    arrow_type    -- the type of the arrow
    cx            -- the x axis of the critical coordinate
    cy            -- the y axis of the critical coordinate
    fx            -- the x axis of the arrow
    fy            -- the y axis of the arrow

    Returns:
    int           -- the damage the monsters will receive
    """

    x_difference = abs(cx - fx)
    y_difference = abs(cy - fy)
    damage = max_damage - (x_difference + y_difference)
    damage = damage if damage > 0 else 0
    if part_weakness in ["todas", arrow_type]:
        return damage
    else:
        return damage//2


def healer(aloy: dict, max_life: int) -> int:
    """ Heal character

    Parameters:
    aloy     -- the character that will be healed
    max_life -- the max life that the character can have

    Returns:
    int      -- the new life of the character
    """

    if aloy["life"] > 0:
        if aloy["life"] + math.floor(0.5*max_life) >= max_life:
            return max_life
        else:
            return aloy["life"] + math.floor(0.5*max_life)


def combat(monsters, combat_quant, aloy, total_arrows) -> (list, int):
    """ Make the character confront a monster

    Parameters:
    monster      -- the monster that will be confronted
    combat_quant -- quantity of monster that the character will confront
    aloy         -- the character
    total_arrows -- the total of arrows the character have in the beginning
                    of the confront

    Returns:
    list         -- list of the positions of the dead monsters
    int          -- the total of arrows the character have in the end of the
                    confront
    """

    fired_arrows, dead_monsters, alive_monsters = 0, [], monsters.copy()
    while combat_quant > 0 and aloy["life"] > 0:
        position, target, arrow_type, fx, fy = input().split(", ")
        monster = monsters[int(position)]

        part_weakness, (cx, cy), max_damage =\
            part_finder(monsters, int(position), target)

        monster["life"] -= damage_calculator(max_damage, part_weakness,
                                             arrow_type, int(cx), int(cy),
                                             int(fx), int(fy))

        if (int(cx), int(cy)) == (int(fx), int(fy)):
            monster["parts"][target]["critics"] += 1

        if monster["life"] <= 0:
            dead_monsters.append(int(position))
            alive_monsters.remove(monster)

        aloy["arrows"][arrow_type] -= 1

        fired_arrows += 1
        if fired_arrows % 3 == 0:
            for i in range(len(alive_monsters)):
                if aloy["life"] > alive_monsters[i]["attack"]:
                    aloy["life"] -= alive_monsters[i]["attack"]
                else:
                    aloy["life"] = 0

        total_arrows -= 1
        if total_arrows == 0 or combat_quant == len(dead_monsters):
            break

    return dead_monsters, total_arrows


def main():
    """The main function of the code"""

    max_life, original_arrows, aloy = character_definer()
    monster_quant = int(input())
    combat_number = 0

    while monster_quant > 0:
        monsters, total_arrows = [], 0

        aloy = {"life": healer(aloy, max_life),
                "arrows": original_arrows.copy()}

        for quantity in aloy["arrows"].values():
            total_arrows += quantity

        combat_quant = int(input())
        monster_quant -= combat_quant

        print(f"Combate {combat_number}, vida = {aloy['life']}")

        for i in range(combat_quant):
            monster_generator(monsters)
        dead_monsters, total_arrows = combat(monsters, combat_quant, aloy,
                                             total_arrows)
        for i in range(len(dead_monsters)):
            print(f"Máquina {dead_monsters[i]} derrotada")

        print(f"Vida após o combate = {aloy['life']}")

        if aloy["life"] <= 0 or total_arrows == 0:
            break

        print("Flechas utilizadas:")

        for arrow, quantity in aloy["arrows"].items():
            if quantity != original_arrows[arrow]:
                print(f"- {arrow}: {original_arrows[arrow] - quantity}/"
                      f"{original_arrows[arrow]}")

        already_critted = False
        first_appearence = -1
        dead_monsters.sort()
        for i in dead_monsters:
            if first_appearence != i:
                first_appearence = i
            dead_monster = monsters[i]["parts"]
            for monsters_part, part_info in dead_monster.items():
                if part_info["critics"] != 0:
                    if already_critted is False:
                        print("Críticos acertados:")
                        already_critted = True
                    if first_appearence == i:
                        print(f"Máquina {i}:")
                        first_appearence = -1
                    print(f"- {part_info['coordinates']}: "
                          f"{part_info['critics']}x")

        combat_number += 1

    if total_arrows != 0:
        if aloy["life"] <= 0:
            print("Aloy foi derrotada em combate e não retornará a tribo.")
        else:
            print("Aloy provou seu valor e voltou para sua tribo.")
    else:
        print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")


if __name__ == "__main__":
    main()
