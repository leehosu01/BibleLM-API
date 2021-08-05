#flask
import flask
from flask import Flask
from BibleLM import inference as model_inference
app = Flask(__name__)

@app.route("/inference", methods=["GET","POST"])
def inference():
    try:
        params = flask.request.json
        if params is None:
            params = flask.request.args

        params = dict(params)
        sentence    = params.get("sentence", "")
        request_cnt = int(params.get("samples", "1"))
        request_cnt = min(8, request_cnt)
        data = {}
        data.update({'candidates': model_inference.inference(sentence, request_cnt) if request_cnt > 0 else []}, "/opt/app/BibleLM/Bible_model_ckpts")
        data.update({"success": True})
    except Exception as e:
        data = {"success": False, 'error' : str(e)}
    return flask.jsonify(data)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(5000), debug=True)
