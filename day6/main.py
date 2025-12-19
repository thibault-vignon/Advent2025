def calculate(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        nums_matrix = []
        for row in range(len(lines) - 1):
            nums_matrix.append([])
            string = lines[row].strip()
            for num in string.split(' '):
                if len(num) > 0:
                    nums_matrix[row].append(int(num))
        ops_list = []
        for op in lines[len(lines) - 1].strip().split(' '):
            if len(op) > 0:
                ops_list.append(op)
    total = 0
    for col in range(len(ops_list)):
        op = ops_list[col]
        val = nums_matrix[0][col]
        for row in range(1, len(lines) - 1):
            if op == '+':
                val += nums_matrix[row][col]
            elif op == '*':
                val *= nums_matrix[row][col]
            else:
                raise ValueError
        total += val
    print(total)


def calculate_columns(filepath):
    total = 0
    with open(filepath, 'r') as file:
        lines = file.readlines()
        ops_list = []
        ops_cols_list = []
        for col, op in enumerate(lines[len(lines) - 1].strip()):
            if op != ' ':
                ops_list.append(op)
                ops_cols_list.append(col)
        for idx in range(len(ops_list)):
            op = ops_list[idx]
            col = ops_cols_list[idx]
            if op == '+':
                val = 0
            elif op == '*':
                val = 1
            else:
                raise ValueErro
            if idx < len(ops_list) - 1:
                last_col = ops_cols_list[idx + 1] - 1
            else:
                last_col = len(lines[1].strip())
            while col < last_col:
                numstring = ''
                for row in range(len(lines) - 1):
                    if lines[row][col] != ' ':
                        numstring += lines[row][col]
                if op == '+':
                    val += int(numstring)
                else:
                    val *= int(numstring)
                col += 1
            total += val
    print(total)


if __name__ == '__main__':
    calculate("input.txt")
    calculate_columns("input.txt")
