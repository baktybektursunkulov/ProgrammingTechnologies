# Задачи Medium

**Уровень:** Medium  
**Данные:** Только код, без внешних файлов. Используйте списки и словари, созданные в программе.

---

## Задача M1. Кэширующий загрузчик (medium)

**Цель:** Инкапсуляция и управление состоянием.

1. Класс `CachedDataLoader`:
   - конструктор принимает список данных (например, `[1, 2, 3]` или список dict);
   - метод `get_data()` — при первом вызове возвращает данные и сохраняет в `_cache`, при последующих — из кэша;
   - метод `invalidate()` — сбрасывает кэш.
2. Запрещено использовать глобальные переменные.
3. Создайте загрузчик с данными `[10, 20, 30]`, вызовите `get_data()` дважды, `invalidate()`, затем снова `get_data()`.

---

## Задача M2. Иерархия продуктов (medium)

**Цель:** ABC, наследование, полиморфизм.

1. Абстрактный класс `Product` (ABC) с методом `get_display_info()`.
2. `ElectronicsProduct(Product)` — атрибуты `name`, `price`. Вывод: название, цена, «Электроника».
3. `FurnitureProduct(Product)` — атрибуты `name`, `price`. Вывод: название, цена, «Мебель».
4. `GenericProduct(Product)` — для неизвестной категории.
5. Функция `product_from_dict(d)` — по `d["category"]` возвращает нужный подкласс.
6. Создайте список товаров в коде (3–4 dict с полями `name`, `price`, `category`), выведите `get_display_info()` для каждого.

---

## Задача M3. Стратегия сортировки (medium)

**Цель:** Паттерн Strategy.

1. Абстрактный класс `SortStrategy` (ABC) с методом `sort(items, key) -> list`.
2. `SortAscending` и `SortDescending` — сортировка по ключу.
3. Класс `DataSorter`:
   - конструктор: `(items, strategy)`;
   - метод `apply(key)` — применяет стратегию;
   - метод `set_strategy(strategy)` — смена стратегии.
4. Создайте список `[{"name": "A", "grade": 85}, {"name": "B", "grade": 92}, {"name": "C", "grade": 78}]`. Отсортируйте по `grade` по убыванию (топ-3), затем по возрастанию (первые 3).

---

## Задача M4. Агрегатор данных (medium)

**Цель:** Композиция, абстрактные источники.

1. `DataSource` (ABC) с методом `fetch() -> list[dict]`.
2. `ListDataSource(DataSource)` — конструктор принимает список dict, `fetch()` возвращает его.
3. Класс `DataAggregator`:
   - конструктор принимает список `DataSource`;
   - `merge_all()` — конкатенация результатов;
   - `total_records()` — общее количество.
4. Создайте два `ListDataSource` с разными данными (например, студенты и товары), объедините через агрегатор, выведите `total_records()` и первые 2 записи.

---

## Задача M5. Цепочка обработчиков (medium)

**Цель:** Паттерн Chain of Responsibility.

1. `LogHandler` (ABC): атрибут `next_handler`, метод `set_next(handler)`, метод `handle(record) -> str`.
2. `InfoHandler` — для `record["level"] == "INFO"` → `"[INFO] message"`, иначе передаёт дальше.
3. `WarningHandler` — для `"WARNING"` → `"[WARN] message"`.
4. `ErrorHandler` — для `"ERROR"` → `"[ERR] message"`.
5. `DefaultHandler` — для остальных → `"[???] message"`.
6. Создайте список логов в коде: `[{"level": "INFO", "message": "Start"}, {"level": "ERROR", "message": "Fail"}, ...]`. Соберите цепочку, обработайте каждую запись.

---

## Задача M6. Фабрика с реестром (medium)

**Цель:** Регистрация типов, создание по строке.

1. Класс `ProductFactory`:
   - классовый атрибут `_registry: dict[str, type]`;
   - метод `register(category, cls)`;
   - метод `create(data)` — по `data["category"]` создаёт объект. Если категории нет — `ValueError`.
2. Зарегистрируйте `ElectronicsProduct` и `FurnitureProduct` (из M2) для `"Electronics"` и `"Furniture"`.
3. Создайте список товаров в коде, создайте объекты через фабрику, выведите `get_display_info()`.

---

## Задача M7. Адаптер (medium)

**Цель:** Паттерн Adapter — единый интерфейс.

1. Класс `DictDataSource` — конструктор принимает список dict, метод `fetch()` возвращает его.
2. Класс `TupleToDictAdapter` — конструктор принимает список кортежей `(name, value)`, метод `fetch()` возвращает список dict вида `[{"name": ..., "value": ...}]`.
3. Функция `print_report(source)` — принимает любой объект с `fetch()`, выводит количество записей и первые 2.
4. Вызовите `print_report(DictDataSource([...]))` и `print_report(TupleToDictAdapter([("A", 1), ("B", 2)]))`.

---

## Критерии оценки

### Easy (задачи 1–7)

| Задача | Баллы |
|--------|-------|
| 1 | 10 |
| 2 | 15 |
| 3 | 15 |
| 4 | 20 |
| 5 | 15 |
| 6 | 15 |
| 7 | 20 |

**Easy итого:** 110 баллов

### Medium (задачи M1–M7)

| Задача | Баллы |
|--------|-------|
| M1 | 20 |
| M2 | 25 |
| M3 | 25 |
| M4 | 25 |
| M5 | 25 |
| M6 | 25 |
| M7 | 25 |

**Medium итого:** 170 баллов

---

## Подсказки

**Easy:**
- Приватный атрибут: `self._balance`
- ABC: `class Vehicle(ABC):` и `@abstractmethod` над методом
- Пустой список: `if not self.students: return None`

**Medium:**
- Chain of Responsibility: в `handle()` — если подходит, возвращаете результат; иначе `return self.next_handler.handle(record)`
- Фабрика: `cls = self._registry.get(category)`; `if cls is None: raise ValueError`
