from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .schemas import TrainRequest,EvalRequest
from . import trainer,evaluator,analytics,serialization,environment
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="ArenaRL",version="0.1.0",description="Multi-agent tabular reinforcement learning lab")
app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")
SESSION={"training":None,"evaluation":None}
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/status")
def status():
 r=SESSION["training"];return {"trained":r is not None,"training":analytics.summarize(r["history"]) if r else None,"policy":serialization.policy_summary(r["q_tables"]) if r else None,"evaluation":SESSION["evaluation"]}
@app.post("/api/train")
def train(req:TrainRequest):
 try:
  SESSION["training"]=trainer.train(req.episodes,req.seed,req.alpha,req.gamma,req.epsilon);SESSION["evaluation"]=None
  return {"summary":analytics.summarize(SESSION["training"]["history"]),"policy":serialization.policy_summary(SESSION["training"]["q_tables"]),"hyperparameters":SESSION["training"]["hyperparameters"]}
 except Exception as e:raise HTTPException(400,str(e))
@app.post("/api/evaluate")
def evaluate(req:EvalRequest):
 if SESSION["training"] is None:raise HTTPException(409,"Train agents before evaluation")
 SESSION["evaluation"]=evaluator.evaluate(SESSION["training"]["q_tables"],req.episodes,req.seed,req.opponent);return SESSION["evaluation"]
@app.get("/api/history")
def history():return SESSION["training"]["history"] if SESSION["training"] else []
@app.get("/api/policy")
def policy():
 if SESSION["training"] is None:raise HTTPException(404,"No trained policy yet")
 return SESSION["training"]["q_tables"]
@app.post("/api/reset")
def reset():SESSION.update(training=None,evaluation=None);return {"reset":True}