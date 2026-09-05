from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_database"]
collection = db["todo_items"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():
    return jsonify({
        "message": "Flask API is working"
    })


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():

    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({
            "error": "itemName and itemDescription are required"
        }), 400

    todo_item = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    result = collection.insert_one(todo_item)

    return jsonify({
        "message": "To-Do item stored successfully",
        "itemId": str(result.inserted_id)
    }), 201


if __name__ == "__main__":
    app.run(debug=True)