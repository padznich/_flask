import sqlite3 as sql
from flask import Flask, render_template, request
'''
conn = sqlite3.connect('dbs_database.db')
print "Opened database successfully"
conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print "Table created successfully"
conn.close()
'''

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dbs_home.html')


@app.route('/enternew')
def new_student():
    return render_template('dbs_student.html')


@app.route('/addrec',methods=['POST', 'GET'])
def addrec():
    if request.method=='POST':
        try:
            nm=request.form['nm']
            addr=request.form['add']
            city=request.form['city']
            pin=request.form['pin']
            with sql.connect("dbs_database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES ('{}','{}','{}','{}')".format(nm,addr,city,pin) )
                con.commit()
                msg= "Record successfully added"
        except:
            con.rollback()
            msg= "error in insert operation"
        finally:
            return render_template("dbs_result.html",msg=msg)
            con.close()


@app.route('/list')
def list():
    con=sql.connect("dbs_database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows=cur.fetchall()
    return render_template("dbs_list.html",rows=rows)


if __name__ == '__main__':
    app.run(debug=True)