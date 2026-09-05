from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Git & GitHub Assignment - Flask App"

@app.route("/api")
def api():
    return jsonify({
        "message": "Hello from Flask API",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)