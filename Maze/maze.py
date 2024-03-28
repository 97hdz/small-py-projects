import random

def create_maze(w, h):
    canvas = []
    # looping throw height and multiplying by the width
    for i in range(h):
        if i == 0 or i == h-1:
            row = ['*' for i in range(w)]
            canvas.append(row)
            print(''.join(row))
            if i == h-1 : print( ' -------------------  ')
        else:
            row = ['*' for i in range(w)]
            row[1:-1]= [' ' for i in range(w-2)]
            canvas.append(row)
            print(''.join(row))

    '''
    #another way of visualizing the maze
    canvas_n = int(len(canvas))
    for i in range(canvas_n+1):
        print(''.join(canvas[i-1]))
    '''
    return canvas

def randomly_player_canvas(canvas):
    if len(canvas) > 2 and len(canvas[0]) > 2:  # Check to avoid index errors in case of very small mazes.
        row = random.randint(1, len(canvas) - 2)
        col = random.randint(1, len(canvas[0]) - 2)
        canvas[row][col] = 'o'
    else:
        print("Canvas is too small to place 'o' without touching the borders.")

    for row in canvas:
        print(''.join(row))

def main():
    width = int(input("Enter width of the maze: "))
    height = int(input("Enter height of the maze: "))
    possibility = (height - 2) * (width - 2)
    # print(possibility)
    canvas = create_maze(width, height)
    randomly_player_canvas(canvas)

if __name__ == '__main__':
    main()