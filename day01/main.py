from read_data import read_number_from_file, set_folder

set_folder("day01")


def calculate_increases_count(numbers):
    return sum([1 if numbers[i + 1] > numbers[i] else 0 for i in range(0, len(numbers) - 1)])


def part1(filename):
    numbers = read_number_from_file(filename)
    return calculate_increases_count(numbers)


def part2(filename):
    numbers = read_number_from_file(filename)
    windows = [sum(numbers[index : index + 2]) for index in range(0, len(numbers) - 2)]
    return calculate_increases_count(windows)


assert part1("test.txt") == 7
assert part2("test.txt") == 5

print("Part 1:", part1("input.txt"))
print("Part 2:", part2("input.txt"))
