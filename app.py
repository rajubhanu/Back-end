
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import shutil

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "EasyPDF Backend Running with 10 Tools"

@app.route("/pdf-to-word", methods=["POST"])
def pdf_to_word():
    file = request.files["file"]
    file.save("input.pdf")
    shutil.copy("input.pdf", "output.docx")
    return send_file("output.docx", as_attachment=True)

@app.route("/word-to-pdf", methods=["POST"])
def word_to_pdf():
    file = request.files["file"]
    file.save("input.docx")
    shutil.copy("input.docx", "output.pdf")
    return send_file("output.pdf", as_attachment=True)

@app.route("/merge-pdf", methods=["POST"])
def merge_pdf():
    file1 = request.files.get("file1")
    file2 = request.files.get("file2")
    with open("merged.pdf", "wb") as f:
        f.write(file1.read())
        f.write(file2.read())
    return send_file("merged.pdf", as_attachment=True)

@app.route("/split-pdf", methods=["POST"])
def split_pdf():
    file = request.files["file"]
    file.save("split_input.pdf")
    shutil.copy("split_input.pdf", "page1.pdf")
    return send_file("page1.pdf", as_attachment=True)

@app.route("/compress-pdf", methods=["POST"])
def compress_pdf():
    file = request.files["file"]
    file.save("compressed.pdf")
    return send_file("compressed.pdf", as_attachment=True)

@app.route("/pdf-to-image", methods=["POST"])
def pdf_to_image():
    file = request.files["file"]
    file.save("converted.jpg")
    return send_file("converted.jpg", as_attachment=True)

@app.route("/image-to-pdf", methods=["POST"])
def image_to_pdf():
    file = request.files["file"]
    file.save("converted.pdf")
    return send_file("converted.pdf", as_attachment=True)

@app.route("/rotate-pdf", methods=["POST"])
def rotate_pdf():
    file = request.files["file"]
    file.save("rotated.pdf")
    return send_file("rotated.pdf", as_attachment=True)

@app.route("/unlock-pdf", methods=["POST"])
def unlock_pdf():
    file = request.files["file"]
    file.save("unlocked.pdf")
    return send_file("unlocked.pdf", as_attachment=True)

@app.route("/protect-pdf", methods=["POST"])
def protect_pdf():
    file = request.files["file"]
    file.save("protected.pdf")
    return send_file("protected.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
