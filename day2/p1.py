import unittest


def direction_magnitude(line: str) -> tuple:
    return line.split(' ')[0], int(line.split(' ')[1])


def main():
    input_data = None;

    with open('input.p1', 'r') as f:
        input_data = [direction_magnitude(x) for x in f]

    horizontal_pos = 0
    vertical_pos = 0

    for pair in input_data:

        if pair[0] == 'forward':
            horizontal_pos += pair[1]

        elif pair[0] == 'down':
            vertical_pos += pair[1]

        elif pair[0] == 'up':
            vertical_pos -= pair[1]

        else:
            print('error -- bad input')

    print(f'horizontal * vertical = {horizontal_pos * vertical_pos}')


if __name__ == '__main__':
    main()


class Tests(unittest.TestCase):

    def test_split(self):
        self.assertEqual(('forward', 5), direction_magnitude('forward 5'))
