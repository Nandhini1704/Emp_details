from flask import Flask,request,url_for,render_template,redirect
import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="employee"
)
app = Flask(__name__)

app.config.from_object(__name__)
app.config.from_envvar("FLASKR_SETTINGS",silent=True)

@app.route('/',methods=["GET","POST"])
def index():
    db = mydb.cursor()
    db.execute('select * from emp_detail')
    result= db.fetchall()
    print(result)
    return render_template('index.html',data=result)


@app.route('/Add_emp',methods=["GET","POST"])
def Add_emp():
    if request.method == 'POST':
        name=request.form['name']
        address = request.form['address']
        gender = request.form['gender']
        join_date = request.form['date']
        db=mydb.connection.cursor()
        sql = "insert into emp_detail(Name,Address,Gender,Joindate) value (%s,%s,%s,%s)"
        db.execute(sql,[name,address,gender,join_date])
        mydb.connect()
        mydb.close()
        return redirect(url_for("index"))
    return render_template('Add.html')





if __name__=="__main__":
    app.run(debug=True)