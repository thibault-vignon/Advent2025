def calculate_splits(filepath):
    splits = 0
    with open(filepath, 'r') as file:
        lines = file.readlines()
        width = len(lines[0].strip())
        start_col = len(lines[0].strip().split('S')[0])
        matrix = [[start_col]]
        for row in range(1, len(lines)):
            matrix.append([])
            for col in matrix[row - 1]:
                if lines[row][col] == '.':
                    if col not in matrix[row]:
                        matrix[row].append(col)
                else:
                    splits += 1
                    if col > 0 and (col - 1) not in matrix[row]:
                        matrix[row].append(col - 1)
                    if col + 1 < width:
                        matrix[row].append(col + 1)
    print(splits)


def calculate_timelines(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        width = len(lines[0].strip())
        start_col = len(lines[0].strip().split('S')[0])
        matrix = [{start_col: 1}]
        for row in range(1, len(lines)):
            matrix.append({})
            for col in matrix[row - 1]:
                if lines[row][col] == '.':
                    if col not in matrix[row]:
                        matrix[row][col] = matrix[row - 1][col]
                    else:
                        matrix[row][col] += matrix[row - 1][col]
                else:
                    if col > 0:
                        if (col - 1) not in matrix[row]:
                            matrix[row][col - 1] = matrix[row - 1][col]
                        else:
                            matrix[row][col - 1] += matrix[row - 1][col]
                    if col + 1 < width:
                        matrix[row][col + 1] = matrix[row - 1][col]
    print(sum(matrix[len(lines) - 1][col] for col in matrix[len(lines) - 1]))


if __name__ == '__main__':
    calculate_splits("input.txt")
    calculate_timelines("input.txt")
