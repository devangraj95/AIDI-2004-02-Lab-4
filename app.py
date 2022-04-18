from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = []
    params = ["Weight", "Length1", "Length2", "Length3", "Height", "Width"]
    for i in params:
        data.append(float(request.form[i]))
    y_pred = model.predict([data])
    prediction_text = f"The species is {y_pred[0]}"
    return render_template("index.html", prediction_text=prediction_text)


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
