import random
import string
from flask import Flask

app = Flask(__name__)

@app.route("/generate-password")
def generate_password():
    password_length = random.randint(10, 20)

    return "".join(
        random.choices(
            string.digits + string.ascii_letters + string.punctuation, k = password_length
        )
    )



if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
