from flask import Flask, request
import pandas as pd
import random
import string


app = Flask(__name__)

@app.route("/calculate-average", methods=['GET'])
def calculate_average():
    df = pd.read_csv('hw.csv')

    df.columns = df.columns.str.strip()

    column_name = "Height(Inches)"
    column_name_1 = "Weight(Pounds)"

    if column_name not in df or column_name_1 not in df:
        return "Column doesn't found", 400

    average_height = df["Height(Inches)"].mean()
    average_weight = df["Weight(Pounds)"].mean()

    results = (f"Average value for {column_name} = {average_height}\n |"
               f" Average value for {column_name_1} = {average_weight}")

    return results



@app.route("/generate-password")
def generate_password():
    password_length = random.randint(10, 20)

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    if password_length > 3:
        password += random.choices(
            string.ascii_letters + string.digits + string.punctuation,
            k=password_length - 3
        )

    random.shuffle(password)

    return "".join(
        random.choices(
            string.digits + string.ascii_letters + string.punctuation, k = password_length
        )
    )



if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )




