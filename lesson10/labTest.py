from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
app = FastAPI()
Output_Directory ="plots1"
os.makedirs(Output_Directory, exist_ok=True)

@app.get("/plots/line")
def get_line_plot(points:int=50):
    x=np.arange(points)
    y=np.random.randint(0,100,size=points)
    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("line plot")
    ax.grid(True)
    path=f"{Output_Directory}/line.png"
    fig.savefig(path)
    plt.close(fig)
    return FileResponse(path,media_type="image/png")
class BarRequest(BaseModel):
    labels: List[str]
    values: List[float]
@app.post("/plots/bar")
def get_bar_plot(request: BarRequest):
    fig,ax=plt.subplots()
    sns.barplot(x=request.labels, y=request.values, ax=ax)
    ax.set_title("bar plot")
    path=f"{Output_Directory}/bar.png"
    fig.savefig(path)
    plt.close(fig)
    return FileResponse(path,media_type="image/png")
class HeatMapRequest(BaseModel):
    matrix: List[List[float]]
@app.post("/plots/heatmap")
def get_heatmap_plot(request: HeatMapRequest):
    data=np.array(request.matrix)
    corr = np.corrcoef(data)
    fig,ax=plt.subplots()
    sns.heatmap(corr, annot=False,ax=ax)
    ax.set_title("heatmap")
    path=f"{Output_Directory}/heatmap.png"
    fig.savefig(path)
    plt.close(fig)
    return FileResponse(path,media_type="image/png")

