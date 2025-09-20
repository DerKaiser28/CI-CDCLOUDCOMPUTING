from flask import Flask
app = Flask(__name__)

@app.get("/")
def root():
    return "<h1>Hello from Cloud Run (CI/CD)! NOW UPDATED USING CI/CD</h1>", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)