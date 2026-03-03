from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return "Video processing coming soon 🔥"
    return """
    <h1>AI Reel Studio</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="clips" multiple><br><br>
        
        <label>Add Lyrics?</label>
        <input type="checkbox" name="lyrics_option"><br><br>

        <textarea name="lyrics" placeholder="Paste lyrics here"></textarea><br><br>

        <button type="submit">Generate Reel</button>
    </form>
    """

if __name__ == "__main__":
    app.run()
