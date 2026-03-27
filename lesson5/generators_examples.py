"""
Examples: Generators in Python
- Generator functions (yield)
- Generator expressions
- Lazy evaluation
- Infinite sequences
- Chaining generators
"""


# ============ Basic Generator Function ============
def count_up_to(n):
    """Generator that yields values from 0 to n-1."""
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


# ============ Generator Expression ============
def generator_expression_example():
    print("\n--- Generator Expression ---")
    # Like list comprehension but with () instead of []
    squares_gen = (x ** 2 for x in range(5))
    print("Type:", type(squares_gen))
    print("Values:", list(squares_gen))

    # Use in for-loop directly
    total = sum(x ** 2 for x in range(10))  # no extra list created
    print("Sum of squares 0..9:", total)


# ============ Infinite Generator ============
def fibonacci():
    """Infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def infinite_generator_example():
    print("\n--- Infinite Generator: Fibonacci ---")
    fib = fibonacci()
    first_10 = [next(fib) for _ in range(10)]
    print("First 10 Fibonacci:", first_10)


# ============ Generator with yield from ============
def flatten(nested_list):
    """Flatten nested list using yield from."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def yield_from_example():
    print("\n--- yield from: flatten ---")
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print("Flattened:", list(flatten(nested)))


# ============ Reading Large Files ============
def read_large_file_line_by_line(file_path):
    """Generator to read file line by line - memory efficient."""
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def read_chunks_example():
    print("\n--- Reading in chunks ---")
    from io import StringIO
    fake_file = StringIO("line1\nline2\nline3\n")
    for line in fake_file:
        print(f"  Got: {line.strip()}")


# ============ Chaining Generators ============
def integers():
    """Yield integers starting from 0."""
    n = 0
    while True:
        yield n
        n += 1


def squares(seq):
    """Yield squares of sequence."""
    for x in seq:
        yield x ** 2


def take(n, seq):
    """Take first n elements from sequence."""
    for _ in range(n):
        try:
            yield next(seq)
        except StopIteration:
            return


def chaining_example():
    print("\n--- Chaining Generators ---")
    # Pipeline: integers -> squares -> take 5
    result = list(take(5, squares(integers())))
    print("First 5 squares (0-4):", result)


# ============ Generator State ============
def generator_state_example():
    print("\n--- Generator State ---")
    gen = count_up_to(5)
    print("next(gen):", next(gen))  # 0
    print("next(gen):", next(gen))  # 1
    print("next(gen):", next(gen))  # 2
    print("Remaining:", list(gen))  # [3, 4] - continues from where it left off


# ============ send() and throw() ============
def echo_generator():
    """Generator that can receive values via send()."""
    while True:
        received = yield
        if received is None:
            break
        print(f"  Received: {received}")


def send_example():
    print("\n--- Generator send() ---")
    gen = echo_generator()
    next(gen)  # prime the generator
    gen.send("hello")
    gen.send("world")
    try:
        gen.send(None)
    except StopIteration:
        pass


if __name__ == "__main__":
    basic_generator_example()
    # generator_vs_list_example()
    # generator_expression_example()
    # infinite_generator_example()
    # yield_from_example()
    # read_chunks_example()
    # chaining_example()
    # generator_state_example()
    # send_example()
