from flask import Flask, jsonify, render_template
import random
app=Flask(__name__)
about_me ={
    "surname": "Мазанов",
    "name":"Алексей",
    "email":"mazalexey@yandex.ru"
    }
quotes_data = [
    {
        "id": 3,
        "author": "Rick Cook",
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы c большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше идиотов. Пока вселенная побеждает."
    },
    {
        "id": 5,
        "author": "Waldi Ravens",
        "text": "Программирование на C похоже на быстрые танцы на только что отполированном полу людей c острыми бритвами в руках."
    }
]

@app.route("/")
def hello_world():
    return "Hello, World"

@app.route("/about")
def about():
    return about_me

@app.route("/quotes")
def quotes():
    return jsonify(quotes_data)

@app.route("/quotes/count")
def quotes_count():
    return {"count": len(quotes_data)}

@app.route("/quotes/random")
def quotes_random():
    quote = random.choice(quotes_data)
    return jsonify(quote["text"])


@app.route('/quote/<int:quote_id>')
def get_quote_text(quote_id):
    quote = next((q for q in quotes_data if q["id"] == quote_id), None)
    if quote:
        return jsonify({"text": quote["text"]})
    else:
        return jsonify({"error": "Quote not found"}), 404

if __name__=="__main__":
    app.run(debug=True)

    

