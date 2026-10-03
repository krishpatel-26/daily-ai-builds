import logging
from fastapi import FastAPI,HTTPException
from .config import Settings
from .models import MemoryCreate
from .store import MemoryStore
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
app=FastAPI(title='Agent Memory Service',version='1.0.0'); settings=Settings(); store=MemoryStore(settings.db_path)
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/memories')
def create_memory(memory:MemoryCreate):
 try:return store.add(memory)
 except Exception as exc: logging.exception('memory_write_failed'); raise HTTPException(500,'memory write failed') from exc
@app.get('/memories')
def list_memories(user_id:str,agent_id:str): return {'items':store.list(user_id,agent_id)}
@app.get('/memories/search')
def search_memories(user_id:str,agent_id:str,q:str,limit:int=8):
 if not q.strip(): raise HTTPException(400,'q must not be empty')
 return {'items':store.search(user_id,agent_id,q,max(1,min(limit,settings.max_results)))}
