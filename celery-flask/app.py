from flask import Flask,jsonify
from celery import Celery
from celery.result import AsyncResult

app = Flask(__name__)

celery = Celery(
    __name__,
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
    )

@app.route('/')
def home():
    return "hello to celery app"

@celery.task
def find_fibonacci_async(number):
    print("Starting calculation of "+str(number))
    def fib(n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        return fib(n-1)+fib(n-2)
    result = fib(number)
    print("Result of "+str(number))
    return result

@app.route('/add_task/<num>')
def add_task(num):
    task = find_fibonacci_async.delay(int(num))
    return str(task.task_id)

@app.route('/get_status/<task_id>')
def get_status(task_id):
    res =celery.AsyncResult(task_id)
    resp = {
            "ready":res.ready(),
            "status":res.status,
            "result":res.result
            }
    return jsonify(resp)




