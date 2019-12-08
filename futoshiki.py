import random
import numpy as np

class Futoshiki():

    def __init__(self, matrix = False, row_constraints = False, col_constraints = False, size=4):
        if not matrix:
            self.matrix, self.rconst, self.cconst = self.init_empty_matrix(size)
        else:
            self.matrix = matrix
            self.rconst = row_constraints
            self.cconst = col_constraints
        self.size = len(self.matrix[0])
    
    def init_empty_matrix(self, size):
        matrix = np.zeros((size, size), dtype=np.int8).tolist()
        row_constraints = np.zeros((size, size-1), dtype=np.int8).tolist()
        col_constraints = np.zeros((size-1, size), dtype=np.int8).tolist()
        return (matrix, row_constraints, col_constraints)

    def get_matrix(self):
        return self.matrix
    
    def get_row_constraints(self):
        return self.rconst
    
    def get_col_constraints(self):
        return self.cconst

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
    
    def symetric_matrix(self):
        """Constructs a bidimensional matrix interspersing the constrints with the values
        
        Returns:
            bidimensional list -- 2D matrix of len(self.matrix) * 2 - 1 size
        """        
        result = []
        cconst_new = []

        for i in range(len(self.cconst)):
            temp_list = []
            for j in range(len(self.cconst[i])):
                temp_list.append(self.cconst[i][j])
                if j < len(self.cconst[i]) - 1:
                    temp_list.append(0)
            cconst_new.append(temp_list)

        for row in range(len(self.matrix)):
            temp_list = []
            for cell in range(len(self.matrix[row])):
                temp_list.append(self.matrix[row][cell])
                if cell <= len(self.rconst[row]) - 1:
                    temp_list.append(self.rconst[row][cell])
            result.append(temp_list)
            if row <= len(self.cconst) - 1:
                result.append(cconst_new[row])

        return result
    
    def fill_matrix(self):
        # BUG: for some reason, some puzzles don't get solved with backtracking...
        is_filled = False
        while not is_filled:
            # Fill main diagonal with random random numbers
            for i in range(self.size):
                self.matrix[i][i] = random.randint(1, self.size)
            
            # Fill the rest of values
            is_filled = self.solve()

    def fill_constraints(self):
        # Row constraints
        for row in range(len(self.rconst)):
            for col in range(len(self.rconst[row])):
                if self.matrix[row][col] > self.matrix[row][col+1]:
                    self.rconst[row][col] = 'gt'
                else:
                    self.rconst[row][col] = 'lt'
        
        # Col constraints
        for row in range(len(self.cconst)):
            for col in range(len(self.cconst[row])):
                if self.matrix[row][col] > self.matrix[row+1][col]:
                    self.cconst[row][col] = 'gt'
                else:
                    self.cconst[row][col] = 'lt'

    def remove_random_values_in_matrix(self, table, k):
        """Removes the amount of numbers specified in a given matrix
        
        Arguments:
            table {int[][]} -- Reference to the matrix where the values will be removed
            k {int} -- Number of values to remove
        """
        to_remove = k
        while to_remove != 0:
            row = random.randint(0, len(table)-1)
            col = random.randint(0, len(table[0])-1)
            if table[row][col] != 0:
                to_remove = to_remove - 1
                table[row][col] = 0
    
    def remove_random_values(self):
        # TODO: remove proportional amount of values in relation to matrix size
        # TODO: play with this + matrix size to determine difficulty
        self.remove_random_values_in_matrix(self.matrix, k=12)
        self.remove_random_values_in_matrix(self.rconst, k=9)
        self.remove_random_values_in_matrix(self.cconst, k=9)
    
    def create_puzzle(self):
        self.fill_matrix()
        self.fill_constraints()
        self.remove_random_values()
