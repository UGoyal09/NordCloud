import os
from flask import Flask
from networkspeed import get_results

app = Flask(__name__)

@app.route("/")
def network_speed():
    return get_results()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))