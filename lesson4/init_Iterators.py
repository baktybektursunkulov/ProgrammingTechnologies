def basic_iter_example():
    print("--- Basic iter() and next() ---")
    numbers = [1, 2, 3, 4, 5]
    it = iter(numbers)

    print(next(it))  # 1
    print(next(it))  # 2
    print(next(it))  # 3

def enumerate_zip_example():
    """enumerate() and zip() return iterators."""
    print("\n--- enumerate() and zip() ---")
    fruits = ["apple", "banana", "cherry"]
    for i, fruit in enumerate(fruits):
        print(f"{i}: {fruit}")

    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")

def list_comprehension_basic():
    print("--- List Comprehension: squares ---")
    squares = [x ** 2 for x in range(1, 6)]
    print(squares)

def list_comprehension_with_condition():
    print("\n--- List Comprehension: evens only ---")
    evens = [x for x in range(10) if x % 2 == 0]
    print(evens)

def list_comprehension_with_else():
    print("\n--- List Comprehension: if-else ---")
    result = ["even" if x % 2 == 0 else "odd" for x in range(5)]
    print(result)

def practical_examples():
    print("\n--- Practical: parse numbers ---")
    data = ["10", "20", "30", "abc", "40"]
    numbers = [int(x) for x in data if x.isdigit()]
    print(numbers)  # [10, 20, 30, 40]

    print("\n--- Practical: word lengths ---")
    sentence = "The quick brown fox"
    lengths = [len(word) for word in sentence.split()]
    print(lengths)  # [3, 5, 5, 3]

if __name__ == "__main__":
    basic_iter_example()
    enumerate_zip_example()
    list_comprehension_basic()
    list_comprehension_with_condition()
    list_comprehension_with_else()
    practical_examples()