"""
Data Visualization with Matplotlib and Seaborn (Part 1):
- line, bar, scatter, hist
- seaborn barplot, heatmap
"""

from __future__ import annotations

try:
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
except ImportError as e:  # pragma: no cover
    raise SystemExit(
        "Не найдены пакеты для визуализации. Установите: pip install matplotlib seaborn pandas"
    ) from e


def line_plot_example() -> None:
    days = [1, 2, 3, 4, 5, 6, 7]
    sales = [12, 15, 14, 18, 22, 19, 24]

    plt.figure(figsize=(8, 4))
    plt.plot(days, sales, marker="o", linestyle="--", color="teal", label="sales")
    plt.title("Sales by day")
    plt.xlabel("day")
    plt.ylabel("sales")
    # plt.grid(False, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


def bar_plot_example() -> None:
    subjects = ["Math", "CS", "Physics"]
    mean_scores = [86, 92, 79]

    plt.figure(figsize=(7, 4))
    plt.bar(subjects, mean_scores, color=["#4c78a8", "#72b7b2", "#f58518"])
    plt.title("Mean score by subject")
    plt.xlabel("subject")
    plt.ylabel("mean score")
    plt.ylim(0, 100)
    # plt.tight_layout()
    plt.show()


def scatter_plot_example() -> None:
    hours_studied = [1, 2, 2, 3, 4, 5, 5, 6]
    score = [55, 62, 64, 70, 78, 85, 83, 91]

    plt.figure(figsize=(7, 4))
    plt.scatter(hours_studied, score, color="purple")
    plt.title("Hours studied vs score")
    plt.xlabel("hours_studied")
    plt.ylabel("score")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def histogram_example() -> None:
    scores = [52, 60, 61, 65, 68, 70, 72, 73, 75, 77, 78, 80, 82, 84, 85, 88, 90, 91, 94, 97]

    plt.figure(figsize=(7, 4))
    plt.hist(scores, bins=6, color="steelblue", edgecolor="black", alpha=0.85)
    plt.title("Score distribution")
    plt.xlabel("score")
    plt.ylabel("count")
    plt.tight_layout()
    plt.show()


def seaborn_barplot_example() -> None:
    df = pd.DataFrame(
        {
            "subject": ["Math", "Math", "CS", "CS", "Physics", "Physics"],
            "score": [82, 91, 88, 95, 76, 84],
        }
    )
    agg = df.groupby("subject", as_index=False)["score"].mean()

    plt.figure(figsize=(7, 4))
    sns.barplot(data=agg, x="subject", y="score", hue="subject", legend=False)
    plt.title("Mean score by subject (Seaborn)")
    plt.xlabel("subject")
    plt.ylabel("mean score")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()


def seaborn_heatmap_example() -> None:
    df = pd.DataFrame(
        {
            "math": [70, 85, 90, 60, 75, 88, 92],
            "physics": [68, 80, 89, 62, 70, 90, 95],
            "cs": [72, 86, 94, 58, 77, 91, 97],
            "english": [65, 78, 84, 70, 74, 83, 88],
        }
    )
    corr = df.corr(numeric_only=True)

    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="Blues", vmin=-1, vmax=1)
    plt.title("Correlation heatmap")
    plt.tight_layout()
    plt.show()


def main() -> None:
    # line_plot_example()
    # bar_plot_example()
    # scatter_plot_example()
    # histogram_example()
    # seaborn_barplot_example()
    seaborn_heatmap_example()


if __name__ == "__main__":
    main()

