from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def _add_values(draw, matrix):
    font = ImageFont.truetype('resources/NewYork.ttf', size=150)
    color = (0, 0, 0)
    pos_init = {'x': 75, 'y': 15} # Initial drawing position. Following are increments of +250

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                pos_x = (pos_init.get('x') + (250 * col))
                pos_y = (pos_init.get('y') + (250 * row))
                draw.text((pos_x, pos_y), str(matrix[row][col]), fill=color, font=font)

def _add_row_constraints(canvas, rconst):
    pos_init = {'x': 205, 'y': 55}

    left = Image.open('resources/arrow.png')
    right = left.rotate(180)
    
    for row in range(len(rconst)):
        for col in range(len(rconst[row])):
            if rconst[row][col] != 0:
                pos_x = (pos_init.get('x') + (250 * col))
                pos_y = (pos_init.get('y') + (250 * row))
                if rconst[row][col] == 'gt':
                    canvas.paste(left, (pos_x, pos_y))
                else:
                    canvas.paste(right, (pos_x, pos_y))

def _add_col_constraints(canvas, cconst):
    pos_init = {'x': 60, 'y': 195}

    left = Image.open('resources/arrow.png')
    top = left.rotate(90, expand=True)
    bottom = left.rotate(270, expand=True)

    for row in range(len(cconst)):
        for col in range(len(cconst[row])):
            if cconst[row][col] != 0:
                pos_x = (pos_init.get('x') + (250 * col))
                pos_y = (pos_init.get('y') + (250 * row))
                if cconst[row][col] == 'gt':
                    canvas.paste(bottom, (pos_x, pos_y))
                else:
                    canvas.paste(top, (pos_x, pos_y))

def create_image(puzzle):
    # TODO: make dynamic canvas to fit any puzzle size
    canvas = Image.open('resources/canvas.png')
    draw = ImageDraw.Draw(canvas)

    _add_values(draw, puzzle.get_matrix())
    _add_row_constraints(canvas, puzzle.get_row_constraints())
    _add_col_constraints(canvas, puzzle.get_col_constraints())

    canvas.show()