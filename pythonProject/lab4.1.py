def read_input_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        N, K, V, M = map(int, data[0].split())
        houses = [(int(line.split()[0]), int(line.split()[1])) for line in data[1:]]
    return N, K, V, M, houses


def calculate_deliveries(N, K, V, M, houses):
    max_deliveries = 0
    best_location = 0

    for i in range(K):
        deliveries = 0
        for house in houses:
            distance = min(abs(house[0] - i), K - abs(house[0] - i))  # considering circular road
            if distance <= M:
                deliveries += -(-house[1] // V)  # ceiling division to calculate number of packages
        if deliveries > max_deliveries:
            max_deliveries = deliveries
            best_location = i

    return max_deliveries


def main():
    file_names = ["Files/27-124a.txt", "Files/27-124b.txt"]
    for file_name in file_names:
        N, K, V, M, houses = read_input_file(file_name)
        max_deliveries = calculate_deliveries(N, K, V, M, houses)
        print(max_deliveries, end=' ')


if __name__ == "__main__":
    main()
