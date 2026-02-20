# ============ List Comprehension ============
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

def list_comprehension_string():
    print("\n--- List Comprehension: string ---")
    chars = [c.upper() for c in "hello"]
    print(chars)  # 'H', 'E', 'L', 'L', 'O'

# ============ Dict Comprehension ============
def dict_comprehension_basic():
    print("\n--- Dict Comprehension ---")
    squares_dict = {x: x ** 2 for x in range(1, 6)}
    print(squares_dict)

def dict_comprehension_from_list():
    print("\n--- Dict from list ---")
    names = ["Alice", "Bob", "Charlie"]
    name_lengths = {name: len(name) for name in names}
    print(name_lengths)

def dict_comprehension_with_condition():
    print("\n--- Dict Comprehension: filter ---")
    evens_dict = {x: x * 2 for x in range(10) if x % 2 == 0}
    print(evens_dict)

# ============ Set Comprehension ============
def set_comprehension_basic():
    print("\n--- Set Comprehension ---")
    squares_set = {x ** 2 for x in range(-3, 4)}
    print(squares_set)

def set_comprehension_dedupe():
    print("\n--- Set Comprehension: dedupe ---")
    words = ["hello", "world", "hello", "python", "world"]
    unique_lengths = {len(w) for w in words}
    print(unique_lengths)

# ============ Practical Examples ============
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
    # list_comprehension_basic()
    # list_comprehension_with_condition()
    # list_comprehension_with_else()
    # list_comprehension_string()
    #  dict_comprehension_basic()
    # dict_comprehension_from_list()
    # dict_comprehension_with_condition()
    # set_comprehension_basic()
    # set_comprehension_dedupe()
    practical_examples()
