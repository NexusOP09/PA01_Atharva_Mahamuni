import time
from bisect import insort, bisect_left

class ArrayList:
    def __init__(self, initial_capacity=2):
        self.array = [None] * initial_capacity
        self.count = 0

    def _resize(self):
        # Python lists automatically resize, but we'll demonstrate our manual strategy
        new_size = self.count + 10  # Incremental strategy
        new_array = [None] * new_size
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array

    def add(self, value):
        if self.count >= len(self.array):
            self._resize()
        self.array[self.count] = value
        self.count += 1

    def sort(self):
        self.array = sorted(self.array[:self.count])

    def binary_insert(self, value):
        insort(self.array[:self.count], value)
        self.count += 1

    def search(self, value):
        index = bisect_left(self.array[:self.count], value)
        if index < self.count and self.array[index] == value:
            return index
        return -1  # Not found


def load_words(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()


def main():
    filename = "EOWL_200 sorted.txt"  # The words file in the same directory
    words = load_words(filename)

    array_list = ArrayList()
    
    # Add words to the ArrayList and measure time
    start_time = time.time()
    for word in words:
        array_list.add(word)
    array_list.sort()  # Sort once after all additions
    end_time = time.time()
    print(f"Time taken to add and sort words: {end_time - start_time:.4f} seconds")
    
    # Measure search time
    search_word = "mountain"  # Change this word as needed
    start_time = time.time()
    index = array_list.search(search_word)
    end_time = time.time()
    if index != -1:
        print(f"Word '{search_word}' found at index {index}.")
    else:
        print(f"Word '{search_word}' not found.")
    print(f"Time taken to search for '{search_word}': {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main() 
