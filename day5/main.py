def count_fresh_available(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        reading_ranges = True
        ranges = []
        available = []
        for row in range(len(lines)):
            string = lines[row].strip()
            if len(string) == 0:
                reading_ranges = False
                continue
            if reading_ranges:
                start, end = int(string.split('-')[0]), int(string.split('-')[1])
                ranges.append((start, end))
            else:
                available.append(int(string))

        count = 0
        for num in available:
            for pair in ranges:
                if pair[0] <= num <= pair[1]:
                    count += 1
                    break
        print(count)


def count_fresh(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        ranges = []
        count = 0
        for row in range(len(lines)):
            string = lines[row].strip()
            if len(string) == 0:
                break
            start, end = int(string.split('-')[0]), int(string.split('-')[1])
            for idx in range(len(ranges)):
                if start <= ranges[idx][0] and end >= ranges[idx][1]:
                    ranges[idx] = (ranges[idx][0], ranges[idx][0] - 1)
                elif start >= ranges[idx][0] and end <= ranges[idx][1]:
                    end = start - 1
                elif ranges[idx][0] <= start <= ranges[idx][1]:
                    start = ranges[idx][1] + 1
                elif ranges[idx][0] <= end <= ranges[idx][1]:
                    end = ranges[idx][0] - 1
            ranges.append((start, end))

        for pair in ranges:
            count += pair[1] - pair[0] + 1
        print(count)

if __name__ == '__main__':
    count_fresh_available("input.txt")
    count_fresh("input.txt")
