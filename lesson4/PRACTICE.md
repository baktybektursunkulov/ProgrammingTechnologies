# Задачи: Итераторы, Comprehensions и работа с JSON/XLSX

**Уровень:** Middle  
**Темы:** Итераторы, List/Dict/Set comprehensions, чтение и запись JSON, чтение и запись XLSX (openpyxl)

---

## Подготовка

```bash
pip install openpyxl
```

Используйте файлы из папки `lesson4/sample_data/`:
- `students.json` — список студентов
- `products.json` — каталог товаров  
- `sales.xlsx` — таблица продаж

---

## Задача 1. JSON → Comprehensions → JSON (базовый mid)

**Цель:** Прочитать JSON, преобразовать через comprehensions, записать результат.

1. Загрузите `students.json` (список словарей с полями: `name`, `age`, `grade`, `city`).
2. С помощью **list comprehension** создайте список имён студентов с оценкой выше 80.
3. С помощью **dict comprehension** создайте словарь `{name: age}` только для студентов из города "Almaty".
4. Сохраните оба результата в новый JSON-файл `filtered_students.json` в формате:
   ```json
   {
     "top_students": ["...", "..."],
     "almaty_ages": {"name": age, ...}
   }
   ```

---

## Задача 3. XLSX → Comprehensions → JSON (mid)

**Цель:** Прочитать Excel, обработать через comprehensions, записать в JSON.

1. Загрузите `sales.xlsx` (лист с колонками: `product`, `quantity`, `price`, `date`).
2. Используя `iter_rows()` или чтение через openpyxl, получите данные в виде списка словарей.
3. С помощью **list comprehension** отфильтруйте продажи с `quantity > 10`.
4. С помощью **dict comprehension** постройте словарь `{product: total_revenue}`, где `total_revenue = quantity * price` для каждого продукта (суммируйте, если продукт встречается несколько раз).
5. Сохраните результат в `sales_summary.json`.

---