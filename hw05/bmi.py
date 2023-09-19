from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def first_page():
    return """
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
   <form method="GET" action="/bmi">
        <h2>BMI 지수 계산하기</h2>
        <label>키를 입력하세요. => </label>
        <input type="text" name="height">
        <label>몸무게를 입력하세요. => </label>
        <input type="text" name="weight">
        <button type="submit">출력</button>
    </form>


</body>
</html>

    """


@app.route("/hello")
def hello_world():
    return "<a href='/'>첫페이지</a> <a href='/hello'>hello</a><p>Hello, World!</p>"


@app.route("/bmi")
def bmi():
    h = int(request.args.get('height'))
    w = int(request.args.get('weight'))
    resp = ""
    resp += "<html>\n"
    resp += '<meta charset="utf-8">\n'
    resp += "<body>\n"
    resp += f"<h2>키:{h}cm 몸무게:{w}kg</h2>\n"
    resp += "<div>\n"


    resp += f"BMI지수는 {w / (h/100) * (h/100)}입니다.<br>\n"
    resp += "</div>\n"
    resp += "</body>\n"
    resp += "</html>\n"

    return resp


app.run(host="0.0.0.0")