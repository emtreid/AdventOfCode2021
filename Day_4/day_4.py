class Board():

    def __init__(self, rows, numbers):
        self.rows = [x.replace("  ", " ").strip().split(" ") for x in rows]
        self.lines = self.find_lines()
        self.time = self.find_time(numbers)

    def find_line_time(self, numbers, line):
            return max([numbers.index(int(x)) for x in line])
    
    def find_lines(self):
        lines = self.rows.copy()
        for i in range(5):
            lines.append([self.rows[j][i] for j in range(5)])
        return lines
    
    def find_time(self, numbers):
        return min([self.find_line_time(numbers, x) for x in self.lines])

    def sum_unmarked(self, numbers, i):
        board_numbers = [int(x) for l in self.rows for x in l]
        numbers_called = numbers[0:i+1]
        return sum([x for x in board_numbers if not x in numbers_called])


if __name__ == "__main__":

    with open('input.txt') as f:
        data = f.read().splitlines()

    numbers = [int(x) for x in data[0].split(",")]

    print(numbers)

    del(data[0])

    n_boards = data.count("")

    boards_input = [data[6*i+1:6*i+6] for i in range(n_boards)]

    boards = [Board(x, numbers) for x in boards_input]

    board_times = [x.time for x in boards]

    win_time = min(board_times)
    winner = boards[board_times.index(win_time)]
    
    lose_time = max(board_times)
    loser = boards[board_times.index(lose_time)]

    print("PART 1:")
    print(numbers[win_time]*winner.sum_unmarked(numbers, win_time))

    print("PART 2:")
    print(numbers[lose_time]*loser.sum_unmarked(numbers, lose_time))

