"""
Basics of NumPy: Arrays and Vectorized Computations (Part 1)

- ndarray: создание, shape, dtype
- Индексирование и срезы (views)
- Векторизованные арифметические операции и ufunc
- Базовое вещание (broadcasting)

Дополнительно (перекликается с TASKS_MIDDLE.md): view vs fancy index,
np.where / np.clip, meshgrid, vstack/hstack, argsort, z-score по столбцам,
норма и матрица квадратов расстояний через @.
"""
from datetime import datetime

import numpy as np


def list_vs_numpy_speed_concept():
    """Идея разницы между списком Python и массивом NumPy.

    Списки обрабатываются в интерпретаторе поэлементно; ``ndarray`` хранит
    данные непрерывно и операции выполняются скомпилированным кодом (быстрее
    на больших объёмах). Демонстрируется создание массива из списка и ``dtype``.
    """
    print("--- List vs NumPy (идея) ---")
    py_list = [1, 2, 3, 4, 5]
    arr = np.array(py_list)
    print("list:", py_list, "| ndarray:", arr, "| dtype:", arr.dtype)
def creating_arrays():
    """Создание массивов: константы, диапазоны, равномерная сетка по отрезку.

    Показывает ``np.array``, ``zeros``, ``ones``, ``arange``, ``linspace``.
    """
    print("\n--- Создание массивов ---")
    print("np.array([1, 2, 3]):", np.array([1, 2, 3]))
    print("np.zeros(4):", np.zeros(4))
    print("np.ones((2, 3)):\n ", np.random.random((2, 3)))

    print("np.arange(0, 10, 2):", np.arange(0, 10, 2))
    print("np.linspace(0, 1, 5):", np.linspace(0, 1, 9))
def shape_dtype():
    """Размерность массива и тип элементов.

    Иллюстрирует атрибуты ``shape``, ``ndim``, ``size``, ``dtype`` и явное
    задание ``dtype`` при создании массива.
    """
    print("\n--- shape, ndim, dtype ---")
    a = np.array([[1.0, 2, 3], [4, 5, 6]])
    print("a:\n", a)
    print("shape:", a.shape, "| ndim:", a.ndim, "| size:", a.size)
    print("dtype:", a.dtype)
    f = np.array([1, 0, 7, -1], dtype=np.bool)
    print("float array:", f, f.dtype)
def vectorized_ops():
    """Поэлементные операции и ufunc без циклов Python.

    Демонстрирует умножение на скаляр, степень, ``sqrt``, сложение и умножение
    массивов одинаковой формы.
    """
    print("\n--- Векторизованные операции ---")
    x = np.array([1.0, 2.0, 3.0, 4])
    print("x:", x)
    print("x * 2:", x * 2)
    print("x ** 2:", x ** 2)
    print("np.sqrt(x):", np.sqrt(x))
    y = np.array([10, 20, 30, 40])
    print("x + y:", x + y)
    print("x * y:", x * y)
def indexing_slicing():
    """Индексы, срезы и двумерная индексация.

    Одномерные срезы с шагом; матрица ``reshape(3, 4)``; обращение к элементу,
    столбцу и подматрице через срезы (часто это view на те же данные).
    """
    print("\n--- Индексы и срезы ---")
    a = np.arange(10)
    print("a:", a)
    print("a[2:7]:", a[2:7])
    print("a[::2]:", a[::2])

    m = np.arange(12).reshape(3, 4)
    print("m:\n", m)
    print("m[1, 2]:", m[1, 2])
    print("m[:, 0]:", m[:, 0])
    print("m[0:2, 1:3]:\n", m[0:2, 1:3])
def boolean_indexing():
    """Маска из сравнения и выбор элементов по условию.

    Строится булев массив ``a > 0`` и используется для извлечения подмножества
    элементов ``a[mask]``.
    """
    print("\n--- Булево индексирование ---")
    a = np.array([3, -1, 5, 0, 12, -4])
    mask = a > 0
    print("a:", a, "| a > 0:", mask)
    print("a[a > 0]:", a[a > 0])
def broadcasting_basics():
    """Вещание: согласование форм при поэлементных операциях.

    Столбец формы ``(3, 1)`` и вектор ``(3,)`` дают при сложении матрицу ``(3, 3)``:
    меньший массив «растягивается» по недостающим осям.
    """
    print("\n--- Broadcasting (базово) ---")
    a = np.array([[1], [2], [3]])  # shape (3, 1)
    b = np.array([10, 20, 30])  # shape (3,)
    print("a:\n", a)
    print("b:", b)
    print("a + b:\n", a + b)
def aggregate_along_axis():
    """Суммирование по всему массиву и вдоль оси ``axis``.

    ``axis=0`` — агрегирование по строкам (вдоль столбцов), ``axis=1`` — по столбцам
    вдоль строк.
    """
    print("\n--- Агрегаты по осям ---")
    m = np.array([[1, 2, 3], [4, 5, 6]])
    print("m:\n", m)
    print("sum всего:", m.sum())
    print("sum axis=0 (по столбцам):", m.sum(axis=0))
    print("sum axis=1 (по строкам):", m.sum(axis=1))


