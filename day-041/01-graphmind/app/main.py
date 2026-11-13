from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .schemas import TrainRequest,EvaluateRequest
from .trainer import train
from .evaluate import evaluate
from .metrics import summarize
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="GraphMind",version="0.1.0"); app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static"); STATE={"run":None}
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/status")
def status():
 r=STATE["run"]; return {"trained":r is not None,"summary":summarize(r["history"]) if r else None,"config":r["config"] if r else None}
@app.post("/api/train")
def train_route(req:TrainRequest):
 try: STATE["run"]=train(req.updates,req.seed,req.learning_rate,req.epochs); return summarize(STATE["run"]["history"])
 except Exception as e: raise HTTPException(400,str(e))
@app.post("/api/evaluate")
def eval_route(req:EvaluateRequest):
 if STATE["run"] is None: raise HTTPException(409,"Train a policy first")
 try:return {"with_communication":evaluate(STATE["run"]["actor"],req.episodes,req.seed,True),"without_communication":evaluate(STATE["run"]["actor"],req.episodes,req.seed,False)}
 except Exception as e:raise HTTPException(400,str(e))
@app.get("/api/history")
def history():return STATE["run"]["history"] if STATE["run"] else []
@app.post("/api/reset")
def reset():STATE["run"]=None;return {"reset":True}