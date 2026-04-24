"""
- merge(validate=...)
- pivot_table и melt
- to_datetime + dt-аксессоры
- resample
- rolling
- interpolate / ffill / bfill
- pd.cut (векторная категоризация)
- astype('category') и memory_usage
"""

from __future__ import annotations

from time import perf_counter

try:
    import pandas as pd
except ImportError as e:  # pragma: no cover
    raise SystemExit("Не найден пакет pandas. Установите его: pip install pandas") from e


def _require_visualization_packages():
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
    except ImportError as e:  # pragma: no cover
        raise SystemExit(
            "Для визуализаций установите пакеты: pip install matplotlib seaborn"
        ) from e
    return plt, sns

def pivot_and_melt_example() -> None:
    print("\n--- pivot_table <-> melt ---")
    df_long = pd.DataFrame(
        {
            "date": ["2026-04-10", "2026-04-10", "2026-04-11", "2026-04-11", "2026-04-11"],
            "shop": ["S1", "S2", "S1", "S2", "S1"],
            "sales": [10, 7, 3, 8, 4],
        }
    )
    df_long["date"] = pd.to_datetime(df_long["date"])
    print("long:\n", df_long)

    wide = df_long.pivot_table(index="date", columns="shop", values="sales", aggfunc="sum")
    print("\nwide:\n", wide)

    long_back = wide.reset_index().melt(id_vars="date", var_name="shop", value_name="sales")
    print("\nback to long:\n", long_back.sort_values(["date", "shop"]))


def datetime_dt_features_example() -> None:
    print("\n--- to_datetime + .dt ---")
    df = pd.DataFrame(
        {
            "ts": [
                "2026-04-10 10:00",
                "2026-04-10 10:15",
                "2026-04-11 09:00",
                "2026-04-12 21:30",
            ],
            "value": [1, 2, 5, 3],
        }
    )
    df["ts"] = pd.to_datetime(df["ts"])
    df["date"] = df["ts"].dt.date
    df["hour"] = df["ts"].dt.hour
    df["weekday"] = df["ts"].dt.weekday
    df["is_weekend"] = df["weekday"] >= 5
    print(df)


def resample_example() -> None:
    print("\n--- resample ---")
    df = pd.DataFrame(
        {
            "ts": pd.to_datetime(
                [
                    "2026-04-10 10:00",
                    "2026-04-10 11:00",
                    "2026-04-11 09:00",
                    "2026-04-11 10:00",
                ]
            ),
            "value": [1, 3, 10, 20],
        }
    ).set_index("ts")

    daily = df.resample("D").sum(numeric_only=True)
    by_30m = df.resample("30min").mean(numeric_only=True)

    print("daily sum:\n", daily)
    print("\n30min mean:\n", by_30m)


def rolling_example() -> None:
    print("\n--- rolling(window=3) ---")
    df = pd.DataFrame(
        {"date": pd.date_range("2026-04-01", periods=8, freq="D"), "value": [1, 2, 4, 8, 6, 3, 5, 7]}
    ).sort_values("date")

    df["ma3"] = df["value"].rolling(window=2).mean()
    df["std3"] = df["value"].rolling(window=3).std(ddof=0)
    print(df)


def missing_fill_interpolate_example() -> None:
    print("\n--- ffill / bfill / interpolate ---")
    df = pd.DataFrame(
        {"ts": pd.date_range("2026-04-01", periods=8, freq="D"), "value": [1, None, None, 4, None, 10, None, 12]}
    ).set_index("ts")

    print("orig:\n", df)
    print("\nforwordfill:\n", df.ffill())
    print("\nbackgroundfill:\n", df.bfill())
    print("\ninterpolate:\n", df.interpolate())


def cut_vectorized_grade_example() -> None:
    print("\n--- pd.cut: grade без apply ---")
    df = pd.DataFrame({"score": [45, 67, 72, 81, 90, 100]})
    bins = [-float("inf"), 70, 80, 90, float("inf")]
    labels = ["F", "C", "B", "A"]
    df["grade"] = pd.cut(df["score"], bins=bins, labels=labels, right=False)
    print(df)