def where_and_clip():
    """Условная подстановка и ограничение значений по диапазону.
    ``np.where(условие, если_да, если_нет)`` — без циклов по элементам.
    ``np.clip(a, min, max)`` приводит каждый элемент к отрезку ``[min, max]``.
    Используется генератор ``np.random.default_rng`` и ``standard_normal``.
    """
    print("\n--- np.where и np.clip ---")
    x = np.linspace(-2, 2, 9)
    y = np.where(x < 0, 0, x)
    print("x:", x)
    print("np.where(x < 0, 0, x):", y)

    rng = np.random.default_rng(42)
    v = rng.standard_normal(8)
    w = np.clip(v, -1.0, 1.0)
    print("v:", np.round(v, 3))
    print("np.clip(v, -1.0, 1.0):", np.round(w, 3))


def meshgrid_example():
    """Декартова сетка координат и поиск минимума на сетке.
    ``meshgrid`` строит матрицы ``X``, ``Y`` одинаковой формы для формул вида
    ``Z = f(X, Y)``. ``np.argmin`` возвращает плоский индекс минимального элемента.
    """
    print("\n--- meshgrid и argmin ---")
    X, Y = np.meshgrid(np.linspace(0, 1, 4), np.linspace(0, 1, 3), indexing="xy")
    Z = X ** 2 + Y ** 2
    print("Z = X**2 + Y**2:\n", Z)
    print("argmin (плоский индекс):", np.argmin(Z), "| min:", Z.flat[np.argmin(Z)])


def stack_arrays():
    """Вертикальная и горизонтальная склейка двумерных массивов.
    ``np.vstack`` — массивы друг под другом (ось 0); ``np.hstack`` — слева направо
    (ось 1) при согласованных остальных размерах.
    """
    print("\n--- vstack / hstack ---")
    A = np.ones((2, 3))
    B = np.zeros((2, 3))
    print("vstack:\n", np.vstack([A, B]))
    print("hstack:\n", np.hstack([A, B]))


def argsort_example():
    """Сортировка индексов и перестановка связанных данных.
    ``argsort()`` даёт порядок по возрастанию; срез ``[::-1]`` — по убыванию.
    Индексы применяются к массиву имён, чтобы вывести их в порядке оценок.
    """
    print("\n--- argsort: порядок по убыванию оценок ---")
    scores = np.array([78, 92, 65, 88])
    names = np.array(["Аня", "Борис", "Вера", "Глеб"])
    idx = scores.argsort()[::-1]
    print("оценки:", scores)
    print("имена от лучшей к худшей:", names[idx])


def column_zscore():
    """Z-score по каждому столбцу: вычитание среднего и деление на СКО.
    ``mean`` и ``std`` с ``axis=0`` дают векторы длины числа столбцов; вещание
    вычитает и делит каждый столбец на свои ``mu`` и ``sigma``. После нормализации
    среднее по столбцам ~0, СКО ~1 (с учётом погрешности float).
    """
    print("\n--- Нормализация столбцов (z-score) ---")
    rng = np.random.default_rng(0)
    D = rng.standard_normal((5, 3))
    mu = D.mean(axis=0)
    sigma = D.std(axis=0, ddof=0)
    D2 = (D - mu) / sigma
    print("mean по столбцам после:", np.round(D2.mean(axis=0), 10))
    print("std по столбцам после:", np.round(D2.std(axis=0, ddof=0), 10))


def distance_and_squared_matrix():
    """Квадрат евклидова расстояния и матрица попарных квадратов расстояний.

    Для двух векторов: ``sum((p-q)**2)`` или ``norm(p-q)**2``. Для строк матрицы
    данных ``X`` формы ``(P, k)`` используется тождество
    ``‖a−b‖² = ‖a‖² + ‖b‖² − 2(a·b)``, реализованное как
    ``r[:,None] + r[None,:] - 2*(X @ X.T)``, где ``r`` — сумма квадратов координат
    по строкам.
    """
    print("\n--- Расстояние и матрица ‖a−b‖² через X @ X.T ---")
    p = np.array([1.0, 2.0])
    q = np.array([4.0, 6.0])
    d2 = ((p - q) ** 2).sum()
    print("квадрат расстояния p-q:", d2, "| norm:", np.linalg.norm(p - q) ** 2)

    rng = np.random.default_rng(7)
    X = rng.standard_normal((4, 3))
    r = (X ** 2).sum(axis=1)
    D2 = r[:, np.newaxis] + r[np.newaxis, :] - 2 * (X @ X.T)
    manual = ((X[0] - X[2]) ** 2).sum()
    print("D2[0,2] == ручной расчёт:", np.isclose(D2[0, 2], manual), "|", D2[0, 2], manual)
    print("диагональ ~ 0:", np.allclose(D2.diagonal(), 0))


def main():
    """Точка входа: раскомментируйте нужные демо или вызовите функции вручную."""
    # list_vs_numpy_speed_concept()
    # creating_arrays()
    # shape_dtype()
    # vectorized_ops()
    # indexing_slicing()
    # boolean_indexing()
    # broadcasting_basics()
    # aggregate_along_axis()
    # where_and_clip()
    # meshgrid_example()
    # stack_arrays()
    # argsort_example()
    # column_zscore()
    # distance_and_squared_matrix()


if __name__ == "__main__":
    t= np.array(['12/10/2025', '12/10/2025', '12/10/2025'], dtype=datetime)

    time  = datetime.now()
    print(t.dtype)

    main()
