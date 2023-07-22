from flask import Flask, render_template, request, redirect, url_for, json
import openai
import os
from models.main_checker import chatGPT
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return 'Hello World'


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        q = data["question"]
        a = data["answer"]
        response = chatGPT(q, a)
        return json.dumps({"data": response, "ok": True})
    except Exception as e:
        print(e)
        return json.dumps({"message": "Something went wrong", "ok": False})


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT") or 5000)
