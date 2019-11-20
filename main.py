# -*- coding: UTF-8 -*-

import result_with_input_pros2 as mdl
import codecs
import json
from flask import Flask, jsonify, Response
app = Flask(__name__)


@app.route('/<inp>')
def index(inp):
    #print(inp)
    #f = codecs.open("input.txt", "r", "utf8")
    #inp = f.read()

    res = mdl.getresult(inp)
    #print(res)
    jsondata = json.dumps(res, ensure_ascii=False)
    response = Response(jsondata, content_type="application/json; charset=utf-8")
    return response


if __name__ == "__main__":
    app.run(debug=True)

