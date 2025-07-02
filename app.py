
from flask import Flask, request, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "EasyPDF Backend Running"

@app.route("/pdf-to-word", methods=["POST"])
def pdf_to_word():
    file = request.files["file"]
    input_path = "input.pdf"
    output_path = "output.docx"
    file.save(input_path)

    # Simulate conversion (just copy file as .docx for demo)
    os.rename(input_path, output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run()
