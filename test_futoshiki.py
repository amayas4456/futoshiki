from futoshiki import Futoshiki

def test_solve():
    table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    expected = [[2, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2]]
    assert puzzle.solve() == expected

def test_no_solution():
    table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 'lt', 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)
    assert puzzle.solve() == False

def test_no_solution_verbose(capsys):
    # https://docs.pytest.org/en/latest/capture.html#accessing-captured-output-from-a-test-function
    table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 'lt', 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)
    puzzle.solve(verbose=True)
    captured = capsys.readouterr()
    assert captured.out.rstrip() == 'No solution :('

def test_find_next_empty():
    table = [[2, 3, 4, 1], [1, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)
    
    expected = (1,2)
    assert puzzle.find_next_empty() == expected

def test_puzzle_full():
    table = [[2, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.find_next_empty() == False

def test_fits_in_col():
    table = [[2, 3, 4, 1], [1, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.fits_in_col(3, 0) == True

def test_not_fits_in_col():
    table = [[2, 3, 4, 1], [1, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.fits_in_col(1, 0) == False

def test_fits_in_row():
    table = [[2, 3, 4, 1], [1, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.fits_in_row(4, 1) == True

def test_not_fits_in_row():
    table = [[2, 3, 4, 1], [1, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.fits_in_row(2, 1) == False

def test_satisfies_constraints():
    table = [[2, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 0, 2]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.satisfies_constraints(1, 3, 2) == True

def test_satisfies_constraints2():
    table = [[2, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 0], [3, 4, 1, 2]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.satisfies_constraints(3, 2, 3) == True

def test_not_satisfies_constraints():
    table = [[2, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 0], [3, 4, 1, 2]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.satisfies_constraints(1, 2, 3) == False

def test_not_satisfies_constraints2():
    table = [[0, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2]]
    row_constraints = [['gt', 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.satisfies_constraints(2, 0, 0) == False

def test_not_satisfies_constraints3():
    table = [[2, 3, 3, 0], [1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2]]
    row_constraints = [[0, 'lt', 'gt'], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.satisfies_constraints(4, 0, 3) == False

def test_not_satisfies_constraints4():
    table = [[0, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2]]
    row_constraints = [[0, 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [['lt', 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.satisfies_constraints(4, 0, 0) == False

def test_not_satisfies_constraints5():
    table = [[0, 3, 4, 1], [1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2]]
    row_constraints = [['lt', 'lt', 0], [0, 0, 0], [0, 'lt', 0], [0, 0, 'lt']]
    col_constraints = [[0, 'gt', 0, 0], ['lt', 0, 0, 0], [0, 0, 0, 'gt']]

    puzzle = Futoshiki(table, row_constraints, col_constraints)

    assert puzzle.satisfies_constraints(4, 0, 0) == False
