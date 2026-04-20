import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)  # 10 čísel v rozsahu 0–100
print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]


def selection_sort(input_collection):
    cloned_data = input_collection[:]

    for current_pos, _ in enumerate(cloned_data):
        print(cloned_data)

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

def main():
    randomized_batch = random_numbers(20)
    ordered_batch = selection_sort(randomized_batch)

    print("--- Test s náhodným seznamem ---")
    print(f"Původní stav:  {randomized_batch}")
    print(f"Seřazený stav: {ordered_batch}")


if __name__ == "__main__":
    main()