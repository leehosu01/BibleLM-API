#flask
import flask
from flask import Flask
from BibleLM import inference
app = Flask(__name__)
@app.route("/inference", methods=["GET","POST"])
def inference():
    try:
        params = flask.request.json
        if params is None:
            params = flask.request.args

        params = dict(params)
        sentence    = params.get("sentence", "")
        request_cnt = int(params.get("cnt", "1"))
        data.update({'candidates': inference.inference(sentence, request_cnt)})
        data.update({"success": True})
    except Exception as e:
        data = {"success": False, 'error' : str(e)}
    return flask.jsonify(data)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
