import result_with_input_pros2 as mdl
import codecs
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/<inp>')
def index(inp):
    #print(inp)
    #f = codecs.open("input.txt", "r", "utf8")
    #input = f.read()

    mdl.getresult(inp)
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)

