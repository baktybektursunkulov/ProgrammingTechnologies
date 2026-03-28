"""
Basics of NumPy: Arrays and Vectorized Computations (Part 1)

- ndarray: создание, shape, dtype
- Индексирование и срезы (views)
- Векторизованные арифметические операции и ufunc
- Базовое вещание (broadcasting)
"""

import numpy as np

def list_vs_numpy_speed_concept():
    """Списки Python — циклы в интерпретаторе; NumPy — компактные массивы и C-код."""
    print("--- List vs NumPy (идея) ---")
    py_list = [1, 2, 3, 4, 5]
    arr = np.array(py_list)
    print("list:", py_list, "| ndarray:", arr, "| dtype:", arr.dtype)

def creating_arrays():
    print("\n--- Создание массивов ---")
    print("np.array([1, 2, 3]):", np.array([1, 2, 3]))
    print("np.zeros(4):", np.zeros(4))
    print("np.ones((2, 3)):\n ", np.random.random((2, 3)))

    print("np.arange(0, 10, 2):", np.arange(0, 10, 2))
    print("np.linspace(0, 1, 5):", np.linspace(0, 1, 9))

def shape_dtype():
    print("\n--- shape, ndim, dtype ---")
    a = np.array([[1.0, 2, 3], [4, 5, 6]])
    print("a:\n", a)
    print("shape:", a.shape, "| ndim:", a.ndim, "| size:", a.size)
    print("dtype:", a.dtype)
    f = np.array([1,0,7,-1], dtype=np.bool)
    print("float array:", f, f.dtype)

def vectorized_ops():
    print("\n--- Векторизованные операции ---")
    x = np.array([1.0, 2.0, 3.0,4])
    print("x:", x)
    print("x * 2:", x * 2)
    print("x ** 2:", x ** 2)
    print("np.sqrt(x):", np.sqrt(x))
    y = np.array([10, 20, 30, 40])
    print("x + y:", x + y)
    print("x * y:", x * y)


def indexing_slicing():
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
    print("\n--- Булево индексирование ---")
    a = np.array([3, -1, 5, 0, 12, -4])
    mask = a > 0
    print("a:", a, "| a > 0:", mask)
    print("a[a > 0]:", a[a > 0])


def broadcasting_basics():
    print("\n--- Broadcasting (базово) ---")
    a = np.array([[1], [2], [3]])  # shape (3, 1)
    b = np.array([10, 20, 30])  # shape (3,)
    print("a:\n", a)
    print("b:", b)
    print("a + b:\n", a + b)


def aggregate_along_axis():
    print("\n--- Агрегаты по осям ---")
    m = np.array([[1, 2, 3], [4, 5, 6]])
    print("m:\n", m)
    print("sum всего:", m.sum())
    print("sum axis=0 (по столбцам):", m.sum(axis=0))
    print("sum axis=1 (по строкам):", m.sum(axis=1))


def main():
    # list_vs_numpy_speed_concept()
    # creating_arrays()
    # shape_dtype()
    # vectorized_ops()
    # indexing_slicing()
    # boolean_indexing()
    # broadcasting_basics()
    aggregate_along_axis()


if __name__ == "__main__":
    main()
