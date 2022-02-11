from flask import Flask, render_template, abort, Response, request

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("home.html")

@app.route("/api", methods=["GET", "POST"])
def usage_data():
    request_body = request.args.get("request")
    if request_body is not None:
        if request_body == "php":
            data = [4, 6, 7, 12, 14, 15, 20, 22, 24, 34, 43]
            labels = ["Jan.", "Feb.", "Mar.", "May", "June", "Jully", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
            return Response(f"{{'data': '{data}', 'labels': {labels}}}", status=200, mimetype='application/json')
        if request_body == "ephp":
            data = [10, 11, 13, 15, 17, 24, 27, 37, 55, 67, 80]
            labels = ["Jan.", "Feb.", "Mar.", "May", "June", "Jully", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
            return Response(f"{{'data': '{data}', 'labels': {labels}}}", status=200, mimetype='application/json')
    return abort(400,description="Missing parameters.")
