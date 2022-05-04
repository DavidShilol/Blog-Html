# -*- coding: utf-8 -*-
"""
Licensed Materials - Property of Qingteng Cloud Security, Inc.
(C) Copyright Qingteng Cloud Security, Inc.. 2019, 2020, 2021 All Rights Reserved
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
File Name   : app.py
Date        : 2022/05/02
Author      : wei.shi@qingteng.cn
Description :
Change Activity:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

import re
import json
from pathlib import Path
from datetime import datetime
import traceback

from flask import (
    Flask,
    request,
    jsonify,
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["get", "post"])
def show_result():
    try:
        params = request.json
        expr = params["expr"]
        if expr:
            ret = str(eval(expr))
            return jsonify(result=ret)
        else:
            return jsonify(result="输点啥呗")
    except Exception as exc:
        print(str(exc) + " | " + str(traceback.print_exc()))
        return jsonify(result="调皮！给我整不会了")


@app.route("/upload", methods=["post"])
def upload():
    file_name = datetime.now().strftime("%Y%m%d-%H%M%S") + ".png"
    absolute_path = Path(__file__).parent.parent / "mt" / file_name
    request.files["file"].save(absolute_path)
    return jsonify(result=f"./mt/{file_name}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8091)
