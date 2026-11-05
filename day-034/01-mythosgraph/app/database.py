import sqlite3
from .config import DB_PATH
SCHEMA="""
CREATE TABLE IF NOT EXISTS characters(id TEXT PRIMARY KEY,name TEXT NOT NULL,role TEXT NOT NULL DEFAULT 'npc');
CREATE TABLE IF NOT EXISTS events(id TEXT PRIMARY KEY,event_type TEXT NOT NULL,actor_id TEXT NOT NULL,target_id TEXT,summary TEXT NOT NULL,importance INTEGER NOT NULL,location TEXT,visibility TEXT NOT NULL,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS witnesses(event_id TEXT NOT NULL,character_id TEXT NOT NULL,PRIMARY KEY(event_id,character_id));
CREATE TABLE IF NOT EXISTS memories(id INTEGER PRIMARY KEY AUTOINCREMENT,character_id TEXT NOT NULL,event_id TEXT NOT NULL,summary TEXT NOT NULL,importance INTEGER NOT NULL,source_type TEXT NOT NULL,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,UNIQUE(character_id,event_id));
CREATE TABLE IF NOT EXISTS relationships(source_id TEXT NOT NULL,target_id TEXT NOT NULL,score INTEGER NOT NULL DEFAULT 0,updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(source_id,target_id));
CREATE TABLE IF NOT EXISTS relationship_events(id INTEGER PRIMARY KEY AUTOINCREMENT,source_id TEXT,target_id TEXT,delta INTEGER,reason TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS facts(id TEXT PRIMARY KEY,subject TEXT NOT NULL,predicate TEXT NOT NULL,object TEXT NOT NULL,source TEXT NOT NULL,confidence REAL NOT NULL,created_at TEXT DEFAULT CURRENT_TIMESTAMP);
"""
def connect():
 DB_PATH.parent.mkdir(parents=True,exist_ok=True)
 c=sqlite3.connect(DB_PATH);c.row_factory=sqlite3.Row;return c
def init_db():
 with connect() as c:c.executescript(SCHEMA)