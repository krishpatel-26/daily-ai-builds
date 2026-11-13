from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .schemas import TrainRequest,EvalRequest
from . import trainer,evaluator,metrics
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="ArenaCTDE",version="0.1.0");app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static");SESSION={"model":None}
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/status")
def status():
 m=SESSION["model"];return {"trained":m is not None,"summary":metrics.summary(m["history"]) if m else None,"config":m["config"] if m else None}
@app.post("/api/train")
def train(req:TrainRequest):
 try:SESSION["model"]=trainer.train(req.updates,req.seed,req.learning_rate,req.epochs);return metrics.summary(SESSION["model"]["history"])
 except Exception as e:raise HTTPException(400,str(e))
@app.post("/api/evaluate")
def evaluate(req:EvalRequest):
 if not SESSION["model"]:raise HTTPException(409,"Train policy first")
 return evaluator.evaluate(SESSION["model"]["actor"],req.episodes,req.seed)
@app.get("/api/history")
def history():return SESSION["model"]["history"] if SESSION["model"] else []
@app.post("/api/reset")
def reset():SESSION["model"]=None;return {"reset":True}