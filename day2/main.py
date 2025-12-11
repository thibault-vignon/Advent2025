import math


def count_doubles(filepath):
    with open(filepath, 'r') as file:
        line = file.readlines()[0]
        total_ids = 0
        pairs = line.split(',')
        for pair in pairs:
            print(f"Starting pair {pair}, current total is {total_ids}")
            start = int(pair.split('-')[0])
            end = int(pair.split('-')[1])
            start_digits = int(math.log10(start)) + 1
            print(f"Start {start}, end {end}, start digits {start_digits}")
            if start_digits % 2 == 0:
                multiplier = 10 ** (start_digits // 2)
                first_half = start // multiplier
                second_half = start % multiplier
                if first_half < second_half:
                    first_half = first_half + 1
            else:
                first_half = 10 ** (start_digits // 2)
                multiplier = first_half * 10
            number = first_half * multiplier + first_half
            print(f"First number {number}")
            while number <= end:
                total_ids += number
                first_half += 1
                if first_half == multiplier:
                    multiplier = multiplier * 10
                number = first_half * multiplier + first_half
            print(f"Final multiplier {multiplier}, final number {number}")
    print(f"Total IDs {total_ids}")


def count_multiples(filepath):
    with open(filepath, 'r') as file:
        line = file.readlines()[0]
        total_ids = 0
        pairs = line.split(',')
        for pair in pairs:
            print(f"Starting pair {pair}, current total is {total_ids}")
            start = int(pair.split('-')[0])
            end = int(pair.split('-')[1])
            print(f"Start {start}, end {end}")
            for number in range(start, end + 1):
                number_length = int(math.log10(number)) + 1
                substring_length = 0
                is_invalid = False
                while substring_length + 1 <= number_length // 2:
                    substring_length += 1
                    if number_length % substring_length != 0:
                        continue
                    substring = str(number)[:substring_length]
                    candidate = int((number_length // substring_length) * substring)
                    if candidate == number:
                        is_invalid = True
                        break
                if is_invalid:
                    total_ids += number
    print(f"Total IDs {total_ids}")

if __name__ == '__main__':
    count_doubles("input.txt")
    count_multiples("input.txt")
