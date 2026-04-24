# Задачи: FastAPI — основы REST API (часть 1)

**Уровень:** Beginner  
**Темы:** создание FastAPI-приложения, маршруты `GET/POST/PUT/DELETE`, `path/query` параметры, модели `Pydantic`, коды ответов, обработка ошибок `HTTPException`

---

## Задача 1. Первый endpoint: `GET /health`

**Цель:** поднять минимальный API и проверить, что сервер отвечает.

1. Установите зависимости: `pip install fastapi uvicorn`.
2. Создайте файл `main.py` и объект `app = FastAPI()`.
3. Добавьте endpoint `GET /health`, который возвращает JSON:
   `{"status": "ok"}`.
4. Запустите сервер:
   `uvicorn main:app --reload`.
5. Проверьте endpoint в браузере или через Swagger (`/docs`).

---

## Задача 2. `GET` c query-параметрами

**Цель:** принимать параметры запроса и фильтровать данные.

1. Создайте in-memory список товаров (например, `id`, `name`, `price`, `in_stock`).
2. Реализуйте `GET /items`.
3. Добавьте query-параметры:
   - `limit` (по умолчанию 10),
   - `min_price` (опционально).
4. Верните только первые `limit` элементов после фильтра по `min_price`.

**Подсказка:** сигнатура может выглядеть так:
`def list_items(limit: int = 10, min_price: float | None = None)`.

---

## Задача 3. `GET /items/{item_id}` и ошибки 404

**Цель:** работа с path-параметрами и обработка отсутствующих данных.

1. Реализуйте endpoint `GET /items/{item_id}`.
2. Найдите товар по `id` в вашем списке.
3. Если товар не найден, выбросьте `HTTPException(status_code=404, detail="Item not found")`.
4. Если найден — верните JSON товара.

---

## Задача 4. `POST /items` + Pydantic-модель

**Цель:** принимать и валидировать тело запроса.

1. Создайте модель `ItemCreate` (`name`, `price`, `in_stock`).
2. Реализуйте `POST /items`:
   - принимает `ItemCreate`,
   - создаёт новый `id`,
   - добавляет товар в in-memory коллекцию.
3. Возвращайте созданный объект и код `201`.

**Подсказка:** используйте `@app.post("/items", status_code=201)`.

---

## Задача 5. `PUT /items/{item_id}`

**Цель:** полное обновление ресурса.

1. Реализуйте `PUT /items/{item_id}`.
2. Принимаем ту же модель `ItemCreate` (или отдельную `ItemUpdate`).
3. Если `item_id` не найден — 404.
4. Если найден — полностью перезапишите поля товара и верните обновлённый объект.

---

## Задача 6. `DELETE /items/{item_id}`

**Цель:** удаление ресурса.

1. Реализуйте endpoint `DELETE /items/{item_id}`.
2. Если запись есть — удалите её и верните:
   `{"message": "deleted"}`.
3. Если записи нет — верните 404.

---

## Задача 7. Мини-практика: Users API

**Цель:** закрепить CRUD на второй сущности.

1. Создайте вторую сущность `User` (`id`, `name`, `email`, `is_active`).
2. Реализуйте endpoints:
   - `GET /users`
   - `GET /users/{user_id}`
   - `POST /users`
   - `DELETE /users/{user_id}`
3. Для `POST` добавьте валидацию email через `EmailStr`.

---

## Задача 8. Проверка API через `/docs`

**Цель:** использовать автодокументацию FastAPI.

1. Откройте Swagger UI: `http://127.0.0.1:8000/docs`.
2. Протестируйте все endpoints из задач 1–7.
3. Убедитесь, что:
   - 200/201 возвращаются в успешных сценариях;
   - 404 возвращается при несуществующих id;
   - валидация тела запроса работает.

---

## Домашний мини-челлендж (по желанию)

- Добавьте endpoint `PATCH /items/{item_id}` для частичного обновления.
- Добавьте сортировку в `GET /items` по цене (`sort=asc|desc`).
- Добавьте endpoint `GET /stats`, который возвращает:
  - количество товаров,
  - среднюю цену,
  - число товаров `in_stock=True`.

---

## Дополнительно: графики через FastAPI (GET/POST -> PNG)

**Цель:** возвращать изображения графиков по HTTP-запросу.

1. Создайте отдельный модуль API для графиков (например, `fastapi_plot_examples.py`).
2. Реализуйте `GET /plots/line`:
   - принимает query-параметр `points`,
   - возвращает PNG графика (через `StreamingResponse`).
3. Реализуйте `GET /plots/hist`:
   - принимает `bins`,
   - возвращает PNG-гистограмму.
4. Реализуйте `POST /plots/bar`:
   - принимает JSON с `labels` и `values`,
   - возвращает PNG `barplot` (`seaborn`).
5. Реализуйте `POST /plots/heatmap`:
   - принимает 2D-матрицу чисел в JSON,
   - строит `heatmap` корреляций и возвращает PNG.

**Пример запуска:**

- `uvicorn lesson10.fastapi_plot_examples:app --reload`

**Примеры запросов:**

- `GET http://127.0.0.1:8000/plots/line?points=60`
- `GET http://127.0.0.1:8000/plots/hist?bins=8`
- `POST http://127.0.0.1:8000/plots/bar` с JSON:
  `{"labels":["A","B","C"],"values":[10,7,14],"title":"Demo bar"}`

**Вариант с `FileResponse` (сохранение в `lesson10/plots/`):**

- `GET http://127.0.0.1:8000/plots/file/line?points=60`
- `GET http://127.0.0.1:8000/plots/file/hist?bins=8`
- `POST http://127.0.0.1:8000/plots/file/bar` с тем же JSON
- `POST http://127.0.0.1:8000/plots/file/heatmap` с матрицей в JSON

