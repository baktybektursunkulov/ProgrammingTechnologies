"""
Pandas Library for Data Handling (Part 1)

- Series и DataFrame: создание, dtype, index, базовая информация
- Чтение/запись: CSV (на примере временного файла в папке урока)
- Индексация и выборка: [], loc, iloc
- Фильтрация и присваивания (в т.ч. по условию)
- Группировки: groupby + agg
- Объединения: concat и merge
- Пропуски: isna / fillna / dropna
"""

from __future__ import annotations

from pathlib import Path


try:
    import pandas as pd
except ImportError as e:  # pragma: no cover
    raise SystemExit(
        "Не найден пакет pandas. Установите его командой: pip install pandas"
    ) from e


def series_and_dataframe_basics() -> None:
    print("--- Series и DataFrame ---")

    s = pd.Series([10, 20, 30], name="score")
    print("Series:\n", s)
    print("dtype:", s.dtype, "| name:", s.name, "| index:", list(s.index))

    df = pd.DataFrame(
        {
            "name": ["Аня", "Борис", "Вера", "Глеб"],
            "age": [19, 20, 19, 21],
            "score": [78, 92, 65, 88],
        }
    )
    print("\nDataFrame:\n", df)
    print("\ninfo():")
    df.info()
    print("\ndescribe(include='all'):\n", df.describe(include="all"))


def read_write_csv_example() -> None:
    print("\n--- CSV: write/read ---")
    lesson_dir = Path(__file__).resolve().parent
    csv_path = lesson_dir / "sample_people.csv"

    df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["Ann", "Bob", "Vera"],
            "city": ["Kyiv", "Lviv", "Odesa"],
        }
    )
    df.to_csv(csv_path, index=False)
    print("Сохранили:", csv_path.name)

    df2 = pd.read_csv(csv_path)
    print("Прочитали:\n", df2)


def selection_loc_iloc() -> None:
    print("\n--- Индексация: [], loc, iloc ---")
    df = pd.DataFrame(
        {
            "name": ["Аня", "Борис", "Вера", "Глеб"],
            "age": [19, 20, 19, 21],
            "score": [78, 92, 65, 88],
        }
    )
    print(df)


    print("\nloc по меткам строк/столбцов:")
    print("df.loc['s2', 'score']:", df.loc[1, "score"])
    # print("df.loc[['s1','s3'], ['name','score']]:\n", df.loc[["s1", "s3"], ["name", "score"]])

    print("\niloc по позициям:")
    print("df.iloc[1, 2]:", df.iloc[1, 2])
    print("df.iloc[0:2, 0:2]:\n", df.iloc[1:3, 0:2])


def filtering_and_assignment() -> None:
    print("\n--- Фильтрация и присваивание ---")
    df = pd.DataFrame(
        {
            "name": ["Аня", "Борис", "Вера", "Глеб"],
            "age": [19, 20, 19, 21],
            "score": [78, 92, 65, 88],
        }
    )

    high = df[df["score"] >= 85]
    print("score >= 85:\n", high)

    df = df.copy()
    df["passed"] = df["score"] >= 70
    df.loc[df["score"] < 70, "passed"] = False
    df.loc[df["score"] >= 90, "grade"] = "A"
    df.loc[(df["score"] >= 80) & (df["score"] < 90), "grade"] = "B"
    df.loc[df["score"] < 80, "grade"] = "C"
    print("\nДобавили столбцы passed/grade:\n", df)


def groupby_agg_example() -> None:
    print("\n--- groupby + agg ---")
    df = pd.DataFrame(
        {
            "student": ["Аня", "Аня", "Борис", "Борис", "Вера"],
            "subject": ["Math", "CS", "Math", "CS", "Math"],
            "score": [90, 95, 70, 85, 88],
        }
    )
    print("Данные:\n", df)

    g = df.groupby("student")["score"].agg(["count", "mean", "min", "max"])
    print("\nАгрегаты по студенту:\n", g)

    pivot_like = df.pivot_table(index="student", columns="subject", values="score", aggfunc="mean")
    print("\nПример pivot_table:\n", pivot_like)


def concat_and_merge_example() -> None:
    print("\n--- concat и merge ---")
    left = pd.DataFrame(
        {"student_id": [1, 2, 3], "name": ["Аня", "Борис", "Вера"]}
    )
    right = pd.DataFrame(
        {"student_id": [1, 2, 4], "group": ["A", "A", "B"]}
    )
    print("left:\n", left)
    print("\nright:\n", right)

    merged = left.merge(right, on="student_id", how="left")
    print("\nmerge how='left':\n", merged)

    top = pd.DataFrame({"x": [1, 2], "y": [10, 20]})
    bottom = pd.DataFrame({"x": [3], "y": [30]})
    stacked = pd.concat([top, bottom], ignore_index=True)
    print("\nconcat по строкам (ignore_index=True):\n", stacked)


def missing_values_example() -> None:
    print("\n--- Пропуски (NaN) ---")
    df = pd.DataFrame(
        {"name": ["A", "B", "C", "D"], "score": [10, None, 30, None]}
    )
    print("Исходные:\n", df)

    print("\nisna():\n", df.isna())
    print("\nfillna(0):\n", df.fillna(0))
    print("\ndropna():\n", df.dropna())

    df2 = df.copy()
    df2["score"] = df2["score"].fillna(df2["score"].mean())
    print("\nЗаполнили средним:\n", df2)


def main() -> None:
    """Точка входа: раскомментируйте нужные демо или вызовите функции вручную."""
    # series_and_dataframe_basics()
    # read_write_csv_example()
    # selection_loc_iloc()
    # filtering_and_assignment()
    # groupby_agg_example()
    # concat_and_merge_example()
    missing_values_example()


if __name__ == "__main__":
    main()

