def shape(m):
    assert m, "map must be not empty"
    return len(m), len(m[0])


def printer(ch, curr, max_index):
    if curr == max_index - 1:
        print(ch)
    else:
        print(ch, end='')


def print_map(m, pos):
    height = len(m)
    length = len(m[0])
    assert pos[0] <= height - 1 and pos[1] <= length - 1, "Indiana Jones left the world"
    for row in range(height):
        for col in range(length):
            if (row, col) == pos:
                printer('@', col, length)
            elif m[row][col] is False:
                printer('#', col, length)
            else:
                printer('.', col, length)


def neighbours(m, pos):
    result = []
    height = len(m)
    length = len(m[0])
    assert pos[0] < height and pos[1] < length, "off-map position"
    if pos[0] < height - 1 and m[pos[0] + 1][pos[1]]:
        result.append((pos[0] + 1, pos[1]))
    if pos[0] > 0 and m[pos[0] - 1][pos[1]]:
        result.append((pos[0] - 1, pos[1]))
    if pos[1] < length - 1 and m[pos[0]][pos[1] + 1]:
        result.append((pos[0], pos[1] + 1))
    if pos[1] > 0 and m[pos[0]][pos[1] - 1]:
        result.append((pos[0], pos[1] - 1))
    # print(result)
    return result


def neighbours_without_labeled(m, dm, pos):
    result = []
    height = len(m)
    length = len(m[0])
    assert pos[0] < height and pos[1] < length, "off-map position"
    if pos[0] < height - 1 and m[pos[0] + 1][pos[1]] and not dm[pos[0] + 1][pos[1]]:
        result.append((pos[0] + 1, pos[1]))

    if pos[0] > 0 and m[pos[0] - 1][pos[1]] and not dm[pos[0] - 1][pos[1]]:
        result.append((pos[0] - 1, pos[1]))

    if pos[1] < length - 1 and m[pos[0]][pos[1] + 1] and not dm[pos[0]][pos[1] + 1]:
        result.append((pos[0], pos[1] + 1))

    if pos[1] > 0 and m[pos[0]][pos[1] - 1] and not dm[pos[0]][pos[1] - 1]:
        result.append((pos[0], pos[1] - 1))

    # print(result)
    return result


def find_next_pos(dm, pos):
    height = len(dm)
    length = len(dm[0])
    current = dm[pos[0]][pos[1]]
    if pos[0] < height - 1 and dm[pos[0] + 1][pos[1]] + 1 == current:
        return pos[0] + 1, pos[1]

    if pos[0] > 0 and dm[pos[0] - 1][pos[1]] + 1 == current:
        return pos[0] - 1, pos[1]

    if pos[1] < length - 1 and dm[pos[0]][pos[1] + 1] + 1 == current:
        return pos[0], pos[1] + 1

    if pos[1] > 0 and dm[pos[0]][pos[1] - 1] + 1 == current:
        return pos[0], pos[1] - 1


def create_route(dm, start, finish):
    result = []
    pos = finish
    while pos != start:
        result.append(pos)
        pos = find_next_pos(dm, pos)
    result.append(start)
    return result[::-1]


def find_route(m, initial):
    map_size = shape(m)
    distance_map = [[0] * map_size[0] for _ in range(map_size[0])]
    label = 1
    distance_map[initial[0]][initial[1]] = label
    current_neighbours = neighbours_without_labeled(m, distance_map, initial)
    while len(current_neighbours) != 0:
        label += 1
        next_neighbours = []
        for neighbour in current_neighbours:
            distance_map[neighbour[0]][neighbour[1]] = label
            if neighbour[0] == 0 or neighbour[0] == map_size[0] - 1 or neighbour[1] == 0 \
                    or neighbour[1] == map_size[1] - 1:
                route = create_route(distance_map, initial, neighbour)
                # print(route)
                return route
            next_neighbours.extend(neighbours_without_labeled(m, distance_map, neighbour))
        current_neighbours = next_neighbours


def escape(m, initial):
    route = find_route(m, initial)
    for element in route:
        print_map(m, element)
        print()


def main():
    m = [[False, False, False, False],
         [False, True, False, True],
         [False, True, True, False],
         [False, False, True, False],
         [False, True, True, False],
         [False, True, False, True]]
    # print_map(m, (2, 1))
    # neighbours(m, (2, 1))
    # find_route(m, (1, 1))
    escape(m, (1, 1))


if __name__ == '__main__':
    main()
