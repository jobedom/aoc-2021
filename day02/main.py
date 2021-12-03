from read_data import read_lines_from_file, set_folder

set_folder("day02")


def get_instructions_from_file(filename):
    instructions = [line.split(" ") for line in read_lines_from_file(filename)]
    return [(instruction, int(amount)) for [instruction, amount] in instructions]


def part1(filename):
    depth = 0
    position = 0

    for instruction in get_instructions_from_file(filename):
        match instruction:
            case ["forward", n]:
                position += n
            case ["up", n]:
                depth -= n
            case ["down", n]:
                depth += n
    return depth * position


def part2(filename):
    depth = 0
    position = 0
    aim = 0

    for instruction in get_instructions_from_file(filename):
        match instruction:
            case ["forward", n]:
                position += n
                depth += n * aim
            case ["up", n]:
                aim -= n
            case ["down", n]:
                aim += n
    return depth * position


assert part1("test.txt") == 150
assert part2("test.txt") == 900

print("Part 1:", part1("input.txt"))
print("Part 2:", part2("input.txt"))
