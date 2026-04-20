import random
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    main()