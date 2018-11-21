from flask import Flask, Response, render_template,url_for, flash, jsonify
import pandas as pd
import urllib, json
import urllib3

app = Flask(__name__)

url = "https://raw.githubusercontent.com/fangshulin/Vis2018/master/dataset/education_expend.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

url2 = "https://raw.githubusercontent.com/fangshulin/Vis2018/master/dataset/literacy.json"
response2 = urllib.request.urlopen(url2)
data1 = json.loads(response2.read())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<year>',methods=['GET', 'POST'])
def api(year):
    y = str(year)
    print(y,data['education_expenditure'][y])
    return jsonify(data['education_expenditure'][y])

@app.route('/vis/<year>',methods=['GET', 'POST'])
def vis(year):
    y = str(year)
    print(y,data1['literacy'][y])
    return jsonify(data1['literacy'][y])

if __name__ == '__main__':
   app.run(debug = True,port=4023)