def matplotlib_lineplot_example() -> None:
    print("\n--- matplotlib: line plot ---")
    plt, _ = _require_visualization_packages()
    df = pd.DataFrame(
        {
            "date": pd.date_range("2026-04-01", periods=10, freq="D"),
            "sales": [12, 15, 14, 18, 22, 19, 24, 26, 25, 28],
        }
    )
    df["ma3"] = df["sales"].rolling(window=3).mean()

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(df["date"], df["sales"], marker="o", label="sales")
    ax.plot(df["date"], df["ma3"], linestyle="--", label="ma3")
    ax.set_title("Daily sales and moving average")
    ax.set_xlabel("date")
    ax.set_ylabel("sales")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    plt.show()


def seaborn_barplot_example() -> None:
    print("\n--- seaborn: barplot ---")
    plt, sns = _require_visualization_packages()
    df = pd.DataFrame(
        {
            "subject": ["Math", "Math", "CS", "CS", "Physics", "Physics"],
            "score": [82, 91, 88, 95, 76, 84],
        }
    )
    agg = df.groupby("subject", as_index=False)["score"].mean()

    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(data=agg, x="subject", y="score", hue="subject", legend=False, ax=ax)
    ax.set_title("Mean score by subject")
    ax.set_xlabel("subject")
    ax.set_ylabel("mean score")
    ax.set_ylim(0, 100)
    fig.tight_layout()
    plt.show()


def seaborn_heatmap_example() -> None:
    print("\n--- seaborn: correlation heatmap ---")
    plt, sns = _require_visualization_packages()
    df = pd.DataFrame(
        {
            "math": [70, 85, 90, 60, 75, 88, 92],
            "physics": [68, 80, 89, 62, 70, 90, 95],
            "cs": [72, 86, 94, 58, 77, 91, 97],
            "english": [65, 78, 84, 70, 74, 83, 88],
        }
    )
    corr = df.corr(numeric_only=True)

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="Blues", vmin=-1, vmax=1, ax=ax)
    ax.set_title("Feature correlation")
    fig.tight_layout()
    plt.show()

#
# def category_memory_example() -> None:
#     print("\n--- astype('category') + memory_usage ---")
#     n = 20_000
#     df = pd.DataFrame(
#         {
#             "city": (["Kyiv", "Lviv", "Odesa", "Dnipro", "Kharkiv"] * (n // 5)),
#             "value": range(n),
#         }
#     )
#     before = int(df.memory_usage(deep=True).sum())
#     df["city"] = df["city"].astype("category")
#     after = int(df.memory_usage(deep=True).sum())
#     print("memory before:", before, "bytes")
#     print("memory after :", after, "bytes")
#     print("saved        :", before - after, "bytes")
# def apply_vs_vectorized_micro_example() -> None:
#     print("\n--- apply vs vectorized (очень кратко) ---")
#     df = pd.DataFrame({"score": list(range(100_000))})
#
#     t0 = perf_counter()
#     _ = df["score"].apply(lambda x: "A" if x >= 90_000 else "B")
#     t1 = perf_counter()
#
#     t2 = perf_counter()
#     _ = pd.Series(["B"] * len(df)).where(df["score"] < 90_000, "A")
#     t3 = perf_counter()
#
#     print("apply seconds     :", round(t1 - t0, 4))
#     print("vectorized seconds:", round(t3 - t2, 4))
#

def main() -> None:
    # pivot_and_melt_example()
    # datetime_dt_features_example()
    # resample_example()
    # rolling_example()
    missing_fill_interpolate_example()
    # cut_vectorized_grade_example()
    # matplotlib_lineplot_example()
    # seaborn_barplot_example()
    # seaborn_heatmap_example()
    # category_memory_example()
    # apply_vs_vectorized_micro_example()


if __name__ == "__main__":
    main()

