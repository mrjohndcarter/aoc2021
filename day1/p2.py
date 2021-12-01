import unittest

from p1 import count_increases_for_array


def get_tuples_from_array(data: list) -> list:
    return [(data[i], data[i + 1], data[i + 2]) for i in range(0, len(data) - 2)]


def main():
    input_data = None;

    with open('input.p1', 'r') as f:
        input_data = [int(x) for x in f]

    print(f'{count_increases_for_array(list(map(lambda x: sum(x), get_tuples_from_array(input_data))))}')


if __name__ == '__main__':
    main()


class TestIncreaseCount(unittest.TestCase):

    def test_a(self):
        self.assertEqual([(1, 2, 3)], get_tuples_from_array([1, 2, 3]))

    def test_b(self):
        self.assertEqual([(1, 2, 3), (2, 3, 4)], get_tuples_from_array([1, 2, 3, 4]))

    def test_sample(self):
        self.assertEqual([(199, 200, 207)],
                         count_increases_for_array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
