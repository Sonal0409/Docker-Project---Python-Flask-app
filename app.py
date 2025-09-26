
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
DATA_FILE = "/data/notes.txt"

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if request.method == "POST":
        note = request.json.get("note", "")
        with open(DATA_FILE, "a") as f:
            f.write(note + "\n")
        return jsonify({"message": "Note saved"}), 201

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            notes = f.readlines()
    else:
        notes = []
    return jsonify({"notes": [n.strip() for n in notes]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

