from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)

client = OpenAI(
  api_key=os.getenv('API_KEY')
)

def start_line():
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
      {"role": "user",
       "content": "write a first part of an unfinished sentence, 10 to 11 words, that could be a beginning of a novel, no ellipsis at the end"}
    ]
  )
  result=completion.choices[0].message.content
  return result


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["GET"])
def generate():
    ai_start=start_line()
    return jsonify({"ai_start": ai_start})

if __name__ == '__main__':
    app.run(debug=True)

