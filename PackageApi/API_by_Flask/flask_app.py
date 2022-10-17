# Editer: Hyean.qin
# Contact: hyean.qin@gmail.com
import logging

from flask import Flask, jsonify, request, Response
from functions import get_datetime,sum_x_y

app = Flask(__name__)
HOST = "localhost"
PORT = 8000


@app.route("/getdatetime")
async def getdatetime():
    name = request.args.get('name', '')  # get的传参方式
    res = jsonify({"{}".format(name): get_datetime()})   # curl "http://localhost:8000/getdatetime?name=curtime"
    print(res.json)
    return res


@app.route("/sumxy")
async def sumxy():
    parameters = request.args   # 直接用 curl "http://localhost:8000/sumxy?x=12&y=23"
    result = sum_x_y(int(parameters['x']), int(parameters['y']))
    print(result)
    return jsonify({'result': result})


@app.post("/sumxy2")  # 使用post方式, json-body传参
async def sumxy2():
    data = request.get_json()
    # curl -X POST "http://localhost:8000/sumxy2" -H "Content-Type:application/json" -d "{\"x\":33, \"y\":24}"
    # 注意点： curl的时候，需要双引号，然而json body里面的key也有双引号，这时候需要用\进行转义，不然会出现异常，无法转成json
    print("data:{}".format(data))
    result = sum_x_y(int(data['x']), int(data['y']))
    print("result:{}".format(result))
    return jsonify({'result': result})


@app.post("/greet")
async def greet():
    name = request.form.get('name', '')  # curl -X POST "http://localhost:8000/greet" -d "name=hyean"
    return "hello, {}".format(name)


@app.post("/greet2")
async def greet2():
    name = request.form.getlist('name')  # getlist by this method
    # curl -X POST "http://localhost:8000/greet" -d "name=hyean" -d "name=hyean2"
    print(name, type(name), len(name))
    return "hello, {}".format(name)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
