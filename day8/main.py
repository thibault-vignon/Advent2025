def calculate_circuits(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        points = []
        for line in lines:
            nums = line.strip().split(',')
            points.append([int(num) for num in nums])
        distances = {}
        for i in range(len(points)):
            for j in range(i):
                distances[(i,j)] = sum((points[i][k] - points[j][k])**2 for k in [0,1,2])
        sorted_distances = sorted(distances.items(), key=lambda item: item[1])
        points_by_circuit = [[idx] for idx in range(len(points))]
        circuit_by_point = [idx for idx in range(len(points))]
        for pair in sorted_distances[:1000]:
            first_circuit = circuit_by_point[pair[0][0]]
            second_circuit = circuit_by_point[pair[0][1]]
            if first_circuit != second_circuit:
                points_by_circuit[first_circuit] = points_by_circuit[first_circuit] + points_by_circuit[second_circuit]
                for idx in points_by_circuit[second_circuit]:
                    circuit_by_point[idx] = first_circuit
        circuit_lengths = {}
        for idx in range(len(points)):
            if circuit_by_point[idx] not in circuit_lengths:
                circuit_lengths[circuit_by_point[idx]] = len(points_by_circuit[circuit_by_point[idx]])
        sorted_lengths = sorted(circuit_lengths.items(), key=lambda item: -item[1])
    print(sorted_lengths[0][1] * sorted_lengths[2][1] * sorted_lengths[1][1])


def calculate_circuits_2(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        points = []
        for line in lines:
            nums = line.strip().split(',')
            points.append([int(num) for num in nums])
        distances = {}
        for i in range(len(points)):
            for j in range(i):
                distances[(i,j)] = sum((points[i][k] - points[j][k])**2 for k in [0,1,2])
        sorted_distances = sorted(distances.items(), key=lambda item: item[1])
        points_by_circuit = [[idx] for idx in range(len(points))]
        circuit_by_point = [idx for idx in range(len(points))]
        for pair in sorted_distances:
            first_circuit = circuit_by_point[pair[0][0]]
            second_circuit = circuit_by_point[pair[0][1]]
            if first_circuit != second_circuit:
                points_by_circuit[first_circuit] = points_by_circuit[first_circuit] + points_by_circuit[second_circuit]
                for idx in points_by_circuit[second_circuit]:
                    circuit_by_point[idx] = first_circuit
                if len(points_by_circuit[first_circuit]) == 1000:
                    print(points[pair[0][0]][0] * points[pair[0][1]][0])
                    break


if __name__ == '__main__':
    calculate_circuits("input.txt")
    calculate_circuits_2("input.txt")
