""" Введение в ООП"""
# ---Простой класс ---
# import Student as s
# s= s.Student("test","test","test")
# s1= s.Student2()
# import Car as c
# car = c.Car("test","test", 2022)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Оценка: {self.grade}"

# --- Методы с возвратом значения ---
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)


# --- Наследование ---
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."
class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"


# --- Полиморфизм: один интерфейс — разное поведение ---
# Одна функция работает с разными типами через общий метод
def make_sound(animal):
    """Полиморфизм: animal может быть Dog, Cat или любой наследник Animal"""
    return animal.speak()


# ещё один пример полиморфизма
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2


def print_area(shape):
    """Полиморфизм: shape может быть Circle, Square или любая фигура"""
    print(f"Площадь: {shape.area()}")


# --- Инкапсуляция (приватные атрибуты) ---
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount
    def get_balance(self):
        return self._balance

# --- Абстракция (ABC) ---
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        return "Двигатель машины заведён"


# --- Композиция: связь «имеет» (has-a) ---
# Один объект содержит другие объекты как часть себя
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"«{self.title}» — {self.author}"


class Library:
    """Библиотека «имеет» список книг — это композиция"""
    def __init__(self):
        self.books = []  # Library содержит объекты Book

    def add_book(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def total_books(self):
        return len(self.books)


# --- Запуск примеров ---
if __name__ == "__main__":
    s = Student("Алиса", 20, 85)
    print(s.info())

    r = Rectangle(5, 3)
    print(f"Площадь: {r.area()}, Периметр: {r.perimeter()}")
    #
    # d = Dog("Бобик")
    # c = Cat("Мурка")
    # print(f"{d.name}: {d.speak()}")
    # print(f"{c.name}: {c.speak()}")

    # # Полиморфизм: одна функция — разные объекты
    animal = Dog("Test")
    print(make_sound(animal))
    # for animal in [Dog("Рекс"), Cat("Васька")]:
    #     print(f"{animal.name}: {make_sound(animal)}")
    #
    # for shape in [Circle(5), Square(4)]:
    #     print_area(shape)

    acc = BankAccount(1000)
    acc.deposit(500)
    print(f"Баланс: {acc.get_balance()}")

    # car = Car()
    # print(car.start_engine())
    #
    # # Композиция: Library «имеет» список Book
    # print("\n--- Композиция (библиотека) ---")
    # lib = Library()
    # lib.add_book(Book("Война и мир", "Толстой"))
    # lib.add_book(Book("Анна Каренина", "Толстой"))
    # lib.add_book(Book("Преступление и наказание", "Достоевский"))
    # print(f"Всего книг: {lib.total_books()}")
    # for book in lib.find_by_author("Толстой"):
    #     print(f"  {book}")
