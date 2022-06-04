from collections import deque


def shape(m):
    assert m, "map must be not empty"
    return len(m), len(m[0])


def print_map(m, pos):
    height, length = shape(m)
    assert pos[0] <= height - 1 and pos[1] <= length - 1, "Indiana Jones left the world"
    for row in range(height):
        for col in range(length):
            if (row, col) == pos:
                ch = "@"
            elif not m[row][col]:
                ch = "#"
            else:
                ch = "."
            print(ch, end="")
        print()


def find_next_pos(dm, pos):
    height, length = shape(dm)
    x, y = pos
    current = dm[x][y]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        point = (x + dx, y + dy)
        inside_map = 0 <= point[0] < height and 0 <= point[1] < length
        if inside_map:
            not_none = not dm[point[0]][point[1]] is None
            if not_none and dm[point[0]][point[1]] + 1 == current:
                return point


def create_route(dm, start, finish):
    result = []
    pos = finish
    while pos != start:
        result.append(pos)
        pos = find_next_pos(dm, pos)
    result.append(start)
    return result[::-1]


def find_neighbours(m, dm, pos, size):
    x, y = pos
    result = []
    height, length = size
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        point = (x + dx, y + dy)
        inside_map = 0 <= point[0] < height and 0 <= point[1] < length
        not_wall = m[point[0]][point[1]]
        is_null = dm[point[0]][point[1]] == 0
        if inside_map and not_wall and is_null:
            result.append(point)
    return result


def find_route(m, initial):
    size = shape(m)
    height, length = size
    assert 0 <= initial[0] < height and 0 <= initial[1] < length, "off-map position"
    distance_map = [[0] * length for _ in range(height)]
    label = 1
    distance_map[initial[0]][initial[1]] = label
    current_neighbours = deque(find_neighbours(m, distance_map, initial, size))
    while current_neighbours:
        next_neighbours = deque()
        label += 1
        for x, y in current_neighbours:
            if distance_map[x][y] == 0:
                distance_map[x][y] = label
            if (x == 0 or x == height - 1
                    or y == 0 or y == length - 1):
                return create_route(distance_map, initial, (x, y))
            next_neighbours.extend(find_neighbours(m, distance_map, (x, y), size))
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
    escape(m, (1, 1))


if __name__ == '__main__':
    main()
