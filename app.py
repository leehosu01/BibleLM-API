#flask
from flask import Flask
from BibleLM import inference
app = Flask(__name__)
@app.route("/generate", methods=["GET","POST"])
def generate():
    data = {"success": False}
    # get the request parameters
    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, echo the msg parameter
    if (params != None):
        #view & model work
        data["data"] = params.get("msg")
        data["file_name"] = params.get("file")
        data["success"] = True
    return flask.jsonify(data)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
