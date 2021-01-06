# This is a sample Python script.
from flask import Flask, make_response, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    df = pd.read_excel("sample.xlsx")
    return df.to_html()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
