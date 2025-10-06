from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(ok=True, msg="Hello, CI!")

if __name__ == "__main__":
    app.run()
