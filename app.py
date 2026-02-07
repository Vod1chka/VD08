from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://dummyjson.com/quotes/random"


def get_random_quote():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        return {
            "content": data["quote"],
            "author": data["author"]
        }

    except Exception as e:
        print("Ошибка загрузки цитаты:", e)
        return {
            "content": "Не удалось загрузить цитату 😢",
            "author": "Ошибка"
        }


@app.route("/")
def index():
    quote = get_random_quote()
    return render_template("index.html", quote=quote)


if __name__ == "__main__":
    app.run(debug=True)
