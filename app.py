from flask import Flask, render_template, request
import openai
import os
from models.main_checker import chatGPT
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        q = data["question"]
        a = data["answer"]
        response = chatGPT(q, a)
        return render_template("home.html", response=response)
    except:
        return render_template("home.html", response="Something went wrong!")


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT") or 5000)
