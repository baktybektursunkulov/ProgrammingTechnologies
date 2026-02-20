def basic_iter_example():
    print("--- Basic iter() and next() ---")
    numbers = [1, 2, 3, 4, 5]
    it = iter(numbers)

    print(next(it))  # 1
    print(next(it))  # 2
    print(next(it))  # 3
    print(next(it))  # 4
    print(next(it))  # 5

# ============ Custom Iterator Class ============
class CountDown:
    """Custom iterator that counts down from n to 0."""
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

def custom_iterator_example():
    """Using a custom iterator class."""
    print("\n--- Custom CountDown Iterator ---")
    for num in CountDown(5):
        print(num, end=" ")
    print()

def sentinel_iterator_example():
    """Using iter() with a callable and sentinel(until) value."""
    print("\n--- Iterator with sentinel ---")
    def read_until_done():
        line = input("Enter text (or 'done' to stop): ")
        return line
    for line in iter(read_until_done, 'done'):
        print(f"You entered: {line}")

    # counter = 0
    # def get_next():
    #     nonlocal counter
    #     counter += 1
    #     return counter if counter <= 3 else "stop"
    #
    # it = iter(get_next, "stop")
    # print(list(it))  # [1, 2, 3]


# ============ Infinite(forever) Iterator ============
class InfiniteCounter:
    def __init__(self, start=0):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        value = self.current
        self.current += 1
        return value

def infinite_iterator_example():
    print("\n--- Infinite Iterator (first 5) ---")
    counter = InfiniteCounter(10)
    for i, val in enumerate(counter):
        # if i >= 5:
        #     break
        print(val, end=" ")
    print()  # Output: 10 11 12 13 14

# ============ File as Iterator ============

def file_iterator_example():
    print("\n--- File as Iterator ---")
    from io import StringIO
    fake_file = StringIO("line1\nline2\nline3\n")
    for line in fake_file:
        print(line.strip())

# ============ enumerate() and zip() - Iterator Tools ============
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


if __name__ == "__main__":
     basic_iter_example()
    # custom_iterator_example()
    # sentinel_iterator_example()
    #  infinite_iterator_example()
    # file_iterator_example()
    # enumerate_zip_example()
