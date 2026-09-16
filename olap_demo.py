from pathlib import Path
import sqlite3

p = Path(__file__).resolve().parent / 'data' / 'oltp.db'
if not p.exists():
    raise SystemExit('Run lab.py first')

with sqlite3.connect(p) as con:
    print('Before:', con.execute('SELECT * FROM orders').fetchall())

    # UPDATE สถานะจาก PENDING เป็น PAID โดยเช็คทั้ง order_id และ status
    cur = con.execute(
        "UPDATE orders SET status = 'PAID' WHERE order_id = 'O1004' AND status = 'PENDING'"
    )
    print('Updated rows (rowcount):', cur.rowcount)

    print('After:', con.execute('SELECT * FROM orders').fetchall())