import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "yeldizsmart.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

DDL = """
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    name TEXT,
    mobile TEXT UNIQUE,
    reg_no TEXT,
    car_model TEXT,
    variant TEXT,
    year TEXT,
    km TEXT,
    address TEXT,
    follow_up TEXT,
    source TEXT,
    context TEXT,
    license TEXT,
    remark TEXT
);
"""

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(DDL)
    return conn

def insert_lead(row: dict):
    conn = get_conn()
    with conn:
        conn.execute(
            """
            INSERT OR IGNORE INTO leads (
                date, name, mobile, reg_no, car_model, variant, year,
                km, address, follow_up, source, context, license, remark
            ) VALUES (
                :date, :name, :mobile, :reg_no, :car_model, :variant, :year,
                :km, :address, :follow_up, :source, :context, :license, :remark
            )
            """,
            row,
        )
    conn.close()
