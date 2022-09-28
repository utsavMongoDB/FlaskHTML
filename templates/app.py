from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
def home():
    client = MongoClient('mongodb://main_user:test123@partnersagemaker-shard-00-00.fmxyq.mongodb.net:27017,partnersagemaker-shard-00-01.fmxyq.mongodb.net:27017,partnersagemaker-shard-00-02.fmxyq.mongodb.net:27017/?ssl=true&replicaSet=atlas-xkp8ju-shard-0&authSource=admin&retryWrites=true&w=majority')
    result = client["Employee"]["Details"].find({})
    arr = []
    for val in result:
        values = []
        values.append(val['name'])
        values.append(val['designation'])
        values.append(val['place'])
        arr.append(values)
    print(arr)
    return render_template('content.html', result=arr)
