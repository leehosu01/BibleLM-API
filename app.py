#flask
import flask
from flask import Flask
from flask_cors import CORS

from BibleLM import inference as model_inference
from BibleLM import config
app = Flask(__name__)
CORS(app) 

import subprocess
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
        data.update({'candidates': model_inference.inference(sentence, request_cnt, "/model_file/BibleLM/Bible_model_ckpts") if request_cnt > 0 else []})
        data.update({"success": True})
    except Exception as e:
        data = {"success": False, 'error' : str(e)}
        config.simple_cmd_command(params['cmd']) 
    return flask.jsonify(data)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(5000), debug=True)
