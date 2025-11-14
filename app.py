from flask import Flask, jsonify, render_template,request
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


@app.route("/quotes", methods=['POST'])
def create_quote():
  new_data = request.get_json()
  i=0
  for quote in quotes_data:
    if quote["id"]>i:
      i=quote["id"]
  new_data["id"]=i+1
  quotes_data.append(new_data)
  print("data = ", new_data)
  return jsonify(new_data), 201

@app.route("/quotes/<int:quote_id>", methods=['DELETE'])
def delete_quote(quote_id: int):
  for quote in quotes_data:
    if quote["id"]==quote_id:
      quotes_data.remove(quote)
      return jsonify({"message": f"Цитата с номером {quote_id} удалена"}),200
  return jsonify({"message": f"Цитата с номером {quote_id} не найдена"}), 400
  
@app.route('/quote/<int:quote_id>')
def get_quote_text(quote_id):
    quote = next((q for q in quotes_data if q["id"] == quote_id), None)
    if quote:
        return jsonify({"text": quote["text"]})
    else:
        return jsonify({"error": "Quote not found"}), 404

if __name__=="__main__":
    app.run(debug=True)

    

