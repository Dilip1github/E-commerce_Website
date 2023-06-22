from flask import Flask,render_template,redirect,request
import pymysql

app = Flask(__name__)

@app.route("/create")
def create():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

@app.route("/forgotpassword")
def forgotpassword():
    return render_template("forgot.html")
# Register

@app.route("/store",methods = ["POST"])
def store():
    id = request.form["userid"]
    user = request.form["username"]
    phone = request.form["phoneno"]
    passw = request.form["password"]
    cpassw = request.form["cpassword"]
    try:
        con = pymysql.connect(host="localhost",user="root",password="",database="registration")
        cur = con.cursor()
        sql = "insert into regdata values('{}','{}',{},'{}','{}');".format(id,user,phone,passw,cpassw)
        cur.execute(sql)
        con.commit()
    except Exception as e:
        print("Failed to insert",e)
    return render_template("output.html")

# Fetch the data

@app.route("/")
def logind():
    try:
        con = pymysql.connect(host="localhost",user="root",password="",database="registration")
        cur = con.cursor()
        sqls = "select * from regdata"
        cur.execute(sqls)
        data = cur.fetchall()
    except Exception as e:
        print("Error",e)
    return render_template("login.html",data=data)

# Fetch to login

@app.route("/under",methods=["POST"])
def under():
    userid = request.form["lguserid"]
    upass = request.form["lgpassword"]
    con = pymysql.connect(host="localhost",user="root",password="",database="registration")
    cur = con.cursor()
    sqll = ("Select * from regdata where UserID = '{}' and Password = '{}'").format(userid,upass)
    cur.execute(sqll)
    dat = cur.fetchone()
    if dat != None:
        return render_template("success.html")
    else:
        return redirect('/')
    
# Forgot password

@app.route("/forgot",methods=["POST"])
def forgot():
    try:
        fguerid = request.form["fguserid"]
        fgpass = request.form["fgpassword"]
        fgcpass = request.form["fgcpassword"]
        con = pymysql.connect(host="localhost",user="root",password="",database="registration")
        cur = con.cursor()
        sqlq = ("update regdata set Password='{}',Confirm_Password='{}' where UserID='{}'").format(fgpass,fgcpass,fguerid)
        cur.execute(sqlq)
        con.commit()
    except Exception as a:
        print("Error",a)
    return render_template("login.html")

app.run(debug=True)