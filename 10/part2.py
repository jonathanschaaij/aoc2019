import math

input_raw = """#.....#...#.........###.#........#..
....#......###..#.#.###....#......##
......#..###.......#.#.#.#..#.......
......#......#.#....#.##....##.#.#.#
...###.#.#.......#..#...............
....##...#..#....##....#...#.#......
..##...#.###.....##....#.#..##.##...
..##....#.#......#.#...#.#...#.#....
.#.##..##......##..#...#.....##...##
.......##.....#.....##..#..#..#.....
..#..#...#......#..##...#.#...#...##
......##.##.#.#.###....#.#..#......#
#..#.#...#.....#...#...####.#..#...#
...##...##.#..#.....####.#....##....
.#....###.#...#....#..#......#......
.##.#.#...#....##......#.....##...##
.....#....###...#.....#....#........
...#...#....##..#.#......#.#.#......
.#..###............#.#..#...####.##.
.#.###..#.....#......#..###....##..#
#......#.#.#.#.#.#...#.#.#....##....
.#.....#.....#...##.#......#.#...#..
...##..###.........##.........#.....
..#.#..#.#...#.....#.....#...###.#..
.#..........#.......#....#..........
...##..#..#...#..#...#......####....
.#..#...##.##..##..###......#.......
.##.....#.......#..#...#..#.......#.
#.#.#..#..##..#..............#....##
..#....##......##.....#...#...##....
.##..##..#.#..#.................####
##.......#..#.#..##..#...#..........
#..##...#.##.#.#.........#..#..#....
.....#...#...#.#......#....#........
....#......###.#..#......##.....#..#
#..#...##.........#.....##.....#...."""

rows = input_raw.split('\n')

length = len(rows)
width = len(rows[-1])

print("length, width:",length,width)

input = []
for row in rows:
    # print(row)
    for char in row:
        input.append(char)
input = ''.join(input)

# print(input)

asteroids = {}
for i in range(1,len(input)+1):
    # print(i,input[i-1])
    if input[i-1] == '#':
        asteroids[i] = 0

# print(asteroids)

best = 0
best_pos = [0,0]

slopes = []
y_tes = (1070)//width
x_tes = (1070) - y_tes*width
# print("X,Y: ",x_tes,y_tes)
for asteroid in asteroids:
    if 1071 == asteroid:
        continue
    y_as = (asteroid-1)//width
    x_as = (asteroid-1) - y_as*width

    d_x = x_as - x_tes
    d_y = y_as - y_tes

    slope = math.atan2(d_x, -d_y)
    if slope in slopes:
        continue
    else:
        asteroids[asteroid]=slope
        slopes.append(slope)

if len(slopes) > best:
    best_pos = [x_tes, y_tes]
    best = len(slopes)

for asteroid in asteroids:
    if asteroids[asteroid] < 0:
        asteroids[asteroid] += 2*math.pi
sorted

n=1
for asteroid, slope in sorted(asteroids.items(), key = lambda kv:(kv[1], kv[0])):
    if slope > 0:
        n+=1
    if n > 198 and n < 202:
        y = (asteroid-1)//width
        x = (asteroid-1) - y*width
        print(n, asteroid, (x,y))
