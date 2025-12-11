def rotations_passing_zero(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        position = 50
        counter = 0
        for line in lines:
            line = line.strip()
            print(f"Prev counter: {counter}")
            print(f"Prev pos: {position}")
            print(f"Line: {line}")
            prev_position = position
            if line[0] == 'L':
                position = position - int(line[1:])
            elif line[0] == 'R':
                position = position + int(line[1:])
            else:
                raise RuntimeError("Unexpected input")
            bump = 0
            if line[0] == 'L':
                if prev_position == 0:
                    bump = 99
                else:
                    bump = -1
            counter += abs((position + bump) // 100)
            position = position % 100
            print(f"New counter: {counter}")
    print(f"Counter is {counter}")

def rotations_ending_zero(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        position = 50
        counter = 0
        for line in lines:
            line = line.strip()
            if line[0] == 'L':
                position = (position - int(line[1:])) % 100
            elif line[0] == 'R':
                position = (position + int(line[1:])) % 100
            else:
                raise RuntimeError("Unexpected input")
            if position == 0:
                counter += 1
    print(f"Counter is {counter}")

if __name__ == '__main__':
    rotations_ending_zero("input.txt")
    rotations_passing_zero("input.txt")
