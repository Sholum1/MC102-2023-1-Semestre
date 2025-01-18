def print_area(area: list[list[str]]):
    """ Print the matrix in the correct way

    Parameters:
    area -- the matrix that will be printed
    """

    for line in area:
        print(" ".join(line))


def move(origin: tuple, destiny: tuple, area: list[list[str]]):
    """ Move the robot and print it

    Parameters:
    origin  -- where the robot is
    destiny -- where the robot will go
    area    -- the matrix that the robot will move through
    """

    i, j = origin
    x, y = destiny
    # Move the robot from origin to destiny
    area[x][y] = "r"
    area[i][j] = "."
    print()
    print_area(area)


def walk(origin: tuple, area: list[list[str]]):
    """ Make the robot walk from the left to the right in even rows and from
    right to left in odd rows, them go down in the edge

    Parameters:
    origin -- where the robot is
    area   -- the matrix that the robot will move through
    """

    # Print the matrix before it being modified
    print_area(area)
    # Verify if there is trash in front of the robot
    # in the initial area and them clean it
    if area[0][1] != "o":
        clear(origin, area)

    # Give the coordinates of the origin to i and j
    i, j = origin

    # Apply i and j
    for i in range(len(area)):
        # Define the direction the robot will move (left = -1 and right = 1)
        direction = (-1)**i
        while len(area[i]) > j + direction >= 0:
            move((i, j),  (i, j + direction), area)
            j += direction
            # Verify if there is trash in front of the robot and them clean it
            if len(area[i]) > j + direction >= 0 and\
               area[i][j + direction] != "o":
                clear((i, j), area)
            # If the robot is in the left side in the last line
            # make it go to the right side
            k = j
            if (i, j) == (len(area) - 1, 0):
                for k in range(len(area[i]) - 1):
                    move((i, k),  (i, k + 1), area)
        # Go down
        if i == len(area) - 1:
            break
        move((i, j), (i + 1, j), area)
        i += 1
        clear((i, j), area)


def scan(origin, area) -> tuple:
    """ Research for dirt in the area

    Parameters:
    current --  the current position of the robot
    area    --  the matrix that will be printed

    Return:
    tuple   -- the new current position of the robot
    """

    # Give the coordinates of the origin to i and j
    i, j = origin
    # Define the positions that will be scanned
    # in the follow order: left, up, right and down
    positions = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]

    # Scan the given position
    for x, y in positions:
        if (x < 0 or y < 0) or (x >= len(area) or y >= len(area[0])):
            continue

        elif area[x][y] == "o":
            return (x, y)
    # Return the position of the dirt
    return (i, j)


def clear(origin, area, where_return=None):
    """ Clean the dirt that the scan found

    Parameters:
    origin       -- the position where the robot found the dirt
    area         -- the matrix that will be cleaned
    where_return -- the position where the first dirt was found
    """

    if where_return is None:
        where_return = origin

    dirt = scan(origin, area)
    current = origin

    while current != dirt:
        move(current, dirt, area)
        current = dirt
        dirt = scan(current, area)
    go_back(current, where_return, area)


def go_back(current, origin, area):
    """ Go back where the dirt was found

    Parameters:
    current      -- the current position of the robot
    origin       -- the position where the robot found the dirt
    area         -- the matrix that will be cleaned
    """

    # Give the current positions coordinates to i and j
    i, j = current
    # Give the origin positions coordinates to x and y
    x, y = origin

    # Go back to the same column
    if y != j:
        direction = 1 if y > j else -1
        move((i, j), (i, j + direction), area)
        j += direction
        clear((i, j), area, origin)

    # Go back to the same line
    elif x != i:
        direction = 1 if x > i else -1
        move((i, j), (i + direction, j), area)
        i += direction
        clear((i, j), area, origin)


def main():
    """The main function of the code"""

    # Define the number of lines and the matrix variables
    n_lines = int(input())
    area = []

    # Give the elements to the matrix
    for i in range(n_lines):
        line = input()
        line_list = [elem for elem in line if elem != " "]
        area.append(line_list)

    # Run the code
    walk((0, 0), area)


if __name__ == "__main__":
    main()
