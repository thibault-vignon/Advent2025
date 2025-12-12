def max_joltage(filepath, length):
    with open(filepath, 'r') as file:
        total_val = 0
        for line in file.readlines():
            string = line.strip()
            largest = length * [0]
            for idx in range(len(line) - 1):
                char = line[idx]
                for pos in range(length):
                    if idx < len(line) - (length - pos) and int(char) > largest[pos]:
                        largest[pos] = int(char)
                        for pos_after in range(pos + 1, length):
                            largest[pos_after] = 0
                        break
            joltage = sum(largest[pos] * (10**(length - 1 - pos)) for pos in range(length))
            print(f"Line {string} has joltage {joltage}")
            total_val += joltage
    print(f"Total joltage {total_val}")


if __name__ == '__main__':
    max_joltage("input.txt", 2)
    max_joltage("input.txt", 12)
