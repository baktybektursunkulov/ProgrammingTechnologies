from abc import ABC, abstractmethod

class StudentDataProcessor:
    """Пример класса для работы со списком студентов (dict)"""
    def __init__(self, data=None):
        self._data = data or []

    def load(self, data):
        self._data = data
        return self._data

    def filter_by_city(self, city):
        return {s["name"]: s["grade"] for s in self._data if s["city"] == city}

    def filter_young(self, age_threshold=22):
        return [s["name"] for s in self._data if s["age"] < age_threshold]


# =============================================================================
# 8. Пример: Strategy (паттерн)
# =============================================================================

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, items, key):
        pass

class SortAscending(SortStrategy):
    def sort(self, items, key):
        return sorted(items, key=lambda x: x.get(key, 0))

class SortDescending(SortStrategy):
    def sort(self, items, key):
        return sorted(items, key=lambda x: x.get(key, 0), reverse=True)


class StudentSorter:
    def __init__(self, students, strategy):
        self.students = students
        self.strategy = strategy

    def apply(self, key="grade"):
        return self.strategy.sort(self.students, key)

    def set_strategy(self, strategy):
        self.strategy = strategy


# =============================================================================
# Запуск примеров
# =============================================================================

if __name__ == "__main__":

    print("\n=== 7. StudentDataProcessor ===")
    students_data = [
        {"name": "Alice", "age": 20, "grade": 92, "city": "Almaty"},
        {"name": "Bob", "age": 22, "grade": 78, "city": "Astana"},
        {"name": "Charlie", "age": 21, "grade": 85, "city": "Almaty"},
    ]
    proc = StudentDataProcessor(students_data)
    print("Almaty:", proc.filter_by_city("Almaty"))
    print("Младше 22:", proc.filter_young(22))

    print("\n=== 8. Strategy (сортировка) ===")
    students = [{"name": "A", "grade": 85}, {"name": "B", "grade": 92}, {"name": "C", "grade": 78}]
    sorter = StudentSorter(students, SortDescending())
    print("По убыванию grade:", [s["name"] for s in sorter.apply("grade")])
    sorter.set_strategy(SortAscending())
    print("По возрастанию grade:", [s["name"] for s in sorter.apply("grade")])
