import random

def create_maze_frame(w, h):
    canvas = []
    # looping throw height and multiplying by the width
    for i in range(h):
        if i == 0 or i == h-1:
            row = ['*' for i in range(w)]
            canvas.append(row)
        else:
            row = ['*' for i in range(w)]
            row[1:-1]= [' ' for i in range(w-2)]
            canvas.append(row)
    return canvas


def random_walls_and_exit(canvas):
    # Function to create a random exit of the maze
    if len(canvas) > 2 and len(canvas[0]) > 2:  # Check to avoid index errors in case of very small mazes.
        row_exit = random.randint(1, len(canvas) - 2)
        # init at 2 do not anchor to the beginning of the row
        col_exit = random.randint(2, len(canvas[0]) - 2)
        canvas[row_exit][col_exit] = 'X'
        #adding the '*' after the 'X', the range method ( from, to )
        for col in range(col_exit + 1, len(canvas[0])):
            canvas[row_exit][col] = '*'

        ## WALLS ----------------------
        walls_input = random.randint(3, len(canvas) - 2)
        for _ in range(walls_input):
            wall_row = random.randint(3, len(canvas) - 2)
            wall_col_start = random.randint(2, len(canvas[0]) - 2)
            # Start from the wall_col_start and continue until you hit a non-empty cell
            for col in range(wall_col_start, len(canvas[0])):
                if canvas[wall_row][col] == ' ':
                    canvas[wall_row][col] = '*'
                else:
                    # return canvas
                    break
    else:
        print("Canvas is too small to place 'X'")
    return canvas
    # for row in canvas:
    #     print(''.join(row))


def finding_exit(canvas):
    h, w = len(canvas), len(canvas[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    print(type(directions))
    queue = [((1, 1), [])]  # Start position with path
    visited = set([(1, 1)])

    while queue:
        (row, col), path = queue.pop(0)  # Use pop(0) to simulate queue behavior

        # Check if exit is found
        if canvas[row][col] == 'X':
            print(f"Exit found at: ({row},{col})")
            print("Path to exit:", path + [(row, col)])
            return path + [(row, col)]

        # Explore neighbors
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < h and 0 <= c < w and canvas[r][c] != '*' and (r, c) not in visited:
                visited.add((r, c))
                queue.append(((r, c), path + [(row, col)]))

    print("No exit found.")
    return None


def main():
    while True:
        try:
            width = int(input("Enter width of the maze: "))
            height = int(input("Enter height of the maze: "))
            canvas_empty = create_maze_frame(width, height)
            canvas = random_walls_and_exit(canvas_empty)
            canvas[1][1] = 'O'
            for row in canvas:
                print(''.join(row))
            finding_exit(canvas)
            break
        except ValueError:
            print("only integers allowed")
            pass

if __name__ == '__main__':
    main()