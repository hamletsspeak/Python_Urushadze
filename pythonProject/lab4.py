def write_decreasing_lengths(input_file, output_file):
    with open(input_file, 'r') as f:
        numbers = [float(num) for num in f.readline().split()]

    decreasing_lengths = []
    length = 1

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            length += 1
        else:
            if length > 1:
                decreasing_lengths.append(length)
            length = 1

    if length > 1:  # Handle the last decreasing sequence
        decreasing_lengths.append(length)

    with open(output_file, 'w') as f:
        for length in decreasing_lengths:
            f.write(str(length) + '\n')

# Пример использования
input_filename = 'Files/input.txt'  # Имя файла с вещественными числами
output_filename = 'Files/output.txt'  # Имя файла, куда будут записаны длины убывающих последовательностей

write_decreasing_lengths(input_filename, output_filename)
