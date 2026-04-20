import random
import matplotlib.pyplot as plt

#otázka: jak tohle může projít testem na plagiátorství když jsme kopírovali kód ze stránky + většinu jsme dělali spolu na cvičení


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


values = random_numbers(10)
print(values)


def selection_sort(input_collection):
    cloned_data = input_collection[:]

    for current_pos, _ in enumerate(cloned_data):
        if current_pos == len(cloned_data) - 1:
            break

        smallest_val_pos = current_pos

        unsorted_portion = cloned_data[current_pos + 1:]

        for search_pos, search_val in enumerate(unsorted_portion, start=current_pos + 1):
            if search_val < cloned_data[smallest_val_pos]:
                smallest_val_pos = search_pos

        if smallest_val_pos != current_pos:
            temporary_swap = cloned_data[current_pos]
            cloned_data[current_pos] = cloned_data[smallest_val_pos]
            cloned_data[smallest_val_pos] = temporary_swap

    return cloned_data


def bubble_sort(input_collection):
    values = input_collection[:]
    n = len(values)

    plt.ion()
    plt.show()

    for i in range(n):
        for j in range(0, n - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if values[j] > values[j + 1]:
                temp = values[j]
                values[j] = values[j + 1]
                values[j + 1] = temp

    plt.ioff()
    plt.show()

    return values


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def find(self, target):
        indices = []
        for i in range(len(self.scores)):
            if self.scores[i] == target:
                indices.append(i)
        return indices

    def get_sorted(self):
        scores = self.scores[:]
        n = len(scores)
        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    temp = scores[j]
                    scores[j] = scores[j + 1]
                    scores[j + 1] = temp
        return scores

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def best(self):
        if not self.scores:
            return None
        return self.get_sorted()[-1]

    def worst(self):
        if not self.scores:
            return None
        return self.get_sorted()[0]

    def pass_rate(self):
        if not self.scores:
            return 0.0
        passed = 0
        for score in self.scores:
            if score >= 50:
                passed += 1
        return passed / len(self.scores)

    def find_sorted(self, score):
        if self._sorted_scores is None:
            print("sorting...")
            self._sorted_scores = self.get_sorted()

        left = 0
        right = len(self._sorted_scores) - 1

        while left <= right:
            mid = (left + right) // 2
            if self._sorted_scores[mid] == score:
                return mid
            elif self._sorted_scores[mid] < score:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def __str__(self):
        return f"StudentsGrades: {self.count()} studentů, průměr {self.average():.1f}"

#otázka: jak tohle může projít testem na plagiátorství když jsme kopírovali kód ze stránky + většinu jsme dělali spolu na cvičení

def main():
    randomized_batch = random_numbers(20)
    ordered_batch = selection_sort(randomized_batch)

    print("--- Test s náhodným seznamem ---")
    print(f"Původní stav:  {randomized_batch}")
    print(f"Seřazený stav: {ordered_batch}")

    randomized_batch_bubble = random_numbers(10)
    ordered_batch_bubble = bubble_sort(randomized_batch_bubble)

    print("\n--- Test s náhodným seznamem (Bubble Sort - animace) ---")
    print(f"Původní stav:  {randomized_batch_bubble}")
    print(f"Seřazený stav: {ordered_batch_bubble}")

    print("\n--- Třída StudentsGrades ---")
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.get_grade(2))
    print(results.get_grade(6))
    print(results.get_grade(7))

    print(results.find(100))
    print(results.find(50))
    print(results.find(77))

    print(results.get_sorted())
    print(results.scores)

    print("\n--- Demonstrace třídy ---")
    print(f"Počet studentů: {results.count()}")
    for i in range(results.count()):
        print(f"Student {i}: {results.scores[i]} points - {results.get_grade(i)}")

    print(f"Indexy s plným počtem bodů: {results.find(100)}")
    print(f"Seřazené výsledky: {results.get_sorted()}")

    print("\n--- Náhodná data ---")
    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

    print("\n+++ Bonusy +++")
    print(results)
    print(f"Nejlepší: {results.best()}")
    print(f"Nejhorší: {results.worst()}")
    print(f"Pass rate: {results.pass_rate()}")

    print("\n+++ Binární vyhledávání s cache +++")
    print(results.find_sorted(91))
    print(results.find_sorted(50))
    print(results.find_sorted(77))

#otázka: jak tohle může projít testem na plagiátorství když jsme kopírovali kód ze stránky + většinu jsme dělali spolu na cvičení
if __name__ == "__main__":
    main()