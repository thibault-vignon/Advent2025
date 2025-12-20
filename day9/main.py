def calculate_rectangle(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        points = []
        for line in lines:
            nums = line.strip().split(',')
            points.append([int(num) for num in nums])
    best_area = 0
    for idx in range(len(points)):
        for p in points[:idx]:
            area = (abs(points[idx][0] - p[0]) + 1) * (abs(points[idx][1] - p[1]) + 1)
            if area > best_area:
                best_area = area
    print(best_area)

if __name__ == '__main__':
    calculate_rectangle("input.txt")
