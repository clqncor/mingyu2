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
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
   <form id='form_id' method="GET" action="javascript:post_query()">
        <h2>BMI 지수 계산하기</h2>
        <label>키를 입력하세요. => </label>
        <input type="text" name="height">
        <label>몸무게를 입력하세요. => </label>
        <input type="text" name="weight">
        <button type="submit">출력</button>
    </form>
    <div id="results"></div>
<script>
function post_query() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/bmi",
        data: $("#form_id").serialize(),
        success: update_result,
        dataType: "html"
    });
}
function update_result(data) {
$("#results").html(data);
}
</script>

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


    resp += f"BMI지수는 {w / (h/100)**2 }입니다.<br>\n"
    resp += "</div>\n"
    resp += "</body>\n"
    resp += "</html>\n"

    return resp


app.run(host="0.0.0.0", debug=True)