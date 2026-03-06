"""Lesson 5: Generators and Lambda Functions"""
from lesson5.generators_examples import yield_from_example


def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1
def basic_generator_example():
    for x in count_up_to(5):
        print(x, end=" ")
    print()

# ============ Generator vs List ============
def squares_list(n):
    """Returns a list - all values in memory."""
    return [x ** 2 for x in range(n)]
def squares_generator(n):
    """Generator - yields one value at a time, memory efficient."""
    for x in range(n):
        yield x ** 2

def generator_vs_list_example():
    print("\n--- Generator vs List (memory) ---")
    # List: all 1000000 values in memory
    # gen = squares_generator(1_000_000)  # no allocation until consumed
    gen = squares_generator(5)
    print("Generator:", list(gen))
    print("First 3 from new generator:", list(squares_generator(10))[:3])


# ============ Basic Lambda ============
def basic_lambda_example():
    print("--- Basic Lambda ---")
    add = lambda x, y: x + y
    print("add(3, 5):", add(3, 5))
    square = lambda x: x ** 2
    print("square(4):", square(4))
    is_even = lambda n: n % 2 == 0
    print("is_even(4):", is_even(4), "| is_even(7):", is_even(7))

# ============ Lambda with map() ============
def lambda_map_example():
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print("map(square, [1..5]):", squared)

    names = ["alice", "bob", "charlie"]
    capitalized = list(map(lambda s: s.capitalize(), names))
    print("map(capitalize, names):", capitalized)


# ============ Lambda with filter() ============
def lambda_filter_example():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("filter(even, [1..10]):", evens)

    words = ["apple", "banana", "cherry", "date", "elderberry"]
    short_words = list(filter(lambda w: len(w) <= 5, words))
    print("filter(len<=5, words):", short_words)


# ============ Lambda with sorted() ============
def lambda_sorted_example():
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 72},
        {"name": "Charlie", "grade": 90},
    ]
    by_grade = sorted(students, key=lambda s: s["grade"])
    print("By grade:", by_grade)

    words = ["banana", "apple", "cherry", "date"]
    by_length = sorted(words, key=lambda w: len(w))
    print("By length:", by_length)

    # Reverse order
    by_grade_desc = sorted(students, key=lambda s: s["grade"], reverse=True)
    print("By grade (desc):", by_grade_desc)

def example(a):
    test = lambda a: a*a
    yield test(a)
def squares(n):
    for i in range(n):
        yield i * i

if __name__ == "__main__":
    for value in squares(5):
        print(value)
    basic_generator_example()
    # generator_vs_list_example()
    # basic_lambda_example()
    # lambda_map_example()
    # lambda_filter_example()
    # lambda_sorted_example()