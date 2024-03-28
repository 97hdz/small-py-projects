def create_maze(w, h):
    canvas = []
    # looping throw height and multiplying by the width
    for i in range(h):
        if i == 0 or i == h-1:
            row = ['*' for i in range(w)]
            canvas.append(row)
            print(''.join(row))
        else:
            row[0], row[1:-1], row[-1] = '*' , [' ' for i in range(w-2)] , '*'
            canvas.append(row)
            print(''.join(row))


def main():
    width = int(input("Enter width of the maze: "))
    height = int(input("Enter height of the maze: "))
    create_maze(width, height)


if __name__ == '__main__':
    main()