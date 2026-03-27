"""
Examples: Lambda Functions in Python
- Basic syntax
- With built-in functions (map, filter, sorted)
- Single expression limitation
- Common use cases
"""


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
    print("\n--- Lambda + map() ---")
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print("map(square, [1..5]):", squared)

    names = ["alice", "bob", "charlie"]
    capitalized = list(map(lambda s: s.capitalize(), names))
    print("map(capitalize, names):", capitalized)


# ============ Lambda with filter() ============
def lambda_filter_example():
    print("\n--- Lambda + filter() ---")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("filter(even, [1..10]):", evens)

    words = ["apple", "banana", "cherry", "date", "elderberry"]
    short_words = list(filter(lambda w: len(w) <= 5, words))
    print("filter(len<=5, words):", short_words)


# ============ Lambda with sorted() ============
def lambda_sorted_example():
    print("\n--- Lambda + sorted() ---")
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 72},
        {"name": "Charlie", "grade": 90},
    ]
    by_grade = sorted(lambda s: s["grade"],students)
    print("By grade:", by_grade)

    words = ["banana", "apple", "cherry", "date"]
    by_length = sorted(words, key=lambda w: len(w))
    print("By length:", by_length)

    # Reverse order
    by_grade_desc = sorted(students, key=lambda s: s["grade"], reverse=True)
    print("By grade (desc):", by_grade_desc)


# ============ Lambda with reduce() ============
def lambda_reduce_example():
    print("\n--- Lambda + reduce() ---")
    from functools import reduce

    numbers = [1, 2, 3, 4, 5]
    product = reduce(lambda a, b: a * b, numbers)
    print("reduce(mul, [1..5]):", product)

    words = ["hello", " ", "world"]
    concatenated = reduce(lambda a, b: a + b, words)
    print("reduce(concat, words):", concatenated)


# ============ Lambda as key in max/min ============
def lambda_max_min_example():
    print("\n--- Lambda + max/min ---")
    words = ["apple", "banana", "cherry", "date"]
    longest = max(words, key=lambda w: len(w))
    shortest = min(words, key=lambda w: len(w))
    print("Longest:", longest, "| Shortest:", shortest)

    students = [{"name": "Alice", "age": 20}, {"name": "Bob", "age": 25}]
    oldest = max(students, key=lambda s: s["age"])
    print("Oldest:", oldest)


# ============ Lambda in default dict/list ============
def lambda_default_example():
    print("\n--- Lambda for defaults ---")
    from collections import defaultdict

    # Group by length
    words = ["a", "ab", "abc", "ab", "a"]
    by_len = defaultdict(list)
    for w in words:
        by_len[len(w)].append(w)
    print("Group by length:", dict(by_len))


# ============ Multiple arguments ============
def lambda_multi_arg_example():
    print("\n--- Lambda: multiple args ---")
    full_name = lambda first, last: f"{first} {last}"
    print("full_name('John', 'Doe'):", full_name("John", "Doe"))

    # *args
    sum_all = lambda *args: sum(args)
    print("sum_all(1,2,3,4):", sum_all(1, 2, 3, 4))


# ============ Lambda vs def ============
def lambda_limitations():
    print("\n--- Lambda limitations ---")
    print("Lambda: single expression only, no statements")
    print("Use def for: multiple lines, assignments, loops")

    # This works - single expression
    valid = lambda x: x * 2 if x > 0 else 0
    print("valid(5):", valid(5), "| valid(-3):", valid(-3))


# ============ Practical: Custom sort ============
def practical_sort_example():
    print("\n--- Practical: complex sort ---")
    data = [
        ("Alice", 25, "Engineer"),
        ("Bob", 30, "Designer"),
        ("Charlie", 25, "Engineer"),
    ]
    # Sort by age, then by name
    sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
    print("Sort by (age, name):", sorted_data)


if __name__ == "__main__":
    # print(filter([1,2,3], key = lambda x: x>15))

    # basic_lambda_example()
    # lambda_map_example()
    # lambda_filter_example()
    lambda_sorted_example()
    # lambda_reduce_example()
    # lambda_max_min_example()
    # lambda_multi_arg_example()
    # lambda_limitations()
    # practical_sort_example()
