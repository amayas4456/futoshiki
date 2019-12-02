class Futoshiki():

    def __init__(self, matrix, row_constraints, col_constraints):
        self.matrix = matrix
        self.rconst = row_constraints
        self.cconst = col_constraints
        self.size = len(matrix[0])

    def satisfies_constraints(self, value, row_num, col_num):
        # Constraints in the row
        if col_num > 0:
            if (self.rconst[row_num][col_num-1] == 'gt' and
                self.matrix[row_num][col_num-1] != 0 and
                self.matrix[row_num][col_num-1] < value):
                return False
            elif (self.rconst[row_num][col_num-1] == 'lt' and
                self.matrix[row_num][col_num-1] != 0 and
                self.matrix[row_num][col_num-1] > value):
                return False
        if col_num < self.size - 1:
            if (self.rconst[row_num][col_num] == 'gt' and
                self.matrix[row_num][col_num+1] != 0 and
                value < self.matrix[row_num][col_num+1]):
                return False
            elif (self.rconst[row_num][col_num] == 'lt' and
                self.matrix[row_num][col_num+1] != 0 and
                value > self.matrix[row_num][col_num+1]):
                return False

        # Constraints in the col
        if row_num > 0:
            if (self.cconst[row_num-1][col_num] == 'gt' and
                self.matrix[row_num-1][col_num] != 0 and
                self.matrix[row_num-1][col_num] < value):
                return False
            if (self.cconst[row_num-1][col_num] == 'lt' and
                self.matrix[row_num-1][col_num] != 0 and
                self.matrix[row_num-1][col_num] > value):
                return False
        if row_num < self.size - 1:
            if (self.cconst[row_num][col_num] == 'gt' and
                self.matrix[row_num+1][col_num] != 0 and
                value < self.matrix[row_num+1][col_num]):
                return False
            if (self.cconst[row_num][col_num] == 'lt' and
                self.matrix[row_num+1][col_num] != 0 and
                value > self.matrix[row_num+1][col_num]):
                return False
        return True

    def fits_in_row(self, value, row_num):
        for i in self.matrix[row_num]:
            if i == value:
                return False
        return True

    def fits_in_col(self, value, col_num):
        for i in range(self.size):
            if self.matrix[i][col_num] == value:
                return False
        return True

    def find_next_empty(self):
        for row_num in range(self.size):
            for col_num in range(self.size):
                if not self.matrix[row_num][col_num]:
                    return(row_num, col_num)
        return False

    def solve(self, verbose=False):
        if not self.solving():
            if verbose:
                print('No solution :(')
            return False
        else:
            if verbose:
                print(self.matrix)
            return self.matrix

    def solving(self):
        cell = self.find_next_empty()
        if not cell:
            return True

        for candidate_num in range(1, self.size + 1):
            if (self.fits_in_row(candidate_num, cell[0]) and
                self.fits_in_col(candidate_num, cell[1]) and
                self.satisfies_constraints(candidate_num, cell[0], cell[1])):

                self.matrix[cell[0]][cell[1]] = candidate_num
                if self.solving():
                    return True
                self.matrix[cell[0]][cell[1]] = 0
        return False

def main():

    table = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    row_constraints = [
        [0, 'lt', 0],
        [0, 0, 0],
        [0, 'lt', 0],
        [0, 0, 'lt']
    ]

    col_constraints = [
        [0, 'gt', 0, 0],
        ['lt', 0, 0, 0],
        [0, 0, 0, 'gt']
    ]

    puzzle = Futoshiki(table, row_constraints, col_constraints)
    puzzle.solve(verbose=True)

if __name__ == '__main__':
    main()
