import random

def create_maze(w, h):
    canvas = []
    # looping throw height and multiplying by the width
    for i in range(h):
        if i == 0 or i == h-1:
            row = ['*' for i in range(w)]
            canvas.append(row)
            # print(''.join(row))
            # if i == h-1 : print( ' -------------------  ')
        else:
            row = ['*' for i in range(w)]
            row[1:-1]= [' ' for i in range(w-2)]
            canvas.append(row)
            # print(''.join(row))
    return canvas


def random_o_x_canvas(canvas):
    # Function to create a random initial position of the player and the exit of the maze
    if len(canvas) > 2 and len(canvas[0]) > 2:  # Check to avoid index errors in case of very small mazes.
        row_exit = random.randint(1, len(canvas) - 2)
        col_exit = random.randint(1, len(canvas[0]) - 2)
        # Ensure player and exit do not overlap
        row_player, col_player = row_exit, col_exit
        while row_player == row_exit and col_player == col_exit:
            row_player = random.randint(1, len(canvas) - 2)
            col_player = random.randint(1, len(canvas[0]) - 2)

        canvas[row_player][col_player] = 'o'
        canvas[row_exit][col_exit] = 'X'

        #adding the '*' after the 'X', the range method ( from, to )
        for col in range(col_exit + 1, len(canvas[0])):
            canvas[row_exit][col] = '*'

        walls_input = random.randint(1, len(canvas) - 2)
        for _ in range(walls_input):
            wall_row = random.randint(3, len(canvas) - 2)
            wall_col_start = random.randint(0, len(canvas[0]) - 2)
            # Start from the wall_col_start and continue until you hit a non-empty cell
            for col in range(wall_col_start, len(canvas[0])):
                if canvas[wall_row][col] == ' ':
                    canvas[wall_row][col] = '*'
                else:
                    break
    else:
        print("Canvas is too small to place 'o'|'X' without touching the borders.")
    # return canvas
    for row in canvas:
        print(''.join(row))

def main():
    while True:
        try:
            width = int(input("Enter width of the maze: "))
            height = int(input("Enter height of the maze: "))
            canvas = create_maze(width, height)
            random_o_x_canvas(canvas)
            break
        except ValueError:
            pass

if __name__ == '__main__':
    main()