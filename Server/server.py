from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
def UploadVideo():
    file = request.files["video"]
    print(file)
    file.save("video.mp4")
    return jsonify(True)

if __name__ == "__main__":
    app.run(debug=True, port=3333)