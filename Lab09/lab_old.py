def print_area(area: list[list[str]]):
    """Print the matrix in the correct way
    (very specific way)

    Parameters:
    area    --  the matrix that will be printed
    """

    for line in area:
        print(" ".join(line))


def clean(current: tuple, area: list[list[str]]) -> tuple:
    """Research for trash in the area

    Parameters:
    current -- the current position of the robot
    area    --  the matrix that will be printed

    Return:
    tuple   -- the new current position of the robot
    """

    i, j = current
    positions = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]

    for trash in positions:
        if (trash[0] < 0 or trash[1] < 0) or (trash[0] >= len(area) or trash[1]
                                              >= len(area[0])):
            continue

        elif area[trash[0]][trash[1]] == 'o':
            area[i][j] = '.'
            area[trash[0]][trash[1]] = 'r'
            print()
            print_area(area)
            return clean((trash[0], trash[1]), area)

    return current


def go_back(current, origin, area):
    if origin[1] > current[1]:
        for i in range(current[1], origin[1]+1):
            current = (current[0], i)
            go_back(clean(current, area), origin, area)
    elif origin[1] < current[1]:
        for i in range(current[1], origin[1]+1, -1):
            current = (current[0], i)
            go_back(clean(current, area), origin, area)

    if origin[0] > current[0]:
        for i in range(current[0], origin[0]+1):
            current = (i, current[1])
            go_back(clean(current, area), origin, area)
    elif origin[0] < current[0]:
        for i in range(current[0], origin[0]+1, -1):
            current = (i, current[1])
            go_back(clean(current, area), origin, area)

    return current


def main():
    """The main function of the code"""

    n_lines = int(input())
    area = []

    for i in range(n_lines):
        line = input()
        line_list = [elem for elem in line if elem != " "]
        area.append(line_list)

    for i, line in enumerate(area):
        if i % 2:
            r = range(len(line) - 1, -1, -1)
        else:
            r = range(len(line))
        for j in r:
            area[i][j] = "r"
            if i or j:
                print()
            print_area(area)
            (i, j) = go_back(clean((i, j), area), (i, j), area)
            area[i][j] = "."


if __name__ == "__main__":
    main()
