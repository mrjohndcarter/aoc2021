from functools import reduce
import unittest


def digify(data: str) -> list:
    return [int(x) for x in data]


def sum_places_for_list_of_strings(data: list) -> list:
    pass


def sum_places_for_lists(a: list, b: list) -> list:
    return [x + y for (x, y) in zip(a, b)]


def get_zeroed_list_for_size(size: int) -> list:
    return [0 for x in range(size)]


# list of pairs of (0, 1) counts
def deduce_ones_and_zeros(sum_places: list, size_of_input_list: int) -> list:
    return [(size_of_input_list - count, count) for count in sum_places]


def select_zero_or_one_most(count_pairs: list) -> list:
    return [0 if count[0] > count[1] else 1 for count in count_pairs]


def select_zero_or_one_least(count_pairs: list) -> list:
    return [0 if count[0] <= count[1] else 1 for count in count_pairs]


def get_integer_from_binary_list(binary_number_list: list) -> list:
    result = 0
    for place in binary_number_list:
        result = (result << 1) | place
    return result


def main():
    input_data = None;

    with open('input.p1', 'r') as f:
        input_data = [digify(x.strip()) for x in f]

    summed = reduce(sum_places_for_lists, input_data, get_zeroed_list_for_size(len(input_data[0])))
    deduced = deduce_ones_and_zeros(summed, len(input_data))

    gamma = get_integer_from_binary_list(select_zero_or_one_most(deduced))
    epsilon = get_integer_from_binary_list(select_zero_or_one_least(deduced))

    print(f'{gamma} * {epsilon} = {gamma * epsilon}')


if __name__ == '__main__':
    main()


class Tests(unittest.TestCase):

    def test_zero(self):
        self.assertEqual([0, 0, 0, 0, 0], get_zeroed_list_for_size(5))

    def test_sum_places_for_lists(self):
        self.assertEqual([1, 2, 1], sum_places_for_lists([1, 1, 1], [0, 1, 0]))

    def test_digify(self):
        self.assertEqual([1, 0, 1], digify("101"))

    def test_sum_places(self):
        self.assertEqual([1, 1, 1, 1, 0], sum_places_for_list_of_strings(["11110"]))

    def test_binary_conversion(self):
        self.assertEqual(39, get_integer_from_binary_list([1, 0, 0, 1, 1, 1]))
