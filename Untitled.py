from flask import Flask, request, redirect, url_for, render_template
import openai, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("API_KEY")
model1 = "text-curie-001"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Untitled_Home.html")

@app.route("/about")
def about():
    return render_template("Untitled_About.html")

@app.route("/<food>")
def food(food):
    response1 = openai.Completion.create(prompt = "Do not include a title, ONLY write a paragraph of recipe and instructions on how to make " + food, model=model1, max_tokens=350, temperature=0.7)
    response2 = openai.Completion.create(prompt = "Do not include a title, ONLY Write a 30 word paragraph description of this " + food, model=model1, max_tokens=300, temperature=0.7)
    response3 = openai.Completion.create(prompt = "ONLY Write a short paragraph of allergies that are associated with this: " + food, model=model1, max_tokens=300, temperature=0.7)
    return render_template("Untitled_Generate.html", content=food, subcontent=response1.choices[0].text, description=response2.choices[0].text, allergy=response3.choices[0].text)

if __name__ == "__main__":
    app.run()