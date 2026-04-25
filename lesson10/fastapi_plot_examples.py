"""
FastAPI + Matplotlib/Seaborn examples:
- GET endpoints returning PNG plots
- POST endpoints building plots from JSON payload
"""

from __future__ import annotations

from io import BytesIO
from math import sin
from pathlib import Path

import matplotlib
import pandas as pd
import seaborn as sns
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field

# Use a non-interactive backend for server environments.
matplotlib.use("Agg")
import matplotlib.pyplot as plt


app = FastAPI(title="Lesson 10: FastAPI plot examples")
PLOTS_DIR = Path(__file__).resolve().parent / "plots"
PLOTS_DIR.mkdir(exist_ok=True)


class BarPlotRequest(BaseModel):
    labels: list[str] = Field(min_length=1)
    values: list[float] = Field(min_length=1)
    title: str = "Bar chart from POST payload"


class HeatmapRequest(BaseModel):
    matrix: list[list[float]] = Field(min_length=2)
    labels: list[str] | None = None
    title: str = "Correlation-like heatmap"


def _figure_to_png_response(fig: plt.Figure) -> StreamingResponse:
    buffer = BytesIO()
    fig.tight_layout()
    fig.savefig(buffer, format="png", dpi=120)
    plt.close(fig)
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")


def _save_figure(fig: plt.Figure, filename: str) -> Path:
    filepath = PLOTS_DIR / filename
    fig.tight_layout()
    fig.savefig(filepath, format="png", dpi=120)
    plt.close(fig)
    return filepath


@app.get("/plots/line")
def line_plot(points: int = Query(default=40, ge=10, le=500)) -> StreamingResponse:
    x_values = list(range(points))
    y_values = [sin(i / 5) + (i / points) for i in x_values]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_values, y_values, marker="o", markersize=3, linewidth=1.5, label="signal")
    ax.set_title("GET /plots/line")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(alpha=0.3)
    ax.legend()
    return _figure_to_png_response(fig)


@app.get("/plots/file/line")
def line_plot_file(points: int = Query(default=40, ge=10, le=500)) -> FileResponse:
    x_values = list(range(points))
    y_values = [sin(i / 5) + (i / points) for i in x_values]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_values, y_values, marker="o", markersize=3, linewidth=1.5, label="signal")
    ax.set_title("GET /plots/file/line")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(alpha=0.3)
    ax.legend()
    filepath = _save_figure(fig, "line_plot.png")
    return FileResponse(path=filepath, media_type="image/png", filename=filepath.name)


@app.get("/plots/hist")
def hist_plot(bins: int = Query(default=10, ge=3, le=30)) -> StreamingResponse:
    values = [55, 60, 61, 65, 68, 70, 72, 73, 75, 77, 78, 80, 82, 84, 85, 88, 90, 91, 94, 97]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(values, bins=bins, color="steelblue", edgecolor="black", alpha=0.85)
    ax.set_title("GET /plots/hist")
    ax.set_xlabel("score")
    ax.set_ylabel("count")
    return _figure_to_png_response(fig)


@app.get("/plots/file/hist")
def hist_plot_file(bins: int = Query(default=10, ge=3, le=30)) -> FileResponse:
    values = [55, 60, 61, 65, 68, 70, 72, 73, 75, 77, 78, 80, 82, 84, 85, 88, 90, 91, 94, 97]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(values, bins=bins, color="steelblue", edgecolor="black", alpha=0.85)
    ax.set_title("GET /plots/file/hist")
    ax.set_xlabel("score")
    ax.set_ylabel("count")
    filepath = _save_figure(fig, "hist_plot.png")
    return FileResponse(path=filepath, media_type="image/png", filename=filepath.name)


@app.post("/plots/bar")
def bar_plot(payload: BarPlotRequest) -> StreamingResponse:
    if len(payload.labels) != len(payload.values):
        raise HTTPException(status_code=400, detail="labels and values must have same length")

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=payload.labels, y=payload.values, hue=payload.labels, legend=False, ax=ax)
    ax.set_title(payload.title)
    ax.set_xlabel("category")
    ax.set_ylabel("value")
    return _figure_to_png_response(fig)


@app.post("/plots/file/bar")
def bar_plot_file(payload: BarPlotRequest) -> FileResponse:
    if len(payload.labels) != len(payload.values):
        raise HTTPException(status_code=400, detail="labels and values must have same length")

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=payload.labels, y=payload.values, hue=payload.labels, legend=False, ax=ax)
    ax.set_title(payload.title)
    ax.set_xlabel("category")
    ax.set_ylabel("value")
    filepath = _save_figure(fig, "bar_plot.png")
    return FileResponse(path=filepath, media_type="image/png", filename=filepath.name)


@app.post("/plots/heatmap")
def heatmap_plot(payload: HeatmapRequest) -> StreamingResponse:
    row_lengths = {len(row) for row in payload.matrix}
    if len(row_lengths) != 1:
        raise HTTPException(status_code=400, detail="all matrix rows must have same length")

    columns_count = next(iter(row_lengths))
    if columns_count < 2:
        raise HTTPException(status_code=400, detail="matrix should have at least 2 columns")

    df = pd.DataFrame(payload.matrix)
    if payload.labels is not None:
        if len(payload.labels) != columns_count:
            raise HTTPException(status_code=400, detail="labels length must equal matrix column count")
        df.columns = payload.labels

    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="Blues", vmin=-1, vmax=1, ax=ax)
    ax.set_title(payload.title)
    return _figure_to_png_response(fig)


@app.post("/plots/file/heatmap")
def heatmap_plot_file(payload: HeatmapRequest) -> FileResponse:
    row_lengths = {len(row) for row in payload.matrix}
    if len(row_lengths) != 1:
        raise HTTPException(status_code=400, detail="all matrix rows must have same length")

    columns_count = next(iter(row_lengths))
    if columns_count < 2:
        raise HTTPException(status_code=400, detail="matrix should have at least 2 columns")

    df = pd.DataFrame(payload.matrix)
    if payload.labels is not None:
        if len(payload.labels) != columns_count:
            raise HTTPException(status_code=400, detail="labels length must equal matrix column count")
        df.columns = payload.labels

    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="Blues", vmin=-1, vmax=1, ax=ax)
    ax.set_title(payload.title)
    filepath = _save_figure(fig, "heatmap_plot.png")
    return FileResponse(path=filepath, media_type="image/png", filename=filepath.name)

