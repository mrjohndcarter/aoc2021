from functools import reduce
import unittest

from p1 import digify, select_zero_or_one_most, sum_places_for_lists, get_zeroed_list_for_size, deduce_ones_and_zeros, \
    get_integer_from_binary_list, select_zero_or_one_least


def filter_list_for_value_at_index(data: list, value: int, place: int) -> list:
    return [number_array for number_array in data if number_array[place] == value]


def main():
    input_data = None

    with open('input.p1', 'r') as f:
        input_data = [digify(x.strip()) for x in f]

    filtered_list = input_data
    for i in range(len(filtered_list[0])):
        summed = reduce(sum_places_for_lists, filtered_list, get_zeroed_list_for_size(len(filtered_list[0])))
        deduced = deduce_ones_and_zeros(summed, len(filtered_list))
        most_common = select_zero_or_one_most(deduced)
        filtered_list = filter_list_for_value_at_index(filtered_list, most_common[i], i)
        if len(filtered_list) == 1:
            break

    oxygen_generator_rating = get_integer_from_binary_list(filtered_list[0])

    filtered_list = input_data
    for i in range(len(filtered_list[0])):
        summed = reduce(sum_places_for_lists, filtered_list, get_zeroed_list_for_size(len(filtered_list[0])))
        deduced = deduce_ones_and_zeros(summed, len(filtered_list))
        most_common = select_zero_or_one_least(deduced)
        filtered_list = filter_list_for_value_at_index(filtered_list, most_common[i], i)
        if len(filtered_list) == 1:
            break

    co2_scrubber_rating = get_integer_from_binary_list(filtered_list[0])

    print(f'{oxygen_generator_rating} * {co2_scrubber_rating} = {oxygen_generator_rating * co2_scrubber_rating}')


if __name__ == '__main__':
    main()


class Tests(unittest.TestCase):

    def test_zero(self):
        self.assertEqual([0, 0, 0, 0, 0], get_zeroed_list_for_size(5))

    def test_sum_places_for_lists(self):
        self.assertEqual([1, 2, 1], sum_places_for_lists([1, 1, 1], [0, 1, 0]))

    def test_digify(self):
        self.assertEqual([1, 0, 1], digify("101"))

    def test_binary_conversion(self):
        self.assertEqual(39, get_integer_from_binary_list([1, 0, 0, 1, 1, 1]))
