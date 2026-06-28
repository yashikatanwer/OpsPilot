from flask import Flask, render_template, request
from utils.analysis import analyze_dataset
import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["excel_file"]

        if file:

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            # Read Excel
            df = pd.read_excel(filepath)

            # Get statistics
            summary = analyze_dataset(df)

            # Debug prints
            print(df.head())
            print(summary)

        
            table = df.head().to_html(
                classes="table",
                index=False
            )

            return render_template(
    "table.html",
    tables=[table],
    summary=summary,
)

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)

