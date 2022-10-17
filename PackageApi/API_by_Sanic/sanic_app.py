# Editer: Hyean.qin
# Contact: hyean.qin@gmail.com
from sanic import Sanic, json
from functions import get_datetime,sum_x_y

app = Sanic("CodeToApi")
HOST = "localhost"
PORT = 8000

@app.route("/getdatetime")
async def getdatetime(request):
    return json({"now": get_datetime()})


@app.route("/sumxy")
async def sumxy(request):
    parameters = request.args   # 直接用 curl "http://localhost:8000/sumxy?x=12&y=23"
    result = sum_x_y(int(parameters['x'][0]), int(parameters['y'][0]))
    return json({'result':result})


@app.post("/sumxy2")  # 使用post方式
async def sumxy2(request):
    parameters = request.json
    # curl -X POST "http://localhost:8000/sumxy2" -H "Content-Type:application/json" -d "{\"x\":33, \"y\":24}"
    # 注意点： curl的时候，需要双引号，然而json body里面的key也有双引号，这时候需要用\进行转义，不然会出现异常，无法转成json
    print(parameters)
    result = sum_x_y(int(parameters['x']), int(parameters['y']))
    return json({'result':result})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT,debug=False)
