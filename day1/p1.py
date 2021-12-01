import unittest


def count_increases_for_array(data: list) -> int:
    comparison_tuples = [(data[i - 1], data[i]) for i in range(1, len(data))]
    return len(list(filter(lambda x: x[0] < x[1], comparison_tuples)))


def main():
    input_data = None;

    with open('input.p1', 'r') as f:
        input_data = [int(x) for x in f]

    print(f'{count_increases_for_array(input_data)}')


if __name__ == '__main__':
    main()


class TestIncreaseCount(unittest.TestCase):

    def test_a(self):
        self.assertEqual(2, count_increases_for_array([1, 2, 3]))

    def test_sample(self):
        self.assertEqual(7, count_increases_for_array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
