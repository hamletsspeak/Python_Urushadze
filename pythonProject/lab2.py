# def possible_numbers(n, guesses):
#     possible = set(range(1, n + 1))
#     for guess, response in guesses:
#         print("Беатриса спрашивает:", guess)
#         print("Август отвечает:", response)
#         guess_set = set(map(int, guess.split()))
#         if response == "YES":
#             possible &= guess_set
#         else:
#             possible -= guess_set
#     return sorted(possible)
#
#
# if __name__ == "__main__":
#     n = int(input())
#     guesses = []
#     while True:
#         try:
#             guess = input()
#             if guess == "HELP":
#                 break
#             response = input()
#             guesses.append((guess, response))
#         except EOFError:
#             break
#
#     result = possible_numbers(n, guesses)
#
#     Вывод результатов
    # if result:
    #     print("Числа, которые мог задумать Август:", end=" ")
    #     print(*result)
    # else:
    #     print("Август не мог задумать ни одного числа из заданных вопросов.")


# def count_votes(records):
#     votes = {}
#     for record in records:
#         candidate, count = record.split()
#         count = int(count)
#         if candidate in votes:
#             votes[candidate] += count
#         else:
#             votes[candidate] = count
#     return votes
#
#
# def main():
#     n = int(input("Введите количество записей: "))
#     records = [input() for _ in range(n)]
#     votes = count_votes(records)
#
    # Сортировка по алфавиту и вывод результатов
    # for candidate, count in sorted(votes.items()):
    #     print(candidate, count)


# if __name__ == "__main__":
#     main()

