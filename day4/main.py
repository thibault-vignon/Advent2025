def count_accessible(filepath):
    with open(filepath, 'r') as file:
        total_accessible = 0
        lines = file.readlines()
        width = len(lines[0].strip())
        height = len(lines)
        matrix = []
        for row in range(height):
            matrix.append(width * [0])
            line = lines[row]
            for col in range(width):
                char = line[col]
                if char == '@':
                    matrix[row][col] = 1
        for row in range(height):
            for col in range(width):
                if matrix[row][col] == 1:
                    neighbors = 0
                    for other_row in range(max(0, row - 1), min(height, row + 2)):
                        for other_col in range(max(0, col - 1), min(width, col + 2)):
                            if matrix[other_row][other_col] == 1 and (other_row, other_col) != (row, col):
                                neighbors += 1
                    if neighbors < 4:
                        total_accessible += 1
        print(total_accessible)


def delete_rolls(filepath):
    with open(filepath, 'r') as file:
        total_accessible = 0
        lines = file.readlines()
        width = len(lines[0].strip())
        height = len(lines)
        matrix = []
        for row in range(height):
            matrix.append(width * [0])
            line = lines[row]
            for col in range(width):
                char = line[col]
                if char == '@':
                    matrix[row][col] = 1
        total_deleted = 0
        deleted_last_it = 1
        while deleted_last_it > 0:
            deleted_last_it = 0
            for row in range(height):
                for col in range(width):
                    if matrix[row][col] == 1:
                        neighbors = 0
                        for other_row in range(max(0, row - 1), min(height, row + 2)):
                            for other_col in range(max(0, col - 1), min(width, col + 2)):
                                if matrix[other_row][other_col] == 1 and (other_row, other_col) != (row, col):
                                    neighbors += 1
                        if neighbors < 4:
                            deleted_last_it += 1
                            matrix[row][col] = 0
            total_deleted += deleted_last_it
        print(total_deleted)


if __name__ == '__main__':
    count_accessible("input.txt")
    delete_rolls("input.txt")
