from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

tasks=[]

def addTask(task):
    global tasks
    tasks.append(task)

def get_tasks():
    return tasks

@app.route('/')
def Index():
    return render_template('Index.html',tasks=get_tasks())

@app.route('/AddTasks',methods=['POST','GET'])
def AddTask_route():
    task=request.form['task']
    addTask(task)
    return redirect(url_for('Index'))

if __name__=='__main__':
    app.run(debug=True)
    