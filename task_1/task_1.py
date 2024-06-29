"""
The Order of Wisdom
The university lecture scheduler has three key professors — Alejandro, Bernardo, and Vicente — planned
to give a series of guest lectures which are expected to significantly boost the university's academic reputation.
They hypothesize that the impact of these lectures on students and faculty will be maximized if the professors speak
in a particular sequence: Alejandro first, followed by Bernardo, and then Vicente.
But there are also five other speakers set to present. However, the organizers have not yet decided the exact order for
all the presentations.What are the probabilities that the three key professors will present in the optimal sequence?
It should be noted that it does not matter if other speakers present before, in between, or after the three professors;
the critical factor for achieving the desired impact is that the sequence of Alejandro,
Bernardo, and Vicente's lectures is preserved.

Необходимо решить данную задачу
1) Математически
2) Полным перебором всевозможных вариантов (ф-ция на python)
3) Мат. Моделированием: N раз генерируем случайную перестановку  (ф-ция на python)
"""

from random import shuffle


def n_random_permutations(speakers, n):
    """3) Мат. Моделирование: N раз генерируем случайную перестановку"""
    n_good_sequences = 0
    for _ in range(n):
        shuffle(speakers)
        if speakers.index("A") < speakers.index("B") < speakers.index("V"):
            n_good_sequences += 1
    return n_good_sequences / n


def count_all_possible_options(
    speakers, curr_sequence, n_sequences=[0], n_good_sequences=[0]
):
    """2) Полный перебор всевозможных вариантов"""

    if len(speakers) == 0:
        n_sequences[0] += 1
        if (
            curr_sequence.index("A")
            < curr_sequence.index("B")
            < curr_sequence.index("V")
        ):
            n_good_sequences[0] += 1

    for i in range(len(speakers)):
        remaining_speakers = speakers[:i] + speakers[i + 1:]
        new_sequence = curr_sequence + [speakers[i]]
        count_all_possible_options(remaining_speakers, new_sequence)

    return n_good_sequences[0], n_sequences[0]


def main():
    # Alejandro, Bernardo, Vicente - A, B, V
    n_other_speakers = 5
    speakers = ["A", "B", "V"] + [i for i in range(n_other_speakers)]
    print("Количество других спикеров: ", n_other_speakers)
    print("Список спикеров: ", speakers)

    # 2) Полный перебор всевозможных вариантов
    print("\n2) Полный перебор всевозможных вариантов:")
    n_good_sequences, n_sequences = count_all_possible_options(speakers, [])
    print(f"Всего последовательностей: {n_sequences}")
    print(f"Последовательностей, когда профессора в правильном порядке: {n_good_sequences}")
    print(f"Вероятность правильной расстановки: {n_good_sequences / n_sequences}")

    # 3) Мат. Моделирование
    print("\n3) Мат. Моделирование:")
    n = 5 * 10**5
    prob = n_random_permutations(speakers, n)
    print(f"Количество случайных перестановок: {n}")
    print(f"Вероятность правильной расстановки: {prob}")


if __name__ == "__main__":
    main()
