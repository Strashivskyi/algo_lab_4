from collections import defaultdict
from typing import List

INPUT_FILE_NAME = "ijones.in"
OUTPUT_FILE_NAME = "ijones.out"


def read_input_data():
    with open(INPUT_FILE_NAME, "r") as input_file:
        width, height = [int(number) for number in input_file.readline().split()]
        corridor = [[letter for letter in row] for row in input_file.readlines()]
    return corridor, width, height


def write_output_data(ways: int):
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        output_file.write(str(ways))


def find_ways(corridor: List[List[int]], width: int, height: int) -> int:
    ways_number_for_tile = [[0 for tile in range(width)] for row in range(height)]
    ways_number_for_letter = defaultdict(int)
    for row in range(height):
        tile_letter = corridor[row][0]
        ways_number_for_tile[row][0] = 1
        ways_number_for_letter[tile_letter] += 1

    for col in range(1, width):
        letter_ways_number_for_current_column = defaultdict(int)
        previous_column = col - 1
        for row in range(height):
            tile_letter = corridor[row][col]
            ways = ways_number_for_letter[tile_letter]
            if tile_letter != corridor[row][previous_column]:
                ways += ways_number_for_tile[row][previous_column]
            ways_number_for_tile[row][col] = ways
            letter_ways_number_for_current_column[tile_letter] += ways
        update_letter_ways(letter_ways_number_for_current_column, ways_number_for_letter)
    if height == 1:
        return ways_number_for_tile[0][width - 1]
    else:
        return ways_number_for_tile[0][width - 1] + ways_number_for_tile[height - 1][width - 1]


def update_letter_ways(letter_ways_number_for_current_column: defaultdict, ways_number_for_letter: defaultdict) -> None:
    for tile_letter in letter_ways_number_for_current_column:
        ways_number_for_letter[tile_letter] += letter_ways_number_for_current_column[tile_letter]


if __name__ == "__main__":
    corridor, width, height = read_input_data()
    successful_ways_number = find_ways(corridor, width, height)
    write_output_data(successful_ways_number)
