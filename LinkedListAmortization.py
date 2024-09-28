import time
from bisect import insort

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            previous = None
            while current and current.data < value:
                previous = current
                current = current.next
            new_node.next = current
            if previous is None:
                self.head = new_node
            else:
                previous.next = new_node
        self.size += 1

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result


def load_words(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()


def main():
    filename = "EOWL_200 sorted.txt"  # The words file in the same directory
    words = load_words(filename)

    strategies = ['incremental', 'doubling', 'fib']

    for strategy in strategies:
        print(f"\nUsing strategy: {strategy}")
        linked_list = LinkedList()

        # Add words to the linked list and measure time
        start_time = time.time()
        for word in words:
            linked_list.add(word)
        end_time = time.time()
        print(f"Time taken to add words: {end_time - start_time:.4f} seconds")
        
        # Measure search time
        search_word = "mountain"  # Change this word as needed
        start_time = time.time()
        found = linked_list.search(search_word)
        end_time = time.time()
        if found:
            print(f"Word '{search_word}' found.")
        else:
            print(f"Word '{search_word}' not found.")
        print(f"Time taken to search for '{search_word}': {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()
