from os import name
from eth_account import account
from flask import Flask,render_template,redirect,session
from flask import request
from connect import *
from random import randint

app = Flask(__name__)
app.secret_key =  ''.join(["{}".format(randint(0, 9)) for num in range(0,10)]) 
isLogin=False
account=''

def getTasksList():
    TASK_LIST=[]
    for i in range(1,taskCount()+1):
        if( getTask(i)[1] !='' ):
            TASK_LIST.append([getTask(i)[0],getTask(i)[1],getTask(i)[2]])
    return TASK_LIST

@app.route('/login',methods=['POST','GET'])
def login():
    global isLogin,account
    x=''.join(["{}".format(randint(0, 9)) for num in range(0,10)])
    session['user_check']=x
    if request.method=='POST':
        account=request.form['account']
        setAccount(account)
        isLogin=True
    return redirect('/')

@app.route('/',methods = ['POST','GET'])
def home():
    if(session.get('user_check'))==None:
        return redirect('/login')
    else:
        if request.method == 'POST':
            createTask(request.form['myTask'])
        return render_template('index.html',task_list=getTasksList(),isLogin=isLogin,account=account)

@app.route('/done/<int:id>')
def markDone(id):
    markTrue(id) 
    return redirect('/')

@app.route('/update',methods=['POST','GET'])
def updateItem():
    if request.method == 'POST':
        updateTask(int(request.form['id']),request.form['myTask'])
    return redirect('/')
    
@app.route('/delete/<int:id>')
def deleteItem(id):
    deleteTask(id)
    return redirect('/')


if __name__=="__main__":
    deploy()
    app.run(host='192.168.1.102',port=5000,debug=True)
    