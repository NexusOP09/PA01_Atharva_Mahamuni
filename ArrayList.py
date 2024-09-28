import time
from bisect import insort

class ArrayList:
    def __init__(self, initial_capacity=2):
        self.array = [None] * initial_capacity  # Initialize the array with a fixed capacity
        self.count = 0  # Number of elements in the array

    def _resize(self):
        # Increase the size of the array by a specified strategy
        new_size = self.count + 10  # Incremental strategy: increase by 10
        new_array = [None] * new_size
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array

    def add(self, value):
        # Add a new element to the array
        if self.count >= len(self.array):
            self._resize()  # Resize if the array is full
        self.array[self.count] = value
        self.count += 1

    def sort(self):
        # Sort the elements in the array
        self.array = sorted(self.array[:self.count])

    def binary_insert(self, value):
        # Insert an element while maintaining sorted order
        insort(self.array[:self.count], value)
        self.count += 1

    def search(self, value):
        # Search for an element using binary search
        left, right = 0, self.count - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == value:
                return mid  # Found the element
            elif self.array[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Not found


def load_words(filename):
    # Load words from a text file
    with open(filename, 'r') as file:
        return file.read().splitlines()
    

def main():
    filename = "EOWL_200 sorted.txt"  # The words file in the same directory
    words = load_words(filename)

    # Create an instance of ArrayList
    array_list = ArrayList()
    
    # Add words to the ArrayList and measure time
    start_time = time.time()
    for word in words:
        array_list.add(word)  # Add word to the list
    array_list.sort()  # Sort the list after all additions
    end_time = time.time()
    print(f"Time taken to add and sort words: {end_time - start_time:.4f} seconds")
    
    # Measure search time for a specific word
    search_word = "mountain"  # Change this word as needed
    start_time = time.time()
    index = array_list.search(search_word)  # Search for the word
    end_time = time.time()
    if index != -1:
        print(f"Word '{search_word}' found at index {index}.")
    else:
        print(f"Word '{search_word}' not found.")
    print(f"Time taken to search for '{search_word}': {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()
