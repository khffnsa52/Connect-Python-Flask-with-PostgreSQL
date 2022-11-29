#app.py
from flask import Flask, render_template
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
app.secret_key = "zkvlvk"
 
DB_HOST = "localhost"
DB_NAME = "tstdb"
DB_USER = "postgres"
DB_PASS = "1234567890"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM heart_failure"
    cur.execute(s) # Execute the SQL
    list_data = cur.fetchall()
    return render_template('index.html', list_data = list_data)

if __name__ == "__main__":
    app.run(debug=True)