from fastapi import FastAPI,Query
from .models import DocumentIn,Hit
from .store import Store
from .retriever import search
app=FastAPI(title='RAG Knowledge Service',version='1.0.0'); store=Store()
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/v1/documents')
def ingest(doc:DocumentIn): return {'document_id':store.add(doc.title,doc.text)}
@app.get('/v1/search',response_model=list[Hit])
def retrieve(q:str=Query(min_length=2),limit:int=Query(default=5,ge=1,le=20)): return search(store.all(),q,limit)