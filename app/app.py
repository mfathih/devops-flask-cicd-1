from flask import Flask, render_template
from datetime import datetime
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        environment=os.getenv("APP_ENV", "local"),
        deployed_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
