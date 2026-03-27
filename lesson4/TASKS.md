# Задачи: Итераторы, Comprehensions и работа с JSON/XLSX

**Уровень:** Middle  
**Темы:** Итераторы, List/Dict/Set comprehensions, чтение и запись JSON, чтение и запись XLSX (openpyxl)

---

## Подготовка

```bash
pip install openpyxl
```

Создайте файл `sales.xlsx` (если его нет):
```bash
python lesson5/create_sample_data.py
```

Используйте файлы из папки `lesson5/sample_data/`:
- `students.json` — список студентов
- `products.json` — каталог товаров  
- `sales.xlsx` — таблица продаж

---

## Задача 1. JSON → Comprehensions → JSON (базовый mid)

**Цель:** Прочитать JSON, преобразовать через comprehensions, записать результат.

1. Загрузите `students.json` (список словарей с полями: `name`, `age`, `grade`, `city`).
2. С помощью **list comprehension** создайте список имён студентов младше 22 лет.
3. С помощью **dict comprehension** создайте словарь `{name: grade}` только для студентов из города "Astana".
4. Сохраните оба результата в новый JSON-файл `filtered_students.json` в формате:
   ```json
   {
     "young_students": ["...", "..."],
     "astana_grades": {"name": grade, ...}
   }
   ```

---

## Задача 2. Итератор по строкам JSON-файла (mid)

**Цель:** Реализовать кастомный итератор для построчного чтения JSON Lines (JSONL).

1. Создайте класс `JsonLinesIterator`, который:
   - принимает путь к `.jsonl` файлу в конструкторе;
   - реализует `__iter__` и `__next__`;
   - при каждом вызове `next()` возвращает следующий распарсенный объект (словарь);
   - при достижении конца файла выбрасывает `StopIteration`.
2. Создайте тестовый файл `logs.jsonl` с 3–5 строками JSON (каждая строка — отдельный объект).
3. Используйте итератор в цикле `for` и выведите все записи.

---

## Задача 3. XLSX → Comprehensions → JSON (mid)

**Цель:** Прочитать Excel, обработать через comprehensions, записать в JSON.

1. Загрузите `sales.xlsx` (лист с колонками: `product`, `quantity`, `price`, `date`).
2. Используя `iter_rows()` или чтение через openpyxl, получите данные в виде списка словарей.
3. С помощью **list comprehension** отфильтруйте продажи с `quantity >= 15`.
4. С помощью **dict comprehension** постройте словарь `{product: total_quantity}`, где `total_quantity` — суммарное количество проданных единиц по каждому продукту (суммируйте, если продукт встречается несколько раз).
5. Сохраните результат в `sales_summary.json` в формате:
   ```json
   {
     "large_orders": [...],
     "quantity_by_product": {"product": total_quantity, ...}
   }
   ```

---

## Задача 4. JSON + Set comprehension + XLSX (mid)

**Цель:** Дедупликация и экспорт в Excel.

1. Загрузите `products.json` (список товаров с полями: `id`, `name`, `category`, `price`).
2. С помощью **set comprehension** получите множество уникальных категорий.
3. Для каждой категории с помощью **list comprehension** соберите список товаров с ценой выше 1000.
4. Создайте новый XLSX-файл `products_by_category.xlsx`:
   - первый лист: все уникальные категории в колонке A;
   - второй лист: товары дороже 1000 с колонками `name`, `category`, `price`.

---

## Задача 5. Генератор + JSON (mid+)

**Цель:** Ленивая загрузка больших JSON-массивов.

1. Напишите **генератор** `read_json_chunks(file_path, chunk_size=5)`, который:
   - загружает JSON-файл (массив объектов);
   - возвращает по `chunk_size` элементов за раз через `yield`.
2. Используйте его для `students.json`: обрабатывайте по 2 студента за итерацию и выводите их имена.
3. *Дополнительно:* объедините с **dict comprehension** — для каждого чанка создайте словарь `{name: grade}` и выведите.

---

## Задача 6. Комплексная: JSON ↔ XLSX с итераторами (mid+)

**Цель:** Конвертация между форматами с использованием итераторов.

1. Прочитайте `students.json`.
2. Реализуйте функцию `students_to_xlsx(students, output_path)`:
   - используйте `enumerate()` для нумерации строк;
   - используйте `zip()` для сопоставления заголовков и значений при записи;
   - создайте XLSX с колонками: `№`, `name`, `age`, `grade`, `city`.
3. Реализуйте функцию `xlsx_to_students(input_path)`:
   - используйте `iter_rows()` как итератор по строкам;
   - пропустите заголовок;
   - верните список словарей (как исходный JSON).
4. Проверьте цикл: JSON → XLSX → JSON, сравните исходные и финальные данные.

---

## Задача 7. Обработка вложенных структур (mid)

**Цель:** Comprehensions с вложенными структурами JSON.

1. Загрузите `products.json` (если есть вложенные объекты, например `specs` или `tags` — используйте их).
2. С помощью **вложенного list comprehension** извлеките все уникальные теги/значения из вложенных структур.
3. Используйте **set comprehension** для дедупликации.
4. Сохраните результат в `extracted_tags.json` как список.

*Если в данных нет вложенности — добавьте поле `tags: ["a", "b"]` к части товаров и работайте с ним.*

---

## Критерии оценки (ориентир)

| Задача | Баллы | Ключевые навыки |
|--------|-------|-----------------|
| 1 | 15 | list/dict comprehension, json.load/dump |
| 2 | 20 | кастомный итератор, __iter__, __next__ |
| 3 | 20 | openpyxl, iter_rows, comprehensions |
| 4 | 15 | set comprehension, запись XLSX |
| 5 | 15 | генератор, yield, json |
| 6 | 25 | enumerate, zip, полный цикл JSON↔XLSX |
| 7 | 15 | вложенные comprehensions |

**Итого:** 125 баллов (можно масштабировать под свою систему).

---

## Подсказки

- Для JSON: `json.load()`, `json.dump(obj, f, indent=2, ensure_ascii=False)`
- Для XLSX: `from openpyxl import Workbook, load_workbook`
- `iter_rows(min_row=2, values_only=True)` — итератор по строкам без заголовка
- При работе с файлами используйте `with open(...) as f` для автоматического закрытия
