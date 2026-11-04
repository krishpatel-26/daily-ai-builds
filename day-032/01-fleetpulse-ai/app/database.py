"""SQLite schema and connection lifecycle."""
import sqlite3
from contextlib import contextmanager
from .config import DB_PATH
SCHEMA="""
CREATE TABLE IF NOT EXISTS assets(
 asset_id TEXT PRIMARY KEY,name TEXT NOT NULL,asset_type TEXT NOT NULL,location TEXT NOT NULL,
 criticality TEXT NOT NULL,temperature_limit REAL NOT NULL,vibration_limit REAL NOT NULL,
 pressure_min REAL NOT NULL,pressure_max REAL NOT NULL,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS telemetry(
 id INTEGER PRIMARY KEY AUTOINCREMENT,asset_id TEXT NOT NULL,timestamp TEXT NOT NULL,
 temperature REAL NOT NULL,vibration REAL NOT NULL,pressure REAL NOT NULL,current REAL NOT NULL,
 rpm REAL NOT NULL,runtime_hours REAL NOT NULL,FOREIGN KEY(asset_id) REFERENCES assets(asset_id)
);
CREATE INDEX IF NOT EXISTS idx_telemetry_asset_time ON telemetry(asset_id,timestamp DESC);
CREATE TABLE IF NOT EXISTS work_orders(
 id INTEGER PRIMARY KEY AUTOINCREMENT,asset_id TEXT NOT NULL,title TEXT NOT NULL,priority TEXT NOT NULL,
 assigned_to TEXT NOT NULL,due_date TEXT NOT NULL,notes TEXT NOT NULL,status TEXT NOT NULL DEFAULT 'open',
 resolution_notes TEXT NOT NULL DEFAULT '',created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
 closed_at TEXT,FOREIGN KEY(asset_id) REFERENCES assets(asset_id)
);
"""
@contextmanager
def connect():
 db=sqlite3.connect(DB_PATH);db.row_factory=sqlite3.Row
 try:
  db.execute("PRAGMA foreign_keys=ON")
  yield db;db.commit()
 finally:db.close()
def initialize():
 with connect() as db:db.executescript(SCHEMA)
