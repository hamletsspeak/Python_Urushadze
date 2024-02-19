def count_votes(records):
    votes = {}
    for record in records:
        candidate, count = record.split()
        count = int(count)
        if candidate in votes:
            votes[candidate] += count
        else:
            votes[candidate] = count
    return votes


def main():
    n = int(input("Введите количество записей: "))
    records = [input() for _ in range(n)]
    votes = count_votes(records)

    # Сортировка по алфавиту и вывод результатов
    for candidate, count in sorted(votes.items()):
        print(candidate, count)
if __name__ == "__main__":
    main()