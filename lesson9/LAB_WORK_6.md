# Лабораторная работа: Matplotlib/Seaborn и объектно-ориентированное программирование

## Требования к программной среде

- Python 3.10+
- Пакеты: `matplotlib`, `seaborn`, `pandas`
- Установка: `pip install matplotlib seaborn pandas`

---

## Задание 1. Класс-настройка графика
1. Создайте класс `PlotConfig`:
   - `figsize: tuple[int, int]`
   - `title: str`
   - `x_label: str`
   - `y_label: str`
   - `style: str | None`
2. Реализуйте метод `apply(ax)`, который применяет заголовок, подписи осей и сетку.
3. Если задан `style`, применяйте его перед построением графика.

---

## Задание 2. Базовый абстрактный класс графика
1. Создайте `BasePlot` (`abc.ABC`) с полями:
   - `config: PlotConfig`
   - `output_dir: Path`
2. Абстрактный метод `draw(self) -> plt.Figure`.
3. Общий метод `save(self, filename: str) -> Path`, который:
   - вызывает `draw()`,
   - сохраняет `png`,
   - закрывает фигуру.

---

## Задание 3. Наследование: графики Matplotlib
1. Реализуйте минимум 3 класса-наследника `BasePlot`:
   - `LinePlot`
   - `BarPlot`
   - `HistogramPlot`
2. В каждом классе храните входные данные в атрибутах экземпляра.
3. Метод `draw()` должен:
   - создавать `figure/axes`,
   - строить соответствующий график,
   - применять `config.apply(ax)`.

---

## Задание 4. Seaborn-обёртка
1. Создайте класс `SeabornPlotFactory`.
2. Реализуйте методы:
   - `barplot(df, x, y, config) -> Figure`
   - `heatmap(df, config, annot=True) -> Figure`
3. Добавьте проверку входных данных (пустой DataFrame, отсутствие столбца и т.д.) с понятными `ValueError`.

---

## Задание 5. Репозиторий данных
1. Создайте класс `CsvDataRepository`.
2. Методы:
   - `load(path) -> pd.DataFrame`
   - `load_required(path, required_columns) -> pd.DataFrame`
3. При отсутствии файла/колонок выбрасывайте понятные исключения.

---

## Задание 6. Композиция: сервис отчёта
1. Создайте класс `VisualizationReportService`.
2. В конструктор передайте:
   - `CsvDataRepository`
   - `SeabornPlotFactory`
   - `output_dir`
3. Реализуйте метод `build_student_report(df) -> dict[str, Path]`, который сохраняет:
   - line по динамике оценок/продаж,
   - bar по средним значениям,
   - heatmap корреляций числовых признаков.

---

## Задание 7. Полиморфный pipeline графиков
1. Реализуйте класс `PlotPipeline`:
   - принимает список объектов `BasePlot`,
   - метод `run_all() -> list[Path]` сохраняет все графики по порядку.
2. Метод `describe()` возвращает названия классов графиков.

